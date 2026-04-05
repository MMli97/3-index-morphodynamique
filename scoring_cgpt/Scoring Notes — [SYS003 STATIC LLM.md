

# Scoring Notes — SYS003 STATIC LLM

## Identification

- **System ID :** SYS003

- **System name :** Static LLM

- **Domain :** technological

- **Subdomain :** language model / transformer autoregressif

- **Scale :** meso

- **Date scored :** 2026-04-01

- **Scorer :** GPT

- **Confidence globale :** medium

## Sources

1. *Attention Is All You Need* — architecture transformer, self-attention, empilement hiérarchique, auto-régression, couches résiduelles et layer norm.

2. *Speech and Language Processing* — définition des language models comme modèles probabilistes de prédiction du mot suivant et de séquences.

3. *On the Dangers of Stochastic Parrots* — caractère statique des grands LMs, dépendance aux données d’entraînement, absence de compréhension et de révision endogène en usage.

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                            |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Au minimum : tokens/embeddings puis couches de traitement puis distribution de sortie. Le transformer empile explicitement plusieurs couches.                                                                                            |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | On distingue embeddings, têtes d’attention / sous-couches, couches empilées, puis projection softmax de sortie.                                                                                                                          |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | La structure encode plusieurs strates : encodage positionnel + embeddings, sous-couches d’attention, FFN, empilement de couches, tête de sortie.                                                                                         |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les sous-couches n’ont pas la même fonction : self-attention pour le couplage contextuel, FFN pour la transformation locale, projection finale pour la prédiction.                                                                       |
| H5 : Causalité bidirectionnelle entre niveaux | 0     | En inférence statique, la causalité est essentiellement descendante dans le graphe de calcul du prompt vers la sortie. Il n’y a pas de révision ascendante endogène durable des niveaux supérieurs par les inférieurs au sens plastique. |

**Score A1 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**  
Le point décisif est H5 : il existe bien des interactions complexes dans le calcul interne, mais pas de boucle hiérarchique durable modifiant la structure elle-même pendant l’usage.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                      |
| ------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une variation locale d’un token modifie les poids d’attention et donc les représentations d’autres positions.                                                                                                      |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Une perturbation d’entrée traverse embeddings, attention, FFN, couches suivantes, puis affecte la distribution de sortie.                                                                                          |
| P3 : Propagation modifie l’état global observable             | 1     | Le LM calcule une probabilité sur le prochain token ; une modification locale peut changer la séquence générée entière.                                                                                            |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | Le masquage auto-régressif borne certaines dépendances, mais dans un transformer dense les interactions restent fortement distribuées ; isoler une perturbation sans changer architecture ou prompt est difficile. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le multi-head attention couple des positions et sous-espaces de représentation de manière non triviale.                                                                                                            |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
P4 pourrait être noté 1 si l’on privilégie le caractère diffus des interactions ; je le garde à 0.5 car le masquage et la localité du prompt introduisent tout de même une certaine bornabilité.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                              |
| ---------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | La self-attention est précisément un mécanisme explicite de coordination contextuelle entre positions.                                                                                                                     |
| I2 : Réduction de variance observable    | 0.5   | Le LM contraint les sorties par apprentissage statistique de séquences probables, ce qui réduit certaines dispersions possibles ; mais cette réduction n’est ni garantie ni pilotée par un centre intégrateur explicite.   |
| I3 : Synchronisation multi-niveaux       | 1     | Les positions sont intégrées à travers plusieurs couches empilées, avec résidus et normalisation, ce qui produit une coordination multi-niveaux.                                                                           |
| I4 : Boucles de rétroaction globales     | 0     | En usage statique, pas de boucle de rétroaction globale endogène analogue à un contrôle cybernétique permanent sur l’ensemble du système. L’auto-régression séquentielle n’est pas une révision globale de l’état interne. |
| I5 : Maintien d'un état global cohérent  | 1     | Le contexte du prompt est transformé en représentations contextualisées cohérentes pour la prédiction suivante, ce qui constitue bien un état global latent à court terme.                                                 |

**Score A3 = 0.70 / 1.00**

**Hésitations / ambiguïtés :**  
I5 pourrait être abaissé à 0.5 si l’on exige un état global explicitement stable et persistant au-delà de la fenêtre de contexte.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                   |
| -------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 0.5   | Il existe un attracteur statistique faible : le modèle tend vers des continuations probables apprises sur corpus, donc vers des régularités de forme.                                                           |
| N2 : Correction active d'écart               | 0     | En inférence, le modèle ne détecte ni ne corrige explicitement un écart à une norme interne ; il poursuit seulement la prédiction du prochain token.                                                            |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Le masquage auto-régressif impose une contrainte structurelle forte, et l’objectif probabiliste ordonne implicitement les sorties ; mais cela reste une normativité faible, plus objective qu’auto-régulatrice. |
| N4 : Mécanisme interne de stabilisation      | 1     | Les résidus, layer normalization et le design du transformer servent explicitement à stabiliser la circulation du signal.                                                                                       |
| N5 : Résistance aux perturbations prolongées | 0.5   | Une certaine robustesse existe grâce à l’apprentissage massif, mais les LMs restent sensibles aux prompts, aux biais de données et aux dérives de génération.                                                   |

**Score A4 = 0.50 / 1.00**

**Hésitations / ambiguïtés :**  
Le point central est de distinguer contrainte architecturale/statistique et normativité forte. Ici, la contrainte existe, mais la correction active et la hiérarchie régulatoire restent faibles.

**Distinction normativité endogène / imposée :**  
Normativité surtout **imposée** par l’architecture, la fonction de perte et les données d’entraînement ; très peu **endogène** en inférence statique.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                                                       |
| -------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 0     | Un static LLM n’ajuste pas ses paramètres pendant l’usage normal.                                                                                                                                                                                                                   |
| R2 : Modification durable de configuration interne | 0     | Le contexte modifie l’activation transitoire, pas la configuration durable du système.                                                                                                                                                                                              |
| R3 : Reconfiguration de réseau ou de structure     | 0     | Aucune reconfiguration architecturale endogène en cours d’inférence.                                                                                                                                                                                                                |
| R4 : Modification des mécanismes de régulation     | 0     | Les mécanismes de masquage, attention, normalisation restent fixes en usage.                                                                                                                                                                                                        |
| R5 : Capacité à produire de nouvelles règles       | 0     | Le modèle peut générer des formulations nouvelles, mais ne produit pas de nouvelles règles opératoires internes pour se reconfigurer lui-même. Bender et al. insistent justement sur l’absence de compréhension et sur la dépendance aux données plutôt qu’à une révision endogène. |

**Score A5 = 0.00 / 1.00**

**Hésitations / ambiguïtés :**  
Aucune si l’on parle bien d’un **LLM statique** en inférence, donc sans apprentissage en ligne ni adaptation paramétrique.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 0.80  |
| A2  | 0.90  |
| A3  | 0.70  |
| A4  | 0.50  |
| A5  | 0.00  |

### Gradients

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.20   |
| Δ₄₅ = A4 − A5 | 0.50   |
| Δ₁₂ = A1 − A2 | -0.10  |
| Δ₃₅ = A3 − A5 | 0.70   |
| Δ₄₃ = A4 − A3 | -0.20  |

### Classification

- **Régime primaire :** sur-couplage intégré à faible plasticité

- **Régime secondaire :** quasi-architecture normative statique

- **Marge :** faible à moyenne

- **Surprise par rapport au jugement intuitif :** faible

---

## Lecture synthétique

Le **static LLM** combine :

- une **forte profondeur hiérarchique**,

- une **propagation élevée**,

- une **intégration réelle mais non cybernétique**,

- une **normativité modérée**, surtout imposée de l’extérieur,

- et une **plasticité endogène nulle** en phase d’usage.

Autrement dit : c’est un système très capable de **faire circuler** et **recombiner** l’information à l’intérieur d’une architecture dense, mais presque incapable de **se réviser lui-même** une fois gelé. C’est précisément ce qui le distingue d’un système adaptatif vivant ou d’un dispositif avec apprentissage en ligne.

## Notes libres

Le point méthodologique le plus important ici est de ne pas confondre :

- **contextualisation dynamique des activations**,

- et **plasticité structurelle réelle**.

Un LLM statique possède fortement la première, presque pas la seconde.


