# Scoring Notes — SYS024 PostgreSQL

## Identification

- **System ID :** SYS024

- **System name :** PostgreSQL

- **Domain :** technological

- **Subdomain :** système de gestion de base de données relationnelle / objet-relationnelle

- **Scale :** meso

- **Date scored :** 2026-04-02

- **Scorer :** Noé

- **Confidence globale :** high

## Sources

1. *PostgreSQL 18.3 Documentation*

2. Hellerstein, Stonebraker, Hamilton, *Architecture of a Database System*

3. Ramakrishnan, Gehrke, *Database Management Systems*

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                                          |
| --------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Oui sans ambiguïté : client/frontend d’un côté, serveur/backend de l’autre, dans un modèle client/serveur explicite.                                                                                                                                                                   |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Oui : connexion et supervision des processus, chaîne parser/rewrite/planner/executor, puis stockage/système physique. La documentation interne distingue explicitement ces étages.                                                                                                     |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | Oui : on peut distinguer au moins client, postmaster/backend, pipeline de requête, catalogues/gestion transactionnelle, puis stockage physique/WAL/mémoire partagée/noyau. Les sources décrivent séparément processus, query processor, catalogs, access methods, storage, WAL et IPC. |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Oui : chaque niveau remplit une fonction distincte — acceptation des connexions, parsing/réécriture, optimisation, exécution, catalogues, accès/indexation, concurrence, récupération.                                                                                                 |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Oui : les catalogues, statistiques, index et règles orientent planification et exécution, tandis que l’activité d’exécution met à jour statistiques, WAL, tables, vacuum, etc. Il y a donc contrainte descendante et rétroaction montante.                                             |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Aucune hésitation majeure. PostgreSQL est un cas très net de système technologique multi-niveaux.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Oui : une modification locale touchant index, règles, statistiques, ou verrous change le comportement du planner, de l’executor, de la concurrence ou des requêtes.                                                                                                                                           |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Oui : une requête textuelle traverse connexion, parseur, rewriter, optimizer, executor, puis stockage ; inversement, des contraintes du stockage/WAL/verrouillage remontent vers l’exécution observable.                                                                                                      |
| P3 : Propagation modifie l'état global observable             | 1     | Oui : WAL, réplication, vacuum, verrouillage, isolation et updates changent l’état global visible du cluster ou de la base, y compris pour d’autres clients.                                                                                                                                                  |
| P4 : Isolement difficile sans modification structurelle       | 1     | Oui dans l’ensemble : PostgreSQL repose sur mémoire partagée, sémaphores, catalogues communs, WAL, processus multiples et mécanismes transactionnels imbriqués ; isoler une perturbation importante demande souvent reconfiguration, désactivation d’un sous-système, changement de schéma ou réorganisation. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Oui : le système couple planification, statistiques, accès indexés, MVCC, WAL, vacuum, catalogues et droits ; ce n’est pas une juxtaposition modulaire faible.                                                                                                                                                |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
P4 pourrait recevoir 0.5 dans une lecture plus stricte, car certaines perturbations restent localisables. Je garde 1 car, à l’échelle du système pertinent ici, les couplages structurels sont très forts.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                             |
| ---------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Oui : coordination explicite par planificateur, gestionnaire transactionnel, locks, WAL, autovacuum, catalogue, mémoire partagée et sémaphores.                                           |
| I2 : Réduction de variance observable    | 1     | Oui : le système vise à rendre l’accès concurrent et les requêtes compatibles avec un état cohérent, via isolation, sérialisation, recovery, vacuum et statistiques de planification.     |
| I3 : Synchronisation multi-niveaux       | 1     | Oui : synchronisation entre processus backend, stockage, journalisation, réplication, workers d’entretien, et vues/statistiques de suivi.                                                 |
| I4 : Boucles de rétroaction globales     | 1     | Oui : les statistiques nourrissent le planner ; l’activité du système déclenche vacuum/analyze ; les mécanismes de monitoring et d’autovacuum ajustent en continu le maintien du système. |
| I5 : Maintien d'un état global cohérent  | 1     | Oui : c’est un objectif constitutif du DBMS, assuré par intégrité transactionnelle, MVCC, WAL, verrous, contraintes et récupération.                                                      |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Aucune hésitation majeure. PostgreSQL est précisément conçu comme machine d’intégration cohérente.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                |
| -------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | Oui : l’attracteur central est un état transactionnellement valide, cohérent, requêtable et récupérable, défini par SQL, contraintes, MVCC et WAL.                                                                                                                                           |
| N2 : Correction active d'écart               | 1     | Oui : récupération WAL, checksums, verrouillage, gestion des conflits de sérialisation, autovacuum et maintenance corrigent activement les écarts ou dérives.                                                                                                                                |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Oui : ordre des priorités explicite entre durabilité/WAL, modes de verrous, niveaux d’isolation, privilèges, politiques de sécurité, mécanismes anti-wraparound.                                                                                                                             |
| N4 : Mécanisme interne de stabilisation      | 1     | Oui : autovacuum launcher/workers, monitoring, replication/failover, checksums, hot standby, WAL et statistiques sont des mécanismes internes de stabilisation.                                                                                                                              |
| N5 : Résistance aux perturbations prolongées | 0.5   | Résistance réelle mais non absolue : PostgreSQL dispose de réplication, failover, hot standby, recovery et checksums, mais la documentation signale aussi des limites en cas de forte contention, erreurs de sérialisation, décalage de réplication ou certaines formes de panne/corruption. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
N5 pourrait monter à 1 si l’on valorise surtout la robustesse architecturale ; je le laisse à 0.5 car la résistance dépend fortement de la configuration, de l’exploitation et du type de perturbation.

**Distinction normativité endogène / imposée :**  
Normativité hybride. Endogène au runtime une fois le système configuré : WAL, MVCC, locks, retry, vacuum, checksums, rule system, planner. Mais une partie importante des normes est aussi imposée de l’extérieur par les humains via schéma, privilèges, politiques, extensions, configuration et triggers.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                             |
| -------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Oui : très forte capacité de réglage local via paramètres serveur, options de planification, vacuum/autovacuum, logging, connexion, locks, etc.                                                                                                           |
| R2 : Modification durable de configuration interne | 1     | Oui : changement durable de configuration du cluster, rôles, privilèges, schémas, index, partitions, replication setup, paramètres persistants.                                                                                                           |
| R3 : Reconfiguration de réseau ou de structure     | 1     | Oui : partitions attach/detach, inheritance, foreign tables, access methods, extensions, réplication logique, failover et workers permettent des reconfigurations structurelles importantes.                                                              |
| R4 : Modification des mécanismes de régulation     | 1     | Oui : l’utilisateur peut modifier règles, triggers, event triggers, policies de sécurité, procédures, extensions d’index, autovacuum et divers paramètres de contrôle.                                                                                    |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | Oui au sens faible seulement : PostgreSQL permet d’ajouter règles, triggers, politiques, types, fonctions et extensions, mais cette production de nouvelles règles n’est pas autonome ; elle dépend d’une intervention de concepteur ou d’administrateur. |

**Score A5 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
R5 est le point décisif. Si l’on compte la générativité par usager comme suffisante, on peut mettre 1. Si l’on exige une auto-révision intrinsèque sans opérateur externe, 0.5 est plus juste.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 1.00  |
| A2  | 1.00  |
| A3  | 1.00  |
| A4  | 0.90  |
| A5  | 0.90  |

### Gradients (calculés)

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | 0.00   |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | 0.10   |
| Δ₄₃ = A4 − A3 | -0.10  |

### Classification

- **Régime primaire :** non calculé ici

- **Régime secondaire :** non calculé ici

- **Marge :** non calculée ici

- **Surprise par rapport au jugement intuitif :** faible ; PostgreSQL ressort comme système technologique très hiérarchisé, très intégré, fortement normatif et hautement révisable, avec une limite surtout sur l’autonomie de production de nouvelles règles.

---

## Notes libres

PostgreSQL apparaît comme un cas presque canonique de système technologique fortement organisé : profondeur hiérarchique nette, couplage transversal fort, intégration élevée, normativité robuste, plasticité importante.

Le seul frein à un profil maximal partout tient à A5-R5 : la plasticité est immense, mais elle est surtout **catalog-driven et user-driven**, pas auto-créatrice au sens fort. De même, A4 reste très haut sans être absolu, car la robustesse aux perturbations prolongées dépend de l’architecture déployée, des pratiques d’administration et du type de contrainte subi.


