# Scoring Notes — SYS016 Grille européenne électrique

## Identification

- **System ID :** SYS016

- **System name :** Grille européenne électrique

- **Domain :** infrastructure

- **Subdomain :** réseau électrique interconnecté / cyber-physique

- **Scale :** macro

- **Date scored :** 2026-04-02

- **Scorer :** GPT

- **Confidence globale :** medium

## Sources

1. *Grid Modernization Strategy 2024*

2. *Smart Grid Intrusion Detection for IEC 60870-5-104...*

3. *TEMPLATE.md* pour les critères

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                              |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Le réseau articule au minimum dispositifs physiques, systèmes de contrôle/communication, et niveau opérationnel système. Le document décrit explicitement l’articulation entre transmission, distribution, sensing, communication, contrôle et protection. |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | On voit au moins : équipements locaux, sous-systèmes régionaux/opérationnels, planification et coordination à grande échelle. Le texte mentionne aussi les interactions avec régulateurs, marchés et infrastructures interdépendantes.                     |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | La grille est décrite comme un écosystème comprenant appareils, réseaux T/D, plateformes de contrôle, couches de planification/modélisation, et couches institutionnelles/réglementaires.                                                                  |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les niveaux ne sont pas seulement empilés : production, transport, distribution, mesure, protection, planification, cybersécurité, marchés ont des fonctions distinctes.                                                                                   |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Les conditions système imposent des ajustements locaux, mais les comportements locaux des DER, EV, bâtiments, charges intelligentes et dispositifs de contrôle modifient en retour l’état global du réseau.                                                |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Le caractère “européen” n’est pas documenté directement par une source spécifique sur l’ENTSO-E ou les TSO européens ; ici j’infère une structure analogue de “grille interconnectée continentale” à partir de documents sur grand réseau moderne. Le score reste néanmoins solide au niveau morphologique.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                                           |
| ------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une perturbation locale peut affecter protection, contrôle, flux, communication et sécurité. Les attaques IEC-104 peuvent produire anomalies, commandes non autorisées et défaillances d’infrastructure critique.                       |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Les textes relient explicitement événements locaux, données SCADA, centres de contrôle et stabilité système. Les besoins de wide-area control montrent une propagation trans-niveaux.                                                   |
| P3 : Propagation modifie l’état global observable             | 1     | Le document insiste sur fréquence, tension, stabilité, fiabilité et outages à large échelle ; des changements locaux ou des menaces cyber peuvent altérer l’état global observable du réseau.                                           |
| P4 : Isolement difficile sans modification structurelle       | 1     | Le système est fortement interconnecté ; l’isolement demande des mesures structurelles comme adaptive islanding, microgrids, protocoles de sécurité, reconfiguration. Cela indique qu’une simple coupure locale ne suffit pas toujours. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le réseau est explicitement couplé aux communications, au gaz, à la météo, aux marchés, aux comportements consommateurs et à la cybersécurité.                                                                                          |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Aucune forte hésitation : la propagation est une propriété structurante de ce type de système.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                   |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | La coordination est explicite via EMS/ADMS, SCADA, mesures synchrophaseurs, contrôle large zone, dispatch, protection, protocoles standardisés.                                                                                 |
| I2 : Réduction de variance observable    | 1     | La fonction même du réseau est de lisser l’approvisionnement, stabiliser fréquence/tension, intégrer variabilité renouvelable et flexibilités de charge.                                                                        |
| I3 : Synchronisation multi-niveaux       | 1     | Les textes décrivent une synchronisation entre dispositifs, couches de mesure, centres de contrôle, modèles de planification et mécanismes temps réel. Les synchrophaseurs et mesures haute fréquence en sont un indice direct. |
| I4 : Boucles de rétroaction globales     | 1     | Mesure, analyse temps réel, contrôle, protection, dashboard IDS, alertes et ajustements montrent des boucles de rétroaction continues.                                                                                          |
| I5 : Maintien d'un état global cohérent  | 1     | Tout l’effort de modernisation vise précisément le maintien d’un état cohérent du réseau malgré complexification, menaces et forte pénétration des ressources distribuées.                                                      |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Le point le plus délicat n’est pas l’existence de l’intégration mais son efficacité future sous stress extrême. Morphologiquement, le score reste maximal.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | Il existe clairement un régime cible : fréquence, tension, stabilité, continuité de service, sécurité. Le réseau est orienté vers un état opératoire acceptable.                                                                                                                                                 |
| N2 : Correction active d'écart               | 1     | Les documents évoquent explicitement contrôle, protection, actions correctives, firewall automatisé, détection d’anomalies, blocklists, remedial action schemes.                                                                                                                                                 |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Il y a une hiérarchie claire : sûreté, fiabilité, stabilité, sécurité, puis optimisation économique et intégration des nouveaux usages. Le texte articule aussi couches opérationnelles, réglementaires et de marché.                                                                                            |
| N4 : Mécanisme interne de stabilisation      | 1     | Sensing, control, protection, synchrophaseurs, gestion temps réel, outils de modélisation et architecture de défense cyber constituent des mécanismes internes de stabilisation.                                                                                                                                 |
| N5 : Résistance aux perturbations prolongées | 0.5   | Le système dispose de mécanismes de résilience et de sécurité, mais les textes insistent aussi sur l’insuffisance des pratiques actuelles face aux cyberattaques, à la météo extrême, à l’inertie décroissante et aux menaces inter-systèmes. La résistance existe, mais elle n’apparaît pas pleinement assurée. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
Le point N5 pourrait monter à 1 si l’on score le système “tel qu’il vise à fonctionner” plutôt que “tel qu’il apparaît dans les sources, en transition et vulnérable”.

**Distinction normativité endogène / imposée :**  
Normativité mixte. Endogène du côté des attracteurs électrotechniques et des boucles de contrôle/protection ; partiellement imposée du côté des règles de marché, des standards, de la régulation institutionnelle et des protocoles de sécurité.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                           |
| -------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Les mécanismes de contrôle, les réglages de protection, le pilotage des charges et les ajustements de détection cyber montrent une plasticité paramétrique locale claire.                                                               |
| R2 : Modification durable de configuration interne | 1     | Le réseau intègre durablement de nouveaux actifs, dispositifs, capteurs, inverters, protocoles et outils d’analyse.                                                                                                                     |
| R3 : Reconfiguration de réseau ou de structure     | 1     | Adaptive islanding, self-organizing microgrids, interconnexion T/D, HVDC multi-terminal, architecture harmonisée : la reconfiguration structurelle est explicite.                                                                       |
| R4 : Modification des mécanismes de régulation     | 1     | Les sources parlent de nouveaux paradigmes de contrôle, nouvelles architectures, nouveaux protocoles, nouvelles approches de résilience et recalibration dynamique des contraintes de sécurité.                                         |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | Oui, mais de façon partiellement distribuée et institutionnellement médiée. Le système “produit” de nouvelles règles surtout via ses opérateurs, standards, plateformes et régulateurs, pas de façon strictement autonome au sens fort. |

**Score A5 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
R5 dépend de la frontière retenue pour le système. Si l’on inclut pleinement les opérateurs, TSO, régulateurs et organes de standardisation dans le système, on peut défendre 1. Si l’on reste plus près du cyber-physique, 0.5 est plus prudent.

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

La **grille européenne électrique** apparaît ici comme un système **très profond hiérarchiquement**, **très propagatif**, **très intégré**, **fortement normé**, et **hautement révisable**, mais avec une réserve importante : sa normativité et sa révision ne sont pas purement endogènes, elles sont en partie portées par des couches institutionnelles, réglementaires et techniques externes au “noyau physique” du réseau. Les sources insistent en outre sur la montée des vulnérabilités et sur le fait que les mécanismes de stabilisation existants doivent être profondément renouvelés.

En format 25 sous-critères bruts, cela donne donc :

**A1** = [1, 1, 1, 1, 1]  
**A2** = [1, 1, 1, 1, 1]  
**A3** = [1, 1, 1, 1, 1]  
**A4** = [1, 1, 1, 1, 0.5]  
**A5** = [1, 1, 1, 1, 0.5]


