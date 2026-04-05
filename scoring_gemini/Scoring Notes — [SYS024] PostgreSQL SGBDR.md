# Scoring Notes — [SYS024] PostgreSQL

## Identification

- **System ID :** SYS024

- **System name :** PostgreSQL

- **Domain :** technological

- **Subdomain :** Database Management System (DBMS)

- **Scale :** meso

- **Date scored :** 2026-04-03

- **Scorer :** LLM

- **Confidence globale :** high

## Sources

1. Architecture of a Database System (Hellerstein, Stonebraker, et al.)

2. Database Management Systems, 3rd Edition (Ramakrishnan, Gehrke)

3. postgresql-18-A4.txt (Documentation technique PostgreSQL)

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                               |
| --------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | PostgreSQL sépare clairement l'analyse logicielle (parsing/planning) et l'exécution physique (accès aux pages disque).                                                          |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | Le système s'articule autour de multiples couches : gestionnaire de requêtes, gestionnaire de transactions, et gestionnaire de stockage/fichiers.                               |
| H3 : ≥ 4 niveaux causaux distincts            | 1         | On observe la pile complète : Matériel/OS sous-jacent -> Storage Engine (Buffer Pool/WAL) -> Relational Engine (Query Optimizer) -> Couche de transport/connexion client.       |
| H4 : Niveaux fonctionnellement différenciés   | 1         | Chaque niveau a un domaine strict : le planificateur de requêtes ne gère pas les verrous, le gestionnaire de mémoire tampon (Buffer Manager) ne comprend pas le langage SQL.    |
| H5 : Causalité bidirectionnelle entre niveaux | 1         | Les requêtes SQL (haut niveau) dictent les E/S (bas niveau), et les temps de latence ou l'état du cache (bas niveau) influencent les choix futurs du planificateur de requêtes. |

**Score A1 = 1.00**

**Hésitations / ambiguïtés :** Aucune. L'architecture d'un SGBD moderne est par conception un modèle d'ingénierie modulaire et profondément hiérarchique.

---

## A2 — Capacité de propagation (Invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                                                  |
| ------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | L'acquisition d'un verrou exclusif par une transaction se propage au gestionnaire de concurrence et peut mettre en pause le moteur d'exécution d'autres requêtes.                  |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | Une défaillance matérielle (latence disque) remonte vers le gestionnaire de cache, ralentit l'exécution globale et provoque des délais d'attente (timeouts) au niveau du client.   |
| P3 : Propagation modifie l'état global observable             | 1         | Une transaction modifiant un schéma ou bloquant de multiples enregistrements altère le débit global (throughput) et la charge du système.                                          |
| P4 : Isolation est difficile sans modification structurelle   | 1         | Impossible de découpler le Buffer Manager du Write-Ahead Logging (WAL) ou du gestionnaire de transactions sans briser les garanties ACID.                                          |
| P5 : Couplage fonctionnel non trivial                         | 1         | Le contrôle de concurrence multiversion (MVCC) intègre étroitement les métadonnées des lignes (xmin, xmax) avec le ramasse-miettes (autovacuum) et la visibilité des transactions. |

**Score A2 = 1.00**

**Hésitations / ambiguïtés :** Les SGBD relationnels sont des systèmes fortement couplés pour garantir la fiabilité de la donnée, l'isolation parfaite des modules internes est donc architecturalement impossible par défaut.

---

## A3 — Intégration

| **Sous-critère**                                  | **Score** | **Justification**                                                                                                                                                                   |
| ------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme de coordination explicite existant | 1         | La coordination est assurée par des composants vitaux comme le Lock Manager et le Transaction Manager.                                                                              |
| I2 : Réduction de la variance observable          | 1         | Malgré des milliers d'écritures concurrentes et de requêtes chaotiques, le SGBD présente un état des données toujours cohérent aux utilisateurs grâce au MVCC.                      |
| I3 : Synchronisation multi-niveaux                | 1         | Synchronisation constante entre la mémoire vive (Buffer Pool), le journal de transactions (WAL) et les fichiers de données via les processus de Checkpoint et de Background Writer. |
| I4 : Boucles de rétroaction globales              | 1         | Le planificateur d'exécution utilise les statistiques globales (histogrammes de distribution des données) continuellement mises à jour pour optimiser ses arbres de requêtes.       |
| I5 : Maintien d'un état global cohérent           | 1         | L'objectif premier du système est de faire respecter les contraintes ACID (Atomicité, Cohérence, Isolation, Durabilité), maintenant ainsi une cohérence absolue de l'état.          |

**Score A3 = 1.00**

**Hésitations / ambiguïtés :** Aucune.

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                                                                                                            |
| -------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1 : Attracteur dynamique existant           | 0.5       | Le système possède des états d'équilibre opérationnels (gestion du cache, allocation mémoire), mais ils sont configurés de l'extérieur par des ingénieurs via `postgresql.conf`.                                                                             |
| N2 : Correction active d'écart               | 1         | Récupération active lors des pannes (Crash Recovery via la relecture du WAL), détection et résolution automatiques des deadlocks (interblocages).                                                                                                            |
| N3 : Hiérarchie de priorités régulatoires    | 0.5       | L'ordre des priorités (par ex., écrire dans le WAL avant d'écrire sur le disque) est codé en dur par les développeurs et non généré par le système lui-même.                                                                                                 |
| N4 : Mécanisme interne de stabilisation      | 1         | Les processus d'arrière-plan (Background Writer, Checkpointer) lissent les pics d'E/S (I/O) pour éviter un blocage complet du système lors d'écritures massives.                                                                                             |
| N5 : Résistance aux perturbations prolongées | 0.5       | Le système résiste bien (mise en file d'attente, MVCC limitant le blocage lecteurs/écrivains), mais face à une perturbation prolongée non prévue (saturation complète de l'espace disque), il s'arrête brutalement sans pouvoir adapter sa propre structure. |

**Score A4 = 0.70**

**Hésitations / ambiguïtés :** Distinction de Canguilhem strictement appliquée. Le SGBD maintient une consistance extrême, mais il le fait pour respecter des normes de conception imposées (ACID) par l'ingénierie humaine. Il n'invente ni ne modifie ses propres normes d'équilibre de façon endogène.

---

## A5 — Capacité de révision (Plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                                                                            |
| -------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| R1 : Ajustement paramétrique local                 | 1         | L'Autovacuum se déclenche de manière autonome en fonction des taux de modification des tables, et le système met à jour ses propres statistiques (auto-analyze) pour le planificateur de requêtes.           |
| R2 : Modification durable de configuration interne | 0         | Le système est incapable de modifier de manière autonome des paramètres architecturaux profonds (mémoire partagée allouée, algorithme de hachage). Intervention d'un DBA requise.                            |
| R3 : Reconfiguration de réseau ou de structure     | 0         | Le système ne peut pas partitionner de lui-même des tables trop grandes ou créer de nouveaux index sans commande `CREATE INDEX`/`PARTITION` explicite d'un administrateur.                                   |
| R4 : Modification des mécanismes de régulation     | 0         | Les protocoles de contrôle de concurrence (SSI, Read Committed) et de verrouillage sont fixes ; le SGBD ne peut pas inventer ou basculer dynamiquement son modèle transactionnel interne de son propre chef. |
| R5 : Capacité à produire de nouvelles règles       | 0         | En tant que logiciel codé de manière déterministe, il ne génère aucune nouvelle règle comportementale ou heuristique inédite qui n'aurait pas été programmée par les développeurs.                           |

**Score A5 = 0.20**

**Hésitations / ambiguïtés :** Suivant les instructions critiques, les ajustements endogènes se limitent strictement aux statistiques et au nettoyage (autovacuum). Tout changement structurel requiert un agent externe (DBA), justifiant les zéros pour R2-R5.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 1.00      |
| A2      | 1.00      |
| A3      | 1.00      |
| A4      | 0.70      |
| A5      | 0.20      |
