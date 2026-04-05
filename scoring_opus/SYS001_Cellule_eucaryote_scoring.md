# Scoring Notes — [SYS001] Cellule eucaryote

## Identification

- **System ID :** SYS001
- **System name :** Eukaryotic cell (cellule eucaryote générique)
- **Domain :** biological
- **Subdomain :** cell biology
- **Scale :** micro
- **Date scored :** 2026-03-30
- **Scorer :** CL (assisté par sources)
- **Confidence globale :** high

## Sources

1. Alberts, B. et al. — *Molecular Biology of the Cell* (Garland, 7th ed.). Cell organization, signal transduction, gene regulation.
2. Lodish, H. et al. — *Molecular Cell Biology* (Freeman, 9th ed.). Organelle function, metabolic integration, homeostasis.
3. Bray, D. — *Wetware: A Computer in Every Living Cell* (Yale UP, 2009). Cellular computation, feedback, integration.

---

## A1 — Profondeur hiérarchique

| Sous-critère | Score | Justification |
|---|---|---|
| H1 : ≥ 2 niveaux causaux distincts | 1 | Au minimum : (1) molécules individuelles (protéines, métabolites) et (2) organelles fonctionnels (noyau, mitochondries, RE). Les réactions moléculaires causent les propriétés des organelles. [Alberts ch. 12–15 ; Lodish ch. 12–14] |
| H2 : ≥ 3 niveaux causaux distincts | 1 | Trois niveaux nets : (1) modifications post-traductionnelles / métabolites, (2) complexes macromoléculaires et organelles, (3) état cellulaire global (cycle cellulaire, phénotype). Bray insiste sur le passage molécules → circuits → comportement cellulaire. [Bray ch. 4–7 ; Alberts ch. 15, 17] |
| H3 : ≥ 4 niveaux causaux distincts | 1 | Quatre niveaux identifiables : (1) métabolites/ions, (2) protéines/enzymes individuelles, (3) voies de signalisation / complexes (cascades MAPK, protéasome, spliceosomes), (4) état global (cycle cellulaire, différenciation, apoptose). Lodish ch. 16 et 19 documentent explicitement ces couches causales emboîtées. |
| H4 : Niveaux fonctionnellement différenciés | 1 | Chaque niveau remplit des fonctions qualitativement distinctes : le niveau moléculaire = catalyse et liaison ; le niveau des voies = transduction et amplification du signal ; le niveau des organelles = compartimentation et spécialisation biochimique ; le niveau cellulaire global = décision (division, différenciation, mort). Les compartiments membranaires (RE, Golgi, lysosomes, mitochondries, noyau) créent des environnements chimiques distincts. [Alberts ch. 12–13 ; Lodish ch. 14] |
| H5 : Causalité bidirectionnelle entre niveaux | 1 | Omniprésente. Le niveau global (ex. : phase du cycle cellulaire) contrôle les voies de signalisation via les CDK/cyclines, tandis que les voies de signalisation (ex. : dommages ADN → p53) modifient l'état global. La transcription (noyau) contrôle la composition du cytoplasme, mais l'état du cytoplasme (calcium, redox) rétroagit sur la transcription. Bray décrit explicitement cette bidirectionnalité comme base de la computation cellulaire. [Bray ch. 6–8 ; Alberts ch. 15, 17 ; Lodish ch. 19] |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune hésitation majeure. La cellule eucaryote est probablement le système biologique micro qui exhibe la plus grande profondeur hiérarchique documentée. La seule question est le grain de H3 : on pourrait argumenter 5 niveaux (ajout du niveau chromatinien/épigénétique), mais 4 est conservateur et suffisant.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère | Score | Justification |
|---|---|---|
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1 | Une mutation dans un gène de signalisation (ex. : Ras) affecte la cascade MAPK, qui affecte la transcription, le métabolisme, et le cycle cellulaire — modules fonctionnels distincts. Le cross-talk entre voies est extensivement documenté. [Lodish ch. 16 ; Alberts ch. 15] |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique | 1 | Exemple canonique : un signal extracellulaire (ligand) active un récepteur (niveau moléculaire) → cascade de kinases (niveau des voies) → modification de la transcription (niveau nucléaire) → changement du phénotype cellulaire (niveau global). Les cascades MAPK traversent explicitement 3–4 niveaux. [Lodish ch. 16.2 ; Bray ch. 5–6] |
| P3 : Propagation modifie l'état global observable | 1 | Un seul signal (ex. : facteur de croissance, dommage ADN) peut déclencher la division cellulaire, l'arrêt du cycle, la différenciation ou l'apoptose — tous des changements d'état global. Alberts : « The cell can adapt and continue to function during starvation or disease ». L'apoptose comme changement d'état global irréversible est un cas paradigmatique. [Lodish ch. 19, 22 ; Alberts ch. 17–18] |
| P4 : Isolement difficile sans modification structurelle | 1 | Le partage de seconds messagers (Ca²⁺, cAMP, IP₃), de pools métaboliques communs et de facteurs de transcription pléiotropes rend l'isolement des voies extrêmement difficile. Bray insiste : les molécules diffusent librement et toute enzyme partage un « pool commun de molécules ». Les scaffold proteins existent précisément parce que l'isolement naturel est faible. [Bray ch. 7 ; Alberts ch. 15 (scaffold proteins et cross-talk)] |
| P5 : Couplage fonctionnel non trivial | 1 | Le couplage n'est pas simple diffusion linéaire mais implique des amplifications non-linéaires (cascades de kinases), des effets de seuil (réponse all-or-none des MAP kinases dans les oocytes), des boucles de rétroaction positive et négative, et des effets combinatoires. Alberts documente la réponse tout-ou-rien des oocytes au progestérone via MAPK. [Alberts ch. 15 fig. 15–20 ; Bray ch. 4–5 ; Lodish ch. 16] |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune. La propagation intra-cellulaire est un des domaines les plus documentés de la biologie moléculaire. Les trois sources convergent.

---

## A3 — Intégration

| Sous-critère | Score | Justification |
|---|---|---|
| I1 : Mécanisme explicite de coordination | 1 | Multiples mécanismes explicites : seconds messagers globaux (Ca²⁺, cAMP), facteurs de transcription maîtres, complexes CDK/cycline pour le cycle cellulaire, système ubiquitine-protéasome pour la dégradation coordonnée. Bray compare les protéines régulatrices à des « conducteurs d'orchestre » synchronisant l'expression de gènes. [Bray ch. 8 ; Lodish ch. 19 ; Alberts ch. 17] |
| I2 : Réduction de variance observable | 1 | L'homéostasie cellulaire est la définition même de la réduction de variance : pH intracellulaire maintenu (~7.2), concentration de Ca²⁺ cytosolique (∼100 nM vs 1 mM extracellulaire), balance redox, ratio ATP/ADP. Alberts : « the metabolic balance of a cell is amazingly stable. Whenever the balance is perturbed, the cell reacts so as to restore the initial state ». [Alberts ch. 2 ; Lodish ch. 12, 21] |
| I3 : Synchronisation multi-niveaux | 1 | Le cycle cellulaire synchronise simultanément : réplication de l'ADN (niveau moléculaire), dynamique du cytosquelette (niveau structural), check-points (niveau des voies de signalisation), et division physique (niveau cellulaire global). Les checkpoints ADN-damage couplent l'état du génome au cycle global. [Lodish ch. 19 ; Alberts ch. 17] |
| I4 : Boucles de rétroaction globales | 1 | Omniprésentes et documentées à tous les niveaux. Exemples : rétroaction négative globale du p53 sur le cycle via MDM2 ; rétroaction positive dans la transition G1→S (CDK positive feedback loop) ; oscillateur circadien cellulaire ; boucle Unfolded Protein Response (UPR) coordonnant RE, noyau et traduction. Bray cite Brandman & Meyer (2008) sur les « feedback loops that shape cellular signals in space and time ». [Lodish ch. 19.3, 21 ; Alberts ch. 17 ; Bray références] |
| I5 : Maintien d'un état global cohérent | 1 | La cellule maintient un phénotype stable et identifiable (type cellulaire) malgré le turnover constant de ses composants (demi-vie protéique typique : heures à jours). L'identité cellulaire (muscle, neurone, épithélium) est maintenue par des réseaux de facteurs de transcription en rétroaction positive mutuelle. Bray : les cellules « deviennent des spécialistes dédiés » avec un « set de protéines de plus en plus restreint ». L'état cancéreux illustre la rupture de cette cohérence. [Bray ch. 8 ; Alberts ch. 7, 22 ; Lodish ch. 22] |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune hésitation. La cellule eucaryote est un cas d'école d'intégration biologique. Tous les sous-critères sont saturés.

---

## A4 — Normativité

| Sous-critère | Score | Justification |
|---|---|---|
| N1 : Attracteur dynamique existant | 1 | Les types cellulaires correspondent à des attracteurs dans l'espace des états d'expression génique, concept formalisé par Kauffman et confirmé empiriquement. Bray : « Specific genes become expressed in subpopulations of cells [...] They become locked into mutually active pathways by positive feedback mechanisms ». Les états stables du cycle cellulaire (G1, S, G2, M) sont des attracteurs dynamiques. [Bray ch. 8 ; Alberts ch. 7 ; Lodish ch. 19] |
| N2 : Correction active d'écart | 1 | La cellule corrige activement les déviations : pompes ioniques maintenant les gradients, chaperones refoldant les protéines mal repliées, systèmes de réparation de l'ADN (MMR, BER, NER, HR), UPR déclenchée par les protéines mal repliées dans le RE, autophagie éliminant les organelles endommagées. Alberts : « the cell reacts so as to restore the initial state ». [Alberts ch. 5, 17 ; Lodish ch. 19.7, 21, 22] |
| N3 : Hiérarchie de priorités régulatoires | 1 | Hiérarchie claire : la survie prime sur la prolifération (checkpoints arrêtant le cycle en cas de dommage ADN), la prolifération prime sur la différenciation (signaux mitogènes vs différenciation), l'intégrité génomique prime sur la continuité cellulaire (apoptose déclenchée par dommages irréparables). Le système p53 incarne cette hiérarchie : réparation → arrêt du cycle → apoptose, selon la gravité. [Lodish ch. 19.7, 22.4 ; Alberts ch. 17, 20] |
| N4 : Mécanisme interne de stabilisation | 1 | Multiples mécanismes intrinsèques : homéostasie du Ca²⁺ (pompes SERCA, canaux), tampon pH (bicarbonate, protéines), régulation osmotique (aquaporines, transporteurs), contrôle du potentiel redox (glutathion, thiorédoxine), protéostasie (chaperones HSP, protéasome). Ces mécanismes sont constitutifs, non contingents. [Alberts ch. 11, 12 ; Lodish ch. 12, 21] |
| N5 : Résistance aux perturbations prolongées | 1 | La cellule survit à des stress prolongés : privation nutritive (autophagie), hypoxie (switch métabolique via HIF), stress thermique (heat-shock response), stress du RE (UPR prolongé). Alberts : « The cell can adapt and continue to function during starvation or disease. Mutations of many kinds can damage or even eliminate particular reaction pathways, and yet — provided that certain minimum requirements are met — the cell survives ». Lodish ch. 21 documente les réponses aux changements environnementaux prolongés. [Alberts ch. 2 ; Lodish ch. 21 ; Bray ch. 6] |

**Score A4 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune.

**Distinction normativité endogène / imposée :** La normativité de la cellule eucaryote est **intégralement endogène**. Toutes les normes (set-points homéostatiques, checkpoints du cycle, seuils d'apoptose) sont encodées dans le génome et les circuits protéiques de la cellule elle-même. Aucune norme n'est imposée de l'extérieur par un opérateur ou un designer. Même les signaux extracellulaires (hormones, facteurs de croissance) sont interprétés et filtrés par la machinerie interne de la cellule — la « norme » est endogène, le signal est exogène. Cas paradigmatique de normativité biologique au sens de Canguilhem.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère | Score | Justification |
|---|---|---|
| R1 : Ajustement paramétrique local | 1 | Omniprésent : ajustement des taux enzymatiques par régulation allostérique, modification post-traductionnelle (phosphorylation, acétylation, ubiquitination), modulation de la dégradation protéique. La régulation allostérique est le mécanisme d'ajustement paramétrique le plus fondamental du vivant. [Alberts ch. 3, 15 ; Lodish ch. 3.4 ; Bray ch. 4] |
| R2 : Modification durable de configuration interne | 1 | La différenciation cellulaire est une modification durable de la configuration : changement stable du profil d'expression génique via modifications épigénétiques (méthylation de l'ADN, modifications des histones). Ces modifications persistent à travers les divisions cellulaires. Alberts : « epigenetic inheritance [...] superimposed on the DNA-based genetic inheritance ». [Alberts ch. 4, 7 ; Lodish ch. 7, 9 ; Bray ch. 8] |
| R3 : Reconfiguration de réseau ou de structure | 1 | Exemples majeurs : remodelage du cytosquelette (polymérisation/dépolymérisation des microtubules et de l'actine), dynamique mitochondriale (fusion/fission), biogenèse d'organelles, remodelage de la chromatine à grande échelle. Lors de la mitose, l'architecture cellulaire entière est reconfigurée. La reprogrammation cellulaire (iPSCs) démontre que même le réseau de régulation génique peut être reconfiguré. Alberts : « Reprogramming involves a massive upheaval of the gene control system ». [Alberts ch. 16, 22 ; Lodish ch. 12 (dynamique mitochondriale), 18 (cytosquelette)] |
| R4 : Modification des mécanismes de régulation | 0.5 | La cellule peut modifier certains de ses mécanismes de régulation : le remodelage chromatinien change quels gènes sont accessibles aux facteurs de transcription, modifiant ainsi les règles de régulation elles-mêmes. L'alternative splicing permet de changer le répertoire de protéines régulatrices. Cependant, ces modifications restent dans le cadre du code génétique existant — la cellule ne crée pas de nouveaux principes régulateurs ex nihilo au sein d'une seule génération cellulaire. Bray note que les circuits de régulation eucaryotes sont « promiscuous and overlapping » mais leur remodelage est contraint. [Bray ch. 8 ; Alberts ch. 7 ; Lodish ch. 9] |
| R5 : Capacité à produire de nouvelles règles | 0.5 | La cellule isolée ne produit pas véritablement de nouvelles règles au sens fort. Cependant : (1) les mutations somatiques et les réarrangements génomiques (ex. : recombinaison V(D)J dans les lymphocytes) créent de nouvelles séquences régulatrices ; (2) l'insertion d'éléments transposables peut créer de nouveaux enhancers ; (3) la sélection clonale dans le système immunitaire est un processus de génération de « nouvelles règles » de reconnaissance. Score 0.5 car ces mécanismes sont limités et souvent stochastiques plutôt que dirigés — la cellule n'innove pas de manière programmatique, mais elle dispose de mécanismes qui peuvent produire de la nouveauté régulière. [Alberts ch. 5 (mutation et réparation), 24 (système immunitaire) ; Lodish ch. 22] |

**Score A5 = 0.80 / 1.00**

**Hésitations / ambiguïtés :** R4 et R5 sont les points les plus discutables. Pour R4, on pourrait argumenter 1 si l'on considère que le remodelage chromatinien *est* une modification du mécanisme de régulation (pas seulement du paramètre). Mais la distinction est que la cellule ne change pas le *type* de mécanisme régulateur — elle module l'accessibilité. Pour R5, le 0.5 reflète la tension entre la capacité réelle de générer de la nouveauté (mutations, recombinaisons) et le fait que cette capacité n'est pas une production dirigée de nouvelles règles au sens systémique.

---

## Synthèse

| Axe | Score |
|-----|-------|
| A1 | 1.00 |
| A2 | 1.00 |
| A3 | 1.00 |
| A4 | 1.00 |
| A5 | 0.80 |

### Gradients (calculés)

| Gradient | Valeur |
|----------|--------|
| Δ₂₃ = A2 − A3 | 0.00 |
| Δ₄₅ = A4 − A5 | +0.20 |
| Δ₁₂ = A1 − A2 | 0.00 |
| Δ₃₅ = A3 − A5 | +0.20 |
| Δ₄₃ = A4 − A3 | 0.00 |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système fortement autonome — scores quasi-saturés sur tous les axes. Profil caractéristique d'un organisme biologique à l'échelle cellulaire.
- **Régime secondaire :** Légère rigidité relative (Δ₄₅ = +0.20) — la normativité dépasse légèrement la capacité de révision, ce qui est typique d'un système optimisé par la sélection naturelle : très robuste, mais limité dans sa capacité à s'auto-modifier fondamentalement.
- **Marge :** Très faible — seuls R4 et R5 ne sont pas saturés.
- **Surprise par rapport au jugement intuitif :** Aucune surprise. La cellule eucaryote est le paradigme du système biologique autonome intégré. Le seul résultat notable est la quasi-saturation même sur A5, qui reflète la richesse des mécanismes de plasticité cellulaire (épigénétique, remodelage, différenciation) souvent sous-estimée.

---

## Notes libres

La cellule eucaryote atteint des scores remarquablement élevés sur tous les axes, ce qui en fait probablement le système micro le mieux « équilibré » du dataset. Quelques observations :

1. **Profondeur hiérarchique exceptionnelle pour un système micro.** La compartimentation membranaire (noyau, RE, Golgi, mitochondries, lysosomes) crée une profondeur structurelle rare à cette échelle.

2. **Le gradient Δ₄₅ = +0.20 est le signal le plus informatif.** Il capture le fait que la cellule est optimisée pour maintenir son état (normativité élevée) plutôt que pour se transformer (plasticité légèrement plus contrainte). Cela reflète l'asymétrie fondamentale du vivant : la sélection naturelle favorise la robustesse sur l'innovation à l'échelle individuelle.

3. **Tension R4/R5.** Le débat porte sur la frontière entre « modifier une règle » et « modifier un paramètre au sein d'une règle ». Le remodelage chromatinien change quels gènes sont régulés, pas comment la régulation fonctionne. La recombinaison V(D)J est un cas limite fascinant : c'est un mécanisme programmé pour produire de la nouveauté, mais seulement dans un domaine très restreint.

4. **Comparaison attendue.** Ce profil devrait contraster fortement avec les systèmes technologiques (faible normativité endogène) et les systèmes institutionnels (profondeur hiérarchique comparable mais plasticité variable).
