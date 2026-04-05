# Scoring Notes — SYS012 Static LLM

## Identification

- **System ID :** SYS012
- **System name :** Static Large Language Model (Transformer, inference-only)
- **Domain :** technological
- **Subdomain :** artificial intelligence / NLP
- **Scale :** meso
- **Date scored :** 2026-04-01
- **Scorer :** CL
- **Confidence globale :** medium

## Sources

1. Vaswani, A. et al. — "Attention Is All You Need", NeurIPS 2017. Architecture Transformer, propagation forward pass.
2. Jurafsky, D. & Martin, J. — *Speech and Language Processing* (3rd draft). Ch. sur les modèles de langue, N-grams, inference, absence d'apprentissage endogène en déploiement.
3. Bender, E. et al. — "On the Dangers of Stochastic Parrots", FAccT 2021. Limites du LLM en tant que système organisationnel, absence de compréhension, biais encodés statiquement.

---

## A1 — Profondeur hiérarchique

| Sous-critère | Score | Justification |
|---|---|---|
| H1 : ≥ 2 niveaux causaux distincts | 1 | Au minimum deux niveaux clairement distincts : (1) tokens/embeddings en entrée, (2) couches de transformation (attention + FFN). Le passage d'une représentation discrète (token) à une représentation continue (vecteur contextualisé) constitue un saut causal net. [Vaswani §3.1 : encoder = empilement de N=6 couches identiques, chacune avec deux sous-couches.] |
| H2 : ≥ 3 niveaux causaux distincts | 1 | Trois niveaux identifiables : (1) embedding + positional encoding, (2) bloc attention multi-tête (calcul des poids contextuels), (3) réseau feed-forward position-wise (transformation non-linéaire). Chaque niveau opère sur des représentations fonctionnellement différentes. [Vaswani §3.1–3.3] |
| H3 : ≥ 4 niveaux causaux distincts | 0.5 | On peut argumenter un 4e niveau avec la couche de sortie (projection linéaire + softmax → distribution sur le vocabulaire), qui constitue un saut représentationnel vers l'espace des probabilités. Cependant les 6 couches empilées sont structurellement identiques — la profondeur est itérative plutôt que qualitativement différenciée. Hésitation légitime. |
| H4 : Niveaux fonctionnellement différenciés | 1 | Oui : l'embedding encode la position et l'identité lexicale ; l'attention calcule les dépendances contextuelles entre positions ; le FFN effectue une transformation non-linéaire locale ; le softmax produit une distribution de probabilité. Fonctions qualitativement distinctes. [Vaswani §3.2–3.4 ; Bender §5 : les couches manipulent la forme linguistique selon des mécanismes distincts.] |
| H5 : Causalité bidirectionnelle entre niveaux | 0 | En inférence (mode statique), la propagation est strictement unidirectionnelle (forward pass). Il n'y a pas de rétropropagation ni de boucle causale ascendante. Les couches inférieures n'ont aucune influence des couches supérieures. Les connexions résiduelles (skip connections) ne constituent pas une causalité descendante, elles additionnent simplement l'entrée à la sortie dans le sens forward. [Vaswani §3.1 : LayerNorm(x + Sublayer(x)), toujours dans le sens avant.] |

**Score A1 = 0.70 / 1.00**

**Hésitations / ambiguïtés :**
H3 est le point de tension principal. La profondeur architecturale (6 couches) est réelle mais itérative : chaque couche a la même structure. La différenciation fonctionnelle émergente entre couches (certaines têtes d'attention se spécialisent, cf. Vaswani appendix — anaphore, syntaxe) pourrait justifier un score de 1, mais cette spécialisation est émergente et non architecturalement prescrite. Score 0.5 retenu.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère | Score | Justification |
|---|---|---|
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1 | Oui : une modification d'un seul token d'entrée modifie son embedding, ce qui via le mécanisme d'attention affecte les représentations de toutes les autres positions. Le mécanisme d'attention est global par conception. [Vaswani §4 : self-attention connecte toutes les positions en O(1) opérations séquentielles.] |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique | 1 | La perturbation d'un embedding se propage à travers toutes les couches successives (attention → FFN → couche suivante → ... → sortmax). La propagation traverse les trois+ niveaux identifiés en A1. [Vaswani §3.1 : empilage séquentiel des couches.] |
| P3 : Propagation modifie l'état global observable | 1 | Oui : la modification d'un seul token en entrée modifie la distribution de probabilité de sortie (l'état global observable du système). L'attention globale garantit cette propriété. [Vaswani §3.2.3 : chaque position dans le décodeur attend sur toutes les positions de l'encodeur.] |
| P4 : Isolement difficile sans modification structurelle | 1 | Le mécanisme d'attention rend l'isolement d'un composant structurellement impossible sans modifier l'architecture (masquer des positions, supprimer des têtes d'attention). Chaque position est couplée à toutes les autres par construction. [Vaswani §3.2 : attention = weighted sum sur toutes les positions.] |
| P5 : Couplage fonctionnel non trivial | 1 | Le couplage attention est non trivial : il est appris, dépendant du contenu (query-key dot product), multi-tête (8 sous-espaces indépendants), et contextuel. Ce n'est pas un simple passage de signal. [Vaswani §3.2.2 : multi-head attention projette dans des sous-espaces différents.] |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**
Score maximal sans hésitation. Le Transformer est conçu pour maximiser la propagation : l'attention globale est précisément un mécanisme de couplage total. La seule nuance concerne le masquage causal dans le décodeur (positions futures masquées), mais cela ne réduit pas la propagation — il la contraint temporellement.

---

## A3 — Intégration

| Sous-critère | Score | Justification |
|---|---|---|
| I1 : Mécanisme explicite de coordination | 1 | Le mécanisme d'attention est un mécanisme explicite de coordination entre toutes les positions : il calcule des poids d'importance relative et combine les informations de manière pondérée. [Vaswani §3.2 : attention = softmax(QK^T/√dk)V.] |
| I2 : Réduction de variance observable | 0.5 | Partiellement. La Layer Normalization réduit explicitement la variance des activations au sein de chaque couche. Cependant, il n'y a pas de mécanisme global de convergence vers un état unifié — le système produit une distribution de probabilité, pas un consensus. [Vaswani §3.1 : LayerNorm après chaque sous-couche.] |
| I3 : Synchronisation multi-niveaux | 0.5 | Les connexions résiduelles créent un canal d'information entre niveaux qui permet une forme de synchronisation (l'information des couches inférieures reste accessible aux couches supérieures). Mais ce n'est pas une synchronisation dynamique active — c'est un câblage architectural fixe. Pas de feedback, pas d'ajustement mutuel entre niveaux. |
| I4 : Boucles de rétroaction globales | 0 | Aucune boucle de rétroaction en mode inférence. Le flux est strictement feedforward. La sortie (distribution de probabilité) n'influence pas le traitement interne pour un même passage. L'auto-régression (le token généré devient l'entrée suivante) constitue une boucle, mais elle opère entre passes successives, pas au sein d'un même forward pass. [Bender §6.1 : le LLM ne modèle pas son propre état, il produit séquentiellement.] |
| I5 : Maintien d'un état global cohérent | 0.5 | Le système maintient une forme de cohérence via l'attention (chaque position est informée de toutes les autres), produisant des sorties localement cohérentes. Mais il n'y a pas de variable d'état global explicite ni de mécanisme de maintien de cohérence à long terme au-delà de la fenêtre de contexte. La cohérence apparente est un artefact statistique. [Bender §6.1 : la cohérence est perçue par le lecteur humain, pas activement maintenue par le modèle.] |

**Score A3 = 0.50 / 1.00**

**Hésitations / ambiguïtés :**
I2 et I5 sont les points de tension. Le Transformer produit des sorties remarquablement intégrées en apparence, mais les mécanismes sous-jacents sont architecturaux et fixes, pas dynamiques. L'absence totale de boucle de rétroaction (I4=0) est le facteur limitant majeur. L'auto-régression est un candidat pour I4, mais elle opère entre passes, pas au sein du système.

---

## A4 — Normativité

| Sous-critère | Score | Justification |
|---|---|---|
| N1 : Attracteur dynamique existant | 0.5 | Les poids appris définissent un bassin attracteur implicite : pour un prompt donné, le système converge vers une distribution de probabilité spécifique. Cependant, cet attracteur est statique (fixé à l'entraînement) et non dynamiquement maintenu. Le softmax impose une normalisation (somme à 1), qui peut être vue comme un attracteur trivial. |
| N2 : Correction active d'écart | 0 | Aucune correction active. Si l'entrée est bruitée ou aberrante, le système ne « corrige » pas — il propage le bruit à travers l'architecture et produit une sortie correspondante. Il n'y a pas de mécanisme de détection d'écart ni de retour à un état normatif. [Bender §5 : le LLM manipule la forme sans référence au sens ; pas de vérification interne.] |
| N3 : Hiérarchie de priorités régulatoires | 0 | Aucune hiérarchie de priorités explicite ou émergente. Toutes les têtes d'attention et couches sont traitées également. Il n'y a pas de mécanisme qui priorise certains aspects du traitement sur d'autres en réponse à des conditions. [Vaswani : architecture symétrique entre couches.] |
| N4 : Mécanisme interne de stabilisation | 0.5 | La Layer Normalization et les connexions résiduelles stabilisent les gradients et les activations, empêchant l'explosion ou la disparition des signaux. C'est un mécanisme de stabilisation, mais architectural et passif (pas adaptatif). [Vaswani §3.1 : residual connections + layer norm.] |
| N5 : Résistance aux perturbations prolongées | 0 | Aucune résistance aux perturbations prolongées. Le système n'a pas de mémoire inter-inférence : chaque forward pass est indépendant. Un prompt adversarial ou biaisé n'est ni détecté ni contré. [Bender §6.2 : le LLM amplifie les biais de ses données d'entraînement sans mécanisme correctif.] |

**Score A4 = 0.20 / 1.00**

**Hésitations / ambiguïtés :**
N1 et N4 sont les seuls candidats positifs, et dans les deux cas il s'agit de propriétés architecturales passives plutôt que de normativité active. La distinction endogène/imposée est cruciale ici.

**Distinction normativité endogène / imposée :**
La normativité du LLM statique est entièrement **imposée** : les poids sont fixés par l'entraînement (processus exogène), la stabilisation est architecturale (conçue par les ingénieurs), et le système n'a aucune capacité de réviser ses propres normes. La normalisation softmax et la layer normalization sont des contraintes mathématiques imposées, pas des normes que le système se donne. C'est un cas paradigmatique de normativité exogène.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère | Score | Justification |
|---|---|---|
| R1 : Ajustement paramétrique local | 0 | Aucun. En mode inférence (« statique »), les poids sont gelés. Aucun paramètre ne change en réponse à l'entrée ou à l'usage. C'est la définition même du système statique. [Jurafsky, Ch. 4 : les modèles de langue en déploiement n'apprennent pas de nouvelles données.] |
| R2 : Modification durable de configuration interne | 0 | Aucune modification durable. Chaque inférence est indépendante ; le système revient exactement au même état après chaque forward pass. Pas de trace, pas de mémoire, pas d'adaptation. [Bender §5 : les LMs n'effectuent pas de compréhension du langage naturel et ne modifient pas leur état interne.] |
| R3 : Reconfiguration de réseau ou de structure | 0 | Impossible. L'architecture est fixe : nombre de couches, de têtes d'attention, dimensions — tout est déterminé à la conception. Aucune reconfiguration structurelle n'est possible en opération. [Vaswani : architecture N=6 couches, h=8 têtes, dmodel=512, fixés.] |
| R4 : Modification des mécanismes de régulation | 0 | Aucune. Les mécanismes de régulation (layer norm, dropout — ce dernier désactivé en inférence, softmax) sont fixes et non modifiables par le système lui-même. |
| R5 : Capacité à produire de nouvelles règles | 0 | Aucune. Le système ne peut pas créer de nouvelles règles de traitement. Il applique les mêmes transformations apprises à chaque entrée. [Bender §6.1 : le LLM est un « perroquet stochastique » — il recombine des formes linguistiques observées selon des régularités statistiques, sans produire de nouvelles règles.] |

**Score A5 = 0.00 / 1.00**

**Hésitations / ambiguïtés :**
Aucune hésitation. Le score nul est la conséquence directe et non ambiguë de la définition « statique » du système. Un LLM en mode inférence, par construction, ne modifie rien de lui-même. C'est l'axe le plus clair du scoring.

Note : le in-context learning (capacité à utiliser des exemples dans le prompt pour adapter le comportement) pourrait être discuté, mais il ne constitue pas une modification des paramètres ni de la structure — c'est un changement d'entrée, pas un changement du système. La distinction est essentielle.

---

## Synthèse

| Axe | Score |
|-----|-------|
| A1 | 0.70 |
| A2 | 1.00 |
| A3 | 0.50 |
| A4 | 0.20 |
| A5 | 0.00 |

### Gradients (calculés)

| Gradient | Valeur |
|----------|--------|
| Δ₂₃ = A2 − A3 | +0.50 |
| Δ₄₅ = A4 − A5 | +0.20 |
| Δ₁₂ = A1 − A2 | −0.30 |
| Δ₃₅ = A3 − A5 | +0.50 |
| Δ₄₃ = A4 − A3 | −0.30 |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Propagation dominante — le système excelle dans la transmission et le couplage d'information (A2=1.00) mais sans intégration active ni normativité endogène.
- **Régime secondaire :** Hiérarchie structurelle modérée (A1=0.70) avec intégration architecturale passive (A3=0.50).
- **Marge :** Le gradient Δ₂₃ = +0.50 est le plus marqué : forte propagation, intégration modeste. Le gradient Δ₃₅ = +0.50 confirme l'absence totale de plasticité. Le profil est celui d'un système rigide mais fortement couplé.
- **Surprise par rapport au jugement intuitif :** Pas de surprise majeure. Le profil confirme l'intuition que le LLM statique est un système de propagation/couplage puissant mais dépourvu d'agentivité, de normativité endogène et de capacité d'auto-modification. Le score A4 plus bas qu'attendu (0.20) reflète le fait que même la stabilisation est passive et imposée. Le score A3 (0.50) est peut-être le plus discutable — l'attention produit une intégration remarquable, mais sans rétroaction dynamique.

---

## Notes libres

- Le LLM statique est un cas d'étude intéressant car il dissocie fortement propagation (maximale) et plasticité (nulle). C'est un système « câblé pour propager » mais qui ne peut pas se modifier.
- L'auto-régression (génération token par token) crée une illusion de dynamique interne, mais chaque forward pass est complètement indépendant. La « mémoire » est entièrement dans le contexte fourni en entrée, pas dans le système.
- La question du in-context learning mériterait un traitement séparé : on pourrait argumenter qu'il constitue un R1 (ajustement paramétrique local) au niveau fonctionnel, même si les paramètres ne changent pas physiquement. La position retenue ici est conservatrice : pas de modification des paramètres = pas de révision.
- Le terme « stochastic parrot » de Bender et al. capture bien le profil systémique : haute propagation, haute intégration apparente, normativité et plasticité nulles.
- Comparaison utile : un LLM avec fine-tuning continu ou RLHF online aurait un profil radicalement différent sur A4 et A5.
