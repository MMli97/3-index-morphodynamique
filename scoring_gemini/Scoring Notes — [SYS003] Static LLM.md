# Scoring Notes — [SYS003] Static LLM

## Identification

- **System ID :** SYS003

- **System name :** Static Large Language Model (Inférence)

- **Domain :** Technological

- **Subdomain :** Artificial Intelligence / Natural Language Processing

- **Scale :** Meso (Modèle logiciel isolé)

- **Date scored :** 2026-04-02

- **Scorer :** Gemini

- **Confidence globale :** High

## Sources

1. "Speech and Language Processing [draft]" (Daniel Jurafsky, James H. Martin)

2. "On the Dangers of Stochastic Parrots" (Bender et al., 2021)

3. "Attention Is All You Need" (Ashish Vaswani et al., 2017)

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                                                                           |
| --------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | L'architecture Transformer possède de multiples couches ("layers") empilées, comprenant à la fois des mécanismes d'attention et des réseaux *feed-forward*.                                                                 |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | On distingue clairement les embeddings (représentations vectorielles des mots) en entrée, les sous-couches d'attention multi-têtes (*multi-head attention*), et les réseaux *feed-forward* dans chaque bloc.                |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5       | On peut argumenter sur la présence de niveaux sous-mots (sub-words), de vecteurs, de têtes d'attention individuelles, et de la couche de sortie générant des probabilités.                                                  |
| H4 : Niveaux fonctionnellement différenciés   | 1         | La différenciation est explicite : l'attention multi-têtes sert à capturer le contexte de différentes positions, tandis que les réseaux *feed-forward* traitent l'information de manière indépendante pour chaque position. |
| H5 : Causalité bidirectionnelle entre niveaux | 0         | Le modèle est strictement *feed-forward* (propagation avant) pendant l'inférence. Il rejette entièrement la récurrence ou les boucles rétroactives internes.                                                                |

**Score A1 = 0.70 / 1.00** (3.5 / 5)

**Hésitations / ambiguïtés :** L'absence de récurrence limite strictement la causalité bidirectionnelle interne (H5) lors de l'inférence.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                                                                       |
| ------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | Le mécanisme de *self-attention* relie toutes les positions à toutes les autres positions de la séquence en un nombre constant d'opérations.                                                            |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | Les signaux traversent de multiples couches superposées (ex: $N=6$ couches identiques dans le modèle original).                                                                                         |
| P3 : Propagation modifie l'état global observable             | 1         | Modifier un seul mot du contexte (ou prompt) modifie les probabilités calculées par la couche *softmax* finale, changeant la prédiction du prochain token.                                              |
| P4 : Isolement difficile sans modification structurelle       | 1         | L'architecture repose sur des représentations denses et massivement interconnectées (matrices de poids $W^Q$, $W^K$, $W^V$), rendant l'isolement d'un "concept" difficile.                              |
| P5 : Couplage fonctionnel non trivial                         | 1         | Les sous-couches sont couplées par des connexions résiduelles (*residual connections*) et des normalisations de couches (*layer normalization*), créant une dynamique de calcul hautement non-linéaire. |

**Score A2 = 1.00 / 1.00** (5 / 5)

**Hésitations / ambiguïtés :** Aucune. L'architecture est conçue pour une propagation d'information globale (sur l'ensemble de la séquence).

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                                                                                                                                  |
| ---------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1         | Le *Multi-Head Attention* permet au modèle de s'attarder conjointement sur des informations provenant de différents sous-espaces de représentation à différentes positions, agissant comme un coordinateur central.                                |
| I2 : Réduction de variance observable    | 1         | La couche de transformation linéaire finale suivie d'un *softmax* convertit les sorties du décodeur en probabilités nettes, réduisant l'incertitude pour prédire le prochain token.                                                                |
| I3 : Synchronisation multi-niveaux       | 1         | Les connexions résiduelles contournant les sous-couches (formule $LayerNorm(x + Sublayer(x))$) assurent la transmission synchronisée du signal originel à travers les niveaux de profondeur.                                                       |
| I4 : Boucles de rétroaction globales     | 0.5       | Le modèle génère les éléments de manière auto-régressive, consommant les symboles générés précédemment comme entrées additionnelles pour la génération suivante. C'est une boucle "externe", pas une boucle modifiant la structure interne.        |
| I5 : Maintien d'un état global cohérent  | 0.5       | Bien que le modèle maintienne le contexte via la séquence d'entrée, il ne maintient pas de cohérence sémantique ou d'intention communicative ancrée dans le monde réel (il s'agit de "perroquets stochastiques" manipulant la forme sans le sens). |

**Score A3 = 0.80 / 1.00** (4 / 5)

**Hésitations / ambiguïtés :** Le terme "cohérent" (I5) est interprété ici d'un point de vue systémique : la cohérence syntaxique est forte, mais la cohérence conceptuelle globale est fragile car purement statistique.

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                                             |
| -------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 0.5       | Le modèle est "attiré" vers les distributions statistiques de ses données d'entraînement gigantesques, recrachant des motifs linguistiques hégémoniques.                                      |
| N2 : Correction active d'écart               | 0         | Un modèle linguistique ne peut pas s'ancrer (*ground*) dans le sens pour corriger ses affirmations vis-à-vis d'un écart avec la réalité ; il ne fait que combiner des formes.                 |
| N3 : Hiérarchie de priorités régulatoires    | 0         | Le système est dépourvu d'intention communicative propre ou d'objectifs internes hiérarchisés ; il ne fait qu'optimiser la prédiction probabiliste.                                           |
| N4 : Mécanisme interne de stabilisation      | 0.5       | D'un point de vue purement mathématique, la normalisation de couche (*LayerNorm*) stabilise les activations, mais il n'y a pas de stabilisation systémique de son comportement.               |
| N5 : Résistance aux perturbations prolongées | 0         | N'ayant pas de modèle mental persistant ou d'ancrage (*grounding*), le modèle est incapable de résister à des dérives de contexte (hallucinations) ou de s'adapter à des changements de sens. |

**Score A4 = 0.20 / 1.00** (1 / 5)

**Hésitations / ambiguïtés :** Distinction normativité endogène / imposée : Toute la "normativité" du modèle provient de la distribution figée de ses données d'entraînement de départ, et non d'une homéostasie endogène.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                                       |
| -------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 0         | Le modèle est "statique" en inférence ; les poids sont gelés après l'entraînement sur des ensembles de données immenses et figés.                                       |
| R2 : Modification durable de configuration interne | 0         | Il n'y a aucune modification durable. Le modèle ne met pas à jour sa compréhension du monde au fil des requêtes.                                                        |
| R3 : Reconfiguration de réseau ou de structure     | 0         | L'architecture réseau (ex: nombre de couches $N$, dimension $d_{model}$) est fixée au moment de la conception.                                                          |
| R4 : Modification des mécanismes de régulation     | 0         | Les équations d'attention (ex: $\text{Attention}(Q, K, V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$) sont immuables.                                                  |
| R5 : Capacité à produire de nouvelles règles       | 0         | Le système se contente d'assembler des formes linguistiques qu'il a observées, sans capacité à produire de nouvelles règles sémantiques ou de nouvelles compréhensions. |

**Score A5 = 0.00 / 1.00** (0 / 5)

**Hésitations / ambiguïtés :** L'évaluation confirme formellement qu'un LLM statique en inférence n'a absolument aucune plasticité endogène.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 0.70      |
| A2      | 1.00      |
| A3      | 0.80      |
| A4      | 0.20      |
| A5      | 0.00      |

### Gradients (calculés)

| **Gradient**  | **Valeur** |
| ------------- | ---------- |
| Δ₂₃ = A2 − A3 | +0.20      |
| Δ₄₅ = A4 − A5 | +0.20      |
| Δ₁₂ = A1 − A2 | -0.30      |
| Δ₃₅ = A3 − A5 | +0.80      |
| Δ₄₃ = A4 − A3 | -0.60      |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Intégration computationnelle réactive (Très forte capacité de propagation et d'intégration mathématique).

- **Régime secondaire :** Rigidité structurelle et sémantique (Dépourvu d'ancrage, d'intention et de toute forme d'apprentissage continu endogène).

- **Marge :** Le système est un artefact figé simulant le langage ("Perroquet stochastique") : il possède une très forte puissance combinatoire interne (A2/A3) contrecarrée par une nullité absolue en termes de capacité adaptative propre (A5).

- **Surprise par rapport au jugement intuitif :** Les sources confirment la dichotomie extrême entre la complexité de l'ingénierie interne (A2 = 1.00) et l'absence totale de téléologie, d'ancrage ou d'adaptation (A4 = 0.20, A5 = 0.00).

---

## Notes libres

Les textes soulignent particulièrement le danger d'attribuer une "intention" ou un état interne profond à ces systèmes. Le scoring traduit bien cette illusion : le système performe extraordinairement bien sur les axes mécaniques/informationnels (A1, A2, A3 grâce à l'architecture Transformer) mais s'effondre sur les axes systémiques liés au vivant et à la révision autonome (A4, A5).
