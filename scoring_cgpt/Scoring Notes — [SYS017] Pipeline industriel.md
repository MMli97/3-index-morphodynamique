# SYS017 — Pipeline industriel,

## Identification

- **System ID :** SYS017

- **System name :** Pipeline industriel

- **Domain :** infrastructure

- **Scale :** macro

- **Date scored :** 2026-04-02

- **Confidence globale :** medium-high

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                   |
| --------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Le système articule clairement des composants locaux et un niveau système : pipe/welds/valves/stations d’un côté, comportement de la ligne et de la livraison de l’autre.                                                       |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | On distingue au minimum : segment/équipement local, station fonctionnelle (pompage/compression), puis réseau ou ligne complète avec points de livraison.                                                                        |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | Les sources décrivent aussi un niveau supérieur de gestion d’intégrité et d’évaluation du risque, au-dessus des équipements/stations/réseau physique.                                                                           |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Route selection, construction, protection anticorrosion, contrôle de station, inspection, réparation, réponse d’urgence et maintenance relèvent de fonctions distinctes.                                                        |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Les états locaux affectent le système global, par exemple la perte d’une station modifie les pressions de livraison; inversement, les set points et contrôles globaux pilotent les unités locales depuis le dispatching office. |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Très peu d’ambiguïté ici. Le pipeline industriel est clairement multi-niveaux.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                     |
| ------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une panne locale de compresseur ou un défaut de segment affecte la pression, la livraison, la maintenance ou la sécurité ailleurs dans le système.                                                                                |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Les perturbations locales remontent au niveau réseau : l’analyse transitoire montre l’effet d’une unité ou station sur les points de livraison.                                                                                   |
| P3 : Propagation modifie l’état global observable             | 1     | Les sources parlent explicitement de baisse de pression aux points de livraison, d’interruption de service, de perte de revenu, de risques sécurité/environnement.                                                                |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | Il existe des moyens d’isoler, inspecter, réparer ou redonder, mais les sources insistent aussi sur la nécessité de spare units, de réparations et parfois de projets d’intégrité planifiés : l’isolement n’est donc pas trivial. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le pipeline couple hydraulique/thermodynamique, matériaux, géotechnique, stations de pompage/compression, contrôle, inspection et contraintes réglementaires.                                                                     |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
Le seul point légèrement discuté est P4, car les pipelines disposent de mécanismes d’isolement et de réparation, mais ceux-ci restent coûteux et structurellement significatifs.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                  |
| ---------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Les contrôleurs de charge, séquences de shutdown, positionnement des valves, inspections et procédures constituent des mécanismes explicites de coordination.                                                  |
| I2 : Réduction de variance observable    | 1     | Le contrôle de débit/pression, les shutdown conditions, les inspections et l’intégrité visent précisément à réduire les écarts opérationnels et le risque de défaillance.                                      |
| I3 : Synchronisation multi-niveaux       | 0.5   | Elle existe entre dispatch, stations, vannes, inspection et maintenance, mais elle repose largement sur procédures et contrôle technique plus que sur une synchronisation organique dense de tous les niveaux. |
| I4 : Boucles de rétroaction globales     | 1     | Les controllers utilisent explicitement le feedback sur le flow rate; l’intégrité management réinjecte inspection et risque dans les décisions de réparation et de maintenance.                                |
| I5 : Maintien d’un état global cohérent  | 1     | L’objectif permanent est de maintenir un état cohérent de livraison, pression, sécurité et intégrité dans les limites de design et d’exploitation.                                                             |

**Score A3 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
I3 n’est pas au maximum car la coordination multi-niveaux est forte mais pas du type hyper-synchronisé qu’on trouverait dans certains systèmes biologiques ou cyber-physiques très serrés.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                           |
| -------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | Le système vise un régime opératoire défini : plages de pression, température, débit, intégrité, sécurité, conformité.                                                  |
| N2 : Correction active d’écart               | 1     | Alarmes, shutdown switches, séquences d’arrêt, inspection, réparation, corrosion monitoring et emergency response corrigent activement les écarts.                      |
| N3 : Hiérarchie de priorités régulatoires    | 1     | La priorité sécurité/intégrité domine clairement : dispositifs de sécurité, pressure relief, response plans, maintenance within design parameters.                      |
| N4 : Mécanisme interne de stabilisation      | 1     | Contrôleurs, monitoring d’intégrité, audits, inspections et maintenance management forment un noyau stabilisateur interne au système pipeline.                          |
| N5 : Résistance aux perturbations prolongées | 1     | L’existence de spare units, de programmes d’intégrité, d’évaluations de risque et d’exercices d’urgence montre une robustesse pensée pour les perturbations prolongées. |

**Score A4 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Faibles. La normativité du pipeline industriel est très marquée.

**Distinction normativité endogène / imposée :**  
Normativité mixte, mais à dominante **imposée-internalisée** : les normes viennent en partie de l’ingénierie, des codes et de la régulation, puis sont encodées dans les dispositifs techniques, procédures et mécanismes de contrôle.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                    |
| -------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Réglage de vannes, set points, contrôle de débit, séquences de démarrage/arrêt : oui, fortement présent.                                                                                                         |
| R2 : Modification durable de configuration interne | 0.5   | Réparations, coating rehabilitation, sleeve repair, cutout repairs modifient durablement certaines parties du système, mais souvent après décision humaine externe.                                              |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | Les sources mentionnent looping, ajout potentiel de stations, expansion de facilities; c’est une capacité réelle mais pas endogène au sens fort.                                                                 |
| R4 : Modification des mécanismes de régulation     | 0.5   | Les changements de critical equipment, les procédures, les programmes d’intégrité et les noncompliances peuvent conduire à réviser les mécanismes de régulation, mais encore une fois via ingénierie/opérateurs. |
| R5 : Capacité à produire de nouvelles règles       | 0     | Le pipeline ne génère pas lui-même de nouvelles règles; les nouvelles règles viennent des ingénieurs, opérateurs, audits, régulateurs ou standards externes.                                                     |

**Score A5 = 0.50 / 1.00**

**Hésitations / ambiguïtés :**  
Le point décisif est celui-ci : le pipeline industriel est révisable, mais sa plasticité est surtout **hétéro-dirigée** plutôt qu’endogène.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 1.00  |
| A2  | 0.90  |
| A3  | 0.90  |
| A4  | 1.00  |
| A5  | 0.50  |

### Gradients

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | 0.50   |
| Δ₁₂ = A1 − A2 | 0.10   |
| Δ₃₅ = A3 − A5 | 0.40   |
| Δ₄₃ = A4 − A3 | 0.10   |

## Lecture rapide

Le **pipeline industriel** apparaît ici comme un système :

- très **hiérarchisé**,

- à **forte propagation** des perturbations,

- très **intégré**,

- fortement **normatif**,

- mais seulement **modérément révisable de manière endogène**.

Autrement dit, c’est un cas très typique de système d’infrastructure **fortement couplé et fortement régulé**, dont la plasticité existe surtout par **intervention organisationnelle et technique externe** plutôt que par auto-révision spontanée.




