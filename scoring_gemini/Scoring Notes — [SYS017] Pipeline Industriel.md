# Scoring Notes — [SYS017] Pipeline industriel

## Identification

- **System ID :** SYS017

- **System name :** Pipeline industriel (Infrastructure physique de transport)

- **Domain :** Infrastructure / Technological

- **Subdomain :** Transport d'hydrocarbures / Énergie

- **Scale :** Macro

- **Date scored :** 2026-04-03

- **Scorer :** IA

- **Confidence globale :** High

## Sources

1. Pipeline design and construction a practical approach, 3rd Edition (M. Mohitpour, H. Golshan, A. Murray)

2. API RP 74 - Recommended Practice for Occupational Safety for Onshore Oil and Gas Production Operation

3. MITEI-annualreport-2025

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                                    |
| --------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | Présence évidente de composants physiques (vannes, pompes) et d'un niveau de contrôle (automates programmables locaux / RTU).                                                        |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | Un troisième niveau est présent via le système de supervision global (SCADA) qui orchestre l'ensemble du réseau.                                                                     |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5       | Un quatrième niveau existe souvent (dispatching de l'entreprise, optimisation économique basée sur la demande), mais il est en partie externe au système purement physique/contrôle. |
| H4 : Niveaux fonctionnellement différenciés   | 1         | Les capteurs acquièrent la donnée, les automates exécutent la logique locale, et le SCADA gère la vue d'ensemble et l'équilibrage du réseau.                                         |
| H5 : Causalité bidirectionnelle entre niveaux | 1         | Le contrôle redescend du SCADA vers les vannes/pompes (top-down), tandis que les capteurs de pression/débit font remonter l'état du système (bottom-up).                             |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** L'attribution d'un quatrième niveau (H3) dépend de la limite exacte fixée entre le système de contrôle industriel (OT) et le système d'information de gestion (IT). Nous accordons 0.5 pour refléter cette frontière.

---

## A2 — Capacité de propagation

| **Sous-critère**                                  | **Score** | **Justification**                                                                                                                                                                                         |
| ------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module | 1         | Une chute de pression, une fuite ou un blocage modifie immédiatement l'hydraulique et affecte les stations de pompage en aval ou en amont.                                                                |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique | 1         | Un événement physique (ex. rupture de conduite) génère des alarmes remontant au système SCADA et déclenchant des procédures d'urgence (API RP 74).                                                        |
| P3 : Propagation modifie l'état global observable | 1         | Une défaillance majeure d'un tronçon peut nécessiter l'arrêt complet de la ligne ou réduire drastiquement la capacité de livraison globale.                                                               |
| P4 : Isolation difficile sans modif structurelle  | 0.5       | Les pipelines sont conçus avec des vannes de sectionnement (block valves) pour isoler les segments, mais les ondes de choc hydraulique (coup de bélier) peuvent se propager rapidement avant l'isolement. |
| P5 : Couplage fonctionnel non trivial             | 1         | La dynamique des fluides crée un couplage complexe entre la température, la pression, la viscosité et la topographie tout au long du pipeline.                                                            |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** Le P4 est évalué à 0.5 car bien que l'isolement soit une fonctionnalité clé de sécurité intégrée dès la conception (API RP 74), la nature fluide du contenu rend la propagation d'anomalies de pression inévitable à court terme.

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                                     |
| ---------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme de coordination explicite | 1         | Le système SCADA est le mécanisme central et explicite de coordination du pipeline.                                                                   |
| I2 : Réduction de variance observable    | 1         | Les régulateurs de pression lissent les variations pour maintenir un flux régulier (steady-state) conformément aux paramètres de design.              |
| I3 : Synchronisation multi-niveaux       | 1         | Les stations de compression/pompage sont synchronisées en cascade pour maintenir l'équilibre hydraulique sur de longues distances.                    |
| I4 : Boucles de rétroaction globales     | 1         | L'ajustement de l'injection en amont est régulé en temps réel par les données de livraison en aval (gestion du "line pack").                          |
| I5 : Maintien d'un état global cohérent  | 1         | Le système maintient la conservation de la masse globale de fluide tout en respectant les limites de pression de service maximales autorisées (MAOP). |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune. Le pipeline en fonctionnement nominal est un système hautement intégré et coordonné.

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                                  |
| -------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1         | Le système tend vers un régime d'écoulement stationnaire (débit et pression cibles).                                                                                               |
| N2 : Correction active d'écart               | 1         | Les boucles PID locales ajustent continuellement l'ouverture des vannes ou la vitesse des pompes pour contrer les déviations de pression.                                          |
| N3 : Hiérarchie de priorités régulatoires    | 1         | Les protocoles de sécurité prévalent systématiquement sur l'efficacité (ex: arrêt d'urgence ou soupape de sûreté prioritaire, selon API RP 74).                                    |
| N4 : Mécanisme interne de stabilisation      | 1         | La conception inclut des mécanismes matériels spécifiques tels que des réservoirs d'expansion et des soupapes de décharge (surge relief valves).                                   |
| N5 : Résistance aux perturbations prolongées | 0.5       | Le système peut tolérer certaines perturbations grâce à son "line pack", mais finit par s'arrêter (shutdown) face à une contrainte prolongée, ne pouvant s'y adapter indéfiniment. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** N5 est évalué à 0.5 car le système physique est rigide. Il résiste aux variations opérationnelles à court terme (tampon de volume) mais n'a pas la résilience d'un système biologique face à une perturbation environnementale prolongée.

---

## A5 — Capacité de révision (Plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                               |
| -------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1         | Ajustement paramétrique possible (ex: réglage des consignes de pression via SCADA). C'est la seule modification authentiquement endogène.       |
| R2 : Modification durable de configuration interne | 0         | Le pipeline est en acier enterré. Il ne peut pas modifier sa propre structure. Les modifications exigent des travaux de construction physiques. |
| R3 : Reconfiguration de réseau ou de structure     | 0         | Nécessite des opérations de "looping" (ajout de tronçons parallèles) ou de déviation pilotées par des ingénieurs humains externes au système.   |
| R4 : Modification des mécanismes de régulation     | 0         | Les algorithmes de contrôle et la logique de sécurité (safety logic) sont codés en dur dans les automates et le SCADA.                          |
| R5 : Capacité à produire de nouvelles règles       | 0         | Le système suit un programme établi et n'a aucune capacité autonome à générer de nouvelles règles d'exploitation.                               |

**Score A5 = 0.20 / 1.00**

**Hésitations / ambiguïtés :** Conformément aux instructions critiques, les limitations physiques (conduite en acier enterrée) et logicielles (règles de contrôle déterministes et non auto-modifiables) plafonnent ce score à l'ajustement purement paramétrique.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 0.90      |
| A2      | 0.90      |
| A3      | 1.00      |
| A4      | 0.90      |
| A5      | 0.20      |
