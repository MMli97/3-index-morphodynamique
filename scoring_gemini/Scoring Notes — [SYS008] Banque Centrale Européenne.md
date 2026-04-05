

# Scoring Notes — [SYS008] Banque Centrale Européenne

## Identification

- **System ID :** SYS008

- **System name :** Banque Centrale Européenne (et Eurosystème)

- **Domain :** institutionnel / économique

- **Subdomain :** Politique monétaire

- **Scale :** macro

- **Date scored :** 2026-04-01

- **Scorer :** Gemini

- **Confidence globale :** high

## Sources

1. *Whatever it takes. Mario Draghi in parole sue* (J. Randow, A. Speciale)

2. *Economics of Monetary Union* (Paul De Grauwe)

3. *The Birth of the Euro* (Otmar Issing)

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                                           |
| --------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | La structure de l'Eurosystème distingue clairement le niveau décisionnel (Conseil des gouverneurs de la BCE) et le niveau opérationnel (Banques Centrales Nationales).                      |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | La politique monétaire passe de la BCE aux BCN, puis se transmet au système bancaire commercial intermédiaire.                                                                              |
| H3 : ≥ 4 niveaux causaux distincts            | 1         | La chaîne causale s'étend jusqu'à l'économie réelle, affectant in fine les ménages et les entreprises via l'octroi de crédit.                                                               |
| H4 : Niveaux fonctionnellement différenciés   | 1         | Les fonctions sont séparées : la BCE conçoit la stratégie monétaire, les BCN exécutent les opérations de liquidité, et les banques commerciales distribuent le crédit.                      |
| H5 : Causalité bidirectionnelle entre niveaux | 1         | Les décisions (taux) descendent vers l'économie (top-down), mais la stratégie de la BCE est ajustée en fonction de la remontée des données macroéconomiques et des chocs réels (bottom-up). |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**

Aucune. La profondeur hiérarchique et la différenciation fonctionnelle sont explicitement inscrites dans l'architecture voulue par les pères fondateurs de la monnaie unique.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                                                                  |
| ------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | Les déséquilibres de liquidité dans un pays affectent rapidement les autres modules via le système de règlement interbancaire TARGET2.                                                             |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | Les modifications des taux directeurs se propagent directement aux taux d'intérêt de détail appliqués par les banques commerciales.                                                                |
| P3 : Propagation modifie l'état global observable             | 1         | De simples annonces verbales, comme le célèbre "Whatever it takes" de Mario Draghi, ont suffi à modifier drastiquement le rendement des obligations souveraines globales et à sauver la zone euro. |
| P4 : Isolement difficile sans modification structurelle       | 1         | La politique monétaire est unique ("one size fits all") ; aucun pays membre ne peut s'en isoler sans sortir de l'Union monétaire.                                                                  |
| P5 : Couplage fonctionnel non trivial                         | 1         | La transmission de la politique monétaire s'opère par des canaux complexes (taux, crédit, anticipations) soumis à de fortes frictions en temps de crise.                                           |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**

Le système est conçu précisément pour assurer une propagation maximale des décisions monétaires au sein de la zone euro.

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                                                     |
| ---------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1         | Le Conseil des gouverneurs de la BCE agit comme l'organe central de coordination où toutes les BCN sont représentées.                                                 |
| I2 : Réduction de variance observable    | 0.5       | La BCE peine parfois à réduire la variance : l'Union monétaire est sujette à des chocs asymétriques difficiles à lisser en l'absence d'une union budgétaire complète. |
| I3 : Synchronisation multi-niveaux       | 1         | La monnaie unique synchronise par nature les agrégats monétaires et les taux de refinancement à travers tous les pays membres.                                        |
| I4 : Boucles de rétroaction globales     | 1         | La "stratégie à deux piliers" de la BCE (analyse économique et monétaire) organise l'absorption de l'information pour piloter le système.                             |
| I5 : Maintien d'un état global cohérent  | 0.5       | Le système a montré sa fragilité face aux risques de fragmentation de la zone euro lors de la crise des dettes souveraines.                                           |

**Score A3 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**

La nature "incomplète" de l'Union économique et monétaire (UEM) limite l'intégration systémique parfaite, justifiant les notes partielles sur la réduction de variance et la cohérence globale.

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                              |
| -------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1 : Attracteur dynamique existant           | 1         | L'objectif de maintien de l'inflation à un niveau proche de, mais inférieur à 2% à moyen terme, constitue l'attracteur central du système.                                     |
| N2 : Correction active d'écart               | 1         | Le pilotage des taux d'intérêt et l'expansion du bilan (Quantitative Easing) visent explicitement à ramener l'inflation vers sa cible.                                         |
| N3 : Hiérarchie de priorités régulatoires    | 1         | Le mandat de stabilité des prix a une priorité absolue (lexical ordering) sur les autres objectifs économiques de l'Union.                                                     |
| N4 : Mécanisme interne de stabilisation      | 1         | La mise en place de l'OMT (Opérations Monétaires sur Titres) a servi de mécanisme de stabilisation ultime (prêteur en dernier ressort de facto) face à la panique des marchés. |
| N5 : Résistance aux perturbations prolongées | 1         | Le système a survécu à la crise financière mondiale puis à la crise existentielle de la zone euro grâce à une gestion agressive.                                               |

**Score A4 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**

Aucune. C'est un système hautement normatif, fondé sur des traités rigides, mais capable de défendre farouchement son attracteur (la survie de l'Euro).

---

## A5 — Capacité de révision (plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                          |
| -------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1         | Modification constante et routinière des taux directeurs selon la conjoncture.                                                                             |
| R2 : Modification durable de configuration interne | 1         | Le basculement vers des politiques non conventionnelles (achats d'actifs massifs) a durablement modifié la taille du bilan et le rôle de la BCE.           |
| R3 : Reconfiguration de réseau ou de structure     | 0.5       | Le réseau s'étend (élargissement de la zone euro), mais cette reconfiguration dépend de décisions politiques des États, pas seulement de la BCE.           |
| R4 : Modification des mécanismes de régulation     | 1         | La BCE a su inventer de nouveaux mécanismes (Forward Guidance, LTRO, OMT) sous la présidence de M. Draghi pour contourner la limite de la baisse des taux. |
| R5 : Capacité à produire de nouvelles règles       | 1         | En réponse aux crises, le système a favorisé la création de l'Union Bancaire, attribuant à la BCE de nouveaux pouvoirs de supervision (SSM).               |

**Score A5 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**

Une légère réserve sur R3 car l'expansion territoriale du système (nouveaux pays) est une donnée exogène, même si la BCE s'adapte très bien institutionnellement à cette intégration.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 1.00      |
| A2      | 1.00      |
| A3      | 0.80      |
| A4      | 1.00      |
| A5      | 0.90      |

### Gradients (calculés)

| **Gradient**  | **Valeur** |
| ------------- | ---------- |
| Δ₂₃ = A2 − A3 | 0.20       |
| Δ₄₅ = A4 − A5 | 0.10       |
| Δ₁₂ = A1 − A2 | 0.00       |
| Δ₃₅ = A3 − A5 | -0.10      |
| Δ₄₃ = A4 − A3 | 0.20       |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système régulatif fort et réseau de propagation de haute intensité.

- **Régime secondaire :** Structure macro-institutionnelle contrainte par un environnement asymétrique.

- **Marge :** Le système de l'Euro souffre d'un déficit d'intégration endémique (Δ₂₃ positif) dû à la centralisation monétaire juxtaposée à une décentralisation fiscale.

- **Surprise par rapport au jugement intuitif :** La très grande capacité d'innovation de l'institution (A5 élevé), portée par des figures de leadership, contraste fortement avec les statuts doctrinaux très stricts de ses origines.

---

## Notes libres

Les textes soulignent une tension permanente : Issing décrit l'architecture parfaite et normative (A1, A4), tandis que De Grauwe pointe les fragilités d'intégration et les chocs asymétriques (qui pénalisent A3). Finalement, Draghi représente la plasticité (A5) et la capacité de résistance du système, capable d'inventer des outils de propagation (A2) hors norme pour préserver la monnaie unique ("Whatever it takes").
