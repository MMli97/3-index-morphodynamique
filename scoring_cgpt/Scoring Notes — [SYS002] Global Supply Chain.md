# Scoring Notes — [SYS002] Global Supply Chain

## Identification

- **System ID :** SYS002

- **System name :** Global supply chain

- **Domain :** infrastructure

- **Subdomain :** réseau logistique / socio-technique

- **Scale :** macro

- **Date scored :** 2026-04-01

- **Scorer :** Noé

- **Confidence globale :** medium-high

## Sources

1. *Supply Chain Management Strategy, Planning, and Operation* — définition, niveaux, cycles, coordination, décision stratégique/planning/opérations.

2. *Logistics and Supply Chain Management* — intégration, résilience, visibilité, collaboration, re-engineering.

3. *The Resilient Enterprise* — propagation des perturbations, flexibilité, redondance, reconfiguration, partenariats fournisseurs.

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                            |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Les textes distinguent clairement plusieurs étages : fournisseurs, fabricants, distributeurs, détaillants, clients.                      |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | La chaîne globale ne se réduit pas à une dyade : elle articule au minimum approvisionnement, transformation, distribution, marché final. |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | Les sources décrivent aussi des niveaux décisionnels distincts : design stratégique, planning, opérations.                               |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les fonctions sont fortement différenciées : sourcing, production, stockage, transport, coordination informationnelle, vente.            |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Les flux d’information, de produits et de fonds circulent dans les deux sens, et les décisions aval rétroagissent sur l’amont.           |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Faibles. La profondeur hiérarchique est l’un des traits les plus explicitement documentés.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score | Justification                                                                                                                                        |
| ------------------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Les exemples de disruption montrent qu’un incident local chez un fournisseur ou dans un site affecte achat, production, livraison et service client. |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Le cas Nokia/Ericsson montre qu’un incendie local chez Philips se propage à plusieurs entreprises et niveaux de la chaîne.                           |
| P3 : Propagation modifie l’état global observable             | 1     | Les perturbations peuvent provoquer baisse de production, pertes de ventes, modification de part de marché, arrêts de lignes.                        |
| P4 : Isolement difficile sans modification structurelle       | 1     | Les textes insistent sur le fait que l’isolement exige souvent redondance, fournisseurs alternatifs, re-engineering ou reconfiguration.              |
| P5 : Couplage fonctionnel non trivial                         | 1     | La chaîne globale est explicitement un système de dépendances complexes entre fournisseurs, capacités, délais, stocks, contrats et information.      |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Faibles. La forte propagation fait partie du cœur même des textes sur la vulnérabilité et la résilience.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                          |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| I1 : Mécanisme explicite de coordination | 1     | Les sources mentionnent explicitement collaboration, partage d’information, planification collaborative, alignement des objectifs et pilotage intégré. |
| I2 : Réduction de variance observable    | 1     | La coordination vise explicitement à réduire distorsion d’information, bullwhip effect et variabilité des flux.                                        |
| I3 : Synchronisation multi-niveaux       | 1     | La chaîne globale articule décisions stratégiques, planification et exécution opérationnelle.                                                          |
| I4 : Boucles de rétroaction globales     | 1     | Les données de demande, commandes et niveaux de stock rétroagissent sur approvisionnement et production.                                               |
| I5 : Maintien d'un état global cohérent  | 1     | Toute la logique SCM vise justement à maintenir disponibilité, coût et synchronisation du système entier.                                              |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Le point le plus délicat est que l’intégration réelle varie beaucoup d’une chaîne à l’autre. Ici je score la **forme générale mature** telle qu’elle est théorisée dans les textes, pas une supply chain moyenne empiriquement fragmentée.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                 |
| -------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | La chaîne est orientée vers des états cibles : service, disponibilité, coûts, profit global, continuité.                                                                                                      |
| N2 : Correction active d'écart               | 1     | Réapprovisionnement, replanification, contrats flexibles, alternatives fournisseurs, gestion du risque sont des mécanismes correctifs explicites.                                                             |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Les textes distinguent niveaux stratégique, tactique et opérationnel, avec arbitrages coût/service/résilience.                                                                                                |
| N4 : Mécanisme interne de stabilisation      | 1     | Stocks de sécurité, visibilité, collaboration, supplier development, continuité et resilience teams jouent ce rôle.                                                                                           |
| N5 : Résistance aux perturbations prolongées | 0.5   | La supply chain globale peut résister partiellement grâce à flexibilité et redondance, mais les textes soulignent aussi sa brittleness et sa vulnérabilité importante aux disruptions longues ou systémiques. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
Le vrai point de décision est N5. J’ai mis **0.5** plutôt que **1** car les sources décrivent la résistance comme possible mais non constitutive ni garantie.

**Distinction normativité endogène / imposée :**  
Mixte. Une partie est endogène au système logistique lui-même (stocks, règles de réapprovisionnement, priorités de flux), une autre est imposée par gouvernance managériale, contrats, standards et objectifs économiques.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                            |
| -------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | La chaîne ajuste quantités, dates de livraison, allocation d’inventaire, sourcing local, capacités.                                                                                                                                      |
| R2 : Modification durable de configuration interne | 1     | Les textes décrivent des changements durables de politiques d’inventaire, d’approvisionnement et de plans de continuité.                                                                                                                 |
| R3 : Reconfiguration de réseau ou de structure     | 1     | Re-engineering de chaîne, fournisseurs alternatifs, re-routage, postponement, dual sourcing : tout cela correspond à une reconfiguration structurelle.                                                                                   |
| R4 : Modification des mécanismes de régulation     | 1     | Les mécanismes eux-mêmes peuvent être modifiés : contrats, visibilité, protocoles de risque, supplier development, collaborative planning.                                                                                               |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | Oui, mais de façon médiée par les acteurs organisationnels. La chaîne ne « produit » pas de nouvelles règles de manière autonome comme un système fortement auto-instituant ; elle les élabore via gouvernance, négociation, management. |

**Score A5 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
R5 est le point le plus discutable. J’ai retenu **0.5** pour ne pas sur-attribuer une auto-révision forte à un système dont la plasticité reste dépendante d’acteurs décisionnels.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 1.00  |
| A2  | 1.00  |
| A3  | 1.00  |
| A4  | 0.90  |
| A5  | 0.90  |

### Gradients

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | 0.00   |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | 0.10   |
| Δ₄₃ = A4 − A3 | -0.10  |

### Lecture rapide

Le profil qui sort est celui d’un système :

- **très profondément hiérarchisé**

- **très fortement couplé**

- **très intégré quand il est bien conçu**

- **normatif et piloté**

- **plasticien, mais pas auto-révisable au plus haut degré**

En clair, la **global supply chain** ressemble ici à une forme **hautement organisée et propagative**, avec une forte capacité de coordination, mais dont la robustesse prolongée et l’auto-production de règles restent plus limitées que sa profondeur ou son intégration.

### Classification

- **Régime primaire :** sur-couplage intégré

- **Régime secondaire :** rigidité normative modérée

- **Marge :** faible à moyenne

- **Surprise par rapport au jugement intuitif :** faible

## Notes libres

Le point crucial est méthodologique : si l’on score la **supply chain globale comme idéal-type organisationnel mature**, on obtient presque un plafond sur A1-A3. Si l’on score au contraire une **supply chain empirique moyenne**, souvent fragmentée, asymétrique et conflictuelle, **A3 pourrait baisser à 0.7–0.8** et **A5 à 0.7–0.8**. Ici j’ai choisi la première lecture, car elle est celle qui est le mieux soutenue par les textes fournis, qui décrivent explicitement les mécanismes de coordination, de visibilité, de résilience et de reconfiguration.
