# Scoring Notes — [SYS021] Thermostat

## Identification

- **System ID :** SYS021

- **System name :** Thermostat (Système classique de régulation thermique par rétroaction)

- **Domain :** technological / infrastructure

- **Subdomain :** Contrôle domotique / Thermodynamique appliquée

- **Scale :** micro / meso

- **Date scored :** [Date du jour]

- **Scorer :** Gemini

- **Confidence globale :** high

## Sources

1. Principes de rétroaction (Feedback Systems - Åström & Murray) : concepts d'atténuation des perturbations, signaux d'erreur, et boucles de contrôle.

2. Théorie Cybernétique (Cybernetics - Wiener) : rétroaction négative (negative feedback) et comportement téléologique (orienté vers un but).

3. Thermodynamique (Advanced Engineering Thermodynamics - Bejan) : flux de chaleur et dynamique du système physique contrôlé.

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                |
| --------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | Il y a une séparation claire entre le niveau "logique/mesure" (le contrôleur) et le niveau "physique" (la dynamique thermique de la pièce).                      |
| H2 : ≥ 3 niveaux causaux distincts            | 0         | Un thermostat classique n'a pas de niveau de méta-contrôle ou d'optimisation supérieur autonome.                                                                 |
| H3 : ≥ 4 niveaux causaux distincts            | 0         | Le système reste fondamentalement à deux niveaux (contrôle et procédé).                                                                                          |
| H4 : Niveaux fonctionnellement différenciés   | 1         | Les composants ont des fonctions strictement distinctes : le capteur (mesure), le comparateur (calcul de l'erreur), et l'actionneur (chauffage/refroidissement). |
| H5 : Causalité bidirectionnelle entre niveaux | 1         | L'état thermique influence le contrôleur (via le capteur), et le contrôleur influence l'état thermique (via l'actionneur).                                       |

**Score A1 = 0.60 / 1.00**

**Hésitations / ambiguïtés :** L'évaluation présume un thermostat classique (On/Off ou PID basique) et non un système en réseau type "Smart Home" (qui pourrait justifier H2).

---

## A2 — Capacité de propagation (invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                        |
| ------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | Une chute de température locale (ex: fenêtre ouverte) modifie l'état du capteur, ce qui déclenche l'allumage du module de chauffage.                     |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | La perturbation physique remonte au niveau de traitement de l'information (signal d'erreur), redescendant en commande physique.                          |
| P3 : Propagation modifie l'état global observable             | 1         | L'activation du chauffage modifie la température de toute la pièce (l'état global du système).                                                           |
| P4 : Isolement difficile sans modification structurelle       | 0.5       | Le capteur et l'actionneur sont physiquement couplés par l'air de la pièce, mais on peut facilement désactiver la boucle fonctionnelle (en l'éteignant). |
| P5 : Couplage fonctionnel non trivial                         | 0         | Le couplage est de nature très triviale (souvent linéaire ou binaire marche/arrêt) défini par une simple équation d'erreur $e(t) = r(t) - y(t)$.         |

**Score A2 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** La "complexité" de la propagation est faible car le mécanisme est explicitement conçu pour être prévisible.

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                        |
| ---------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1         | La boucle de rétroaction négative (negative feedback loop) est l'essence même de ce mécanisme.                                           |
| I2 : Réduction de variance observable    | 1         | C'est le but principal du thermostat : l'atténuation des perturbations pour réduire la variance de la température autour de la consigne. |
| I3 : Synchronisation multi-niveaux       | 0         | Ne s'applique pas réellement à un système aussi plat.                                                                                    |
| I4 : Boucles de rétroaction globales     | 1         | La boucle relie la sortie globale (température de la pièce) à l'entrée globale (consigne).                                               |
| I5 : Maintien d'un état global cohérent  | 1         | Maintient l'homéostasie thermique (l'état stationnaire) du système face à l'environnement.                                               |

**Score A3 = 0.80 / 1.00**

**Hésitations / ambiguïtés :** Le thermostat est l'archétype même de l'intégration par rétroaction.

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                         |
| -------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1         | Le point de consigne (setpoint) agit mathématiquement comme un attracteur stable pour l'état du système.                                                  |
| N2 : Correction active d'écart               | 1         | Le calcul du signal d'erreur et son utilisation par l'actionneur constituent une correction active continue.                                              |
| N3 : Hiérarchie de priorités régulatoires    | 0         | Il n'y a qu'une seule règle/priorité (atteindre la température cible). Pas d'arbitrage complexe.                                                          |
| N4 : Mécanisme interne de stabilisation      | 1         | La rétroaction agit intrinsèquement comme un stabilisateur face aux dérives thermiques naturelles.                                                        |
| N5 : Résistance aux perturbations prolongées | 0.5       | Résiste tant que la capacité calorifique de l'actionneur (la puissance du radiateur) n'est pas dépassée par la perturbation (ex: le grand froid extrême). |

**Score A4 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** **Distinction normativité endogène / imposée :** La normativité est *strictement imposée*. Le "but" (la consigne) est dicté de l'extérieur par l'utilisateur humain, il ne se génère pas lui-même.

---

## A5 — Capacité de révision (plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                  |
| -------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
| R1 : Ajustement paramétrique local                 | 0         | Sauf intervention externe, le système ne modifie pas ses propres gains (ex: composantes P, I, D) face au contexte. |
| R2 : Modification durable de configuration interne | 0         | La structure de la boucle de contrôle est fixe ("hard-wired").                                                     |
| R3 : Reconfiguration de réseau ou de structure     | 0         | Aucune capacité de changer son architecture physique ou de créer de nouvelles boucles.                             |
| R4 : Modification des mécanismes de régulation     | 0         | L'algorithme de contrôle ne mute et n'évolue pas avec le temps.                                                    |
| R5 : Capacité à produire de nouvelles règles       | 0         | Le système est déterministe et strictement cantonné aux règles implémentées par l'ingénieur.                       |

**Score A5 = 0.00 / 1.00**

**Hésitations / ambiguïtés :** Un thermostat "intelligent" (type Nest avec Machine Learning) pourrait marquer 0.5 sur R1 ou R4, mais pour le système standard "thermostat", la plasticité endogène est complètement nulle.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 0.60      |
| A2      | 0.70      |
| A3      | 0.80      |
| A4      | 0.70      |
| A5      | 0.00      |

### Gradients (calculés)

| **Gradient**  | **Valeur** | **Interprétation brève**                                                                                     |
| ------------- | ---------- | ------------------------------------------------------------------------------------------------------------ |
| Δ₂₃ = A2 − A3 | -0.10      | Le système est extrêmement contraint et intégré (A3 élevé), dominant sa capacité de propagation chaotique.   |
| Δ₄₅ = A4 − A5 | 0.70       | Forte régulation (A4) mais rigidité absolue (A5). Typique des machines cybernétiques de première génération. |
| Δ₁₂ = A1 − A2 | -0.10      | Propagation très légèrement supérieure à sa profondeur hiérarchique (système "plat").                        |
| Δ₃₅ = A3 − A5 | 0.80       | Contraste massif entre son comportement hautement intégré et son incapacité d'apprentissage.                 |
| Δ₄₃ = A4 − A3 | -0.10      | La norme (A4) est presque parfaitement traduite en mécanismes d'intégration (A3).                            |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Intégration normative stricte (Mécanique/Automatique).

- **Régime secondaire :** Machine cybernétique rigide (Téléologique imposée).

- **Marge :** Le système est structurellement fermé. Faible résilience face aux situations hors paramètres conceptuels initiaux.

- **Surprise par rapport au jugement intuitif :** Aucune. Le profil `A3, A4 > A1, A2 > A5` est l'empreinte digitale mathématique classique de tout système d'ingénierie à rétroaction de contrôle simple.
