# Scoring Notes — SYS005 Colonie de fourmis

## Identification

- **System ID :** SYS005
- **System name :** Colonie de fourmis (ant colony)
- **Domain :** biological
- **Subdomain :** entomologie sociale / systèmes collectifs
- **Scale :** meso
- **Date scored :** 2026-04-01
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Bonabeau, E., Dorigo, M. & Theraulaz, G. (1999). *Swarm Intelligence: From Natural to Artificial Systems*. Oxford University Press.
2. Gordon, D. M. (2010). *Ant Encounters: Interaction Networks and Colony Behavior*. Princeton University Press.
3. Theraulaz, G. & Bonabeau, E. (1999). "A Brief History of Stigmergy." *Artificial Life*, 5(2), 97–116.

---

## A1 — Profondeur hiérarchique

| Sous-critère | Score | Justification |
|---|---|---|
| H1 : ≥ 2 niveaux causaux distincts | 1 | Deux niveaux clairement documentés : (1) individu (fourmi ouvrière avec seuils de réponse, comportement local) et (2) colonie (patterns collectifs émergents — pistes de fourragement, allocation de tâches). Bonabeau ch.1 : le comportement collectif émerge d'interactions entre individus simples. Gordon ch.1 : le comportement de la colonie ne se réduit pas aux attributs individuels. |
| H2 : ≥ 3 niveaux causaux distincts | 1 | Trois niveaux identifiables : (1) individu (réponses sensorimotrices, seuils internes), (2) sous-groupe fonctionnel (caste, groupe de tâche — fourrageuses, patrouilleuses, nourrices), (3) colonie entière (allocation globale des tâches, architecture du nid, exploitation des ressources). Gordon ch.2 : la colonie ajuste les effectifs par tâche ; les groupes de tâches sont des niveaux intermédiaires fonctionnels distincts. |
| H3 : ≥ 4 niveaux causaux distincts | 0.5 | Un quatrième niveau — l'environnement modifié (stigmergie) — agit comme substrat causal distinct : les traces phéromonales et structures du nid constituent un niveau d'information externe au corps des individus qui contraint le comportement collectif (Theraulaz & Bonabeau 1999 : la colonie enregistre son activité dans l'environnement physique). Cependant, ce niveau n'est pas strictement « interne » au système au sens classique, d'où 0.5. |
| H4 : Niveaux fonctionnellement différenciés | 1 | Chaque niveau remplit des fonctions distinctes : l'individu exécute des réponses stimulus-action ; le sous-groupe fonctionnel spécialise temporairement certaines tâches (polyéthisme temporel, castes morphologiques chez Pheidole) ; la colonie réalise l'allocation globale, la reproduction et la défense. Bonabeau ch.3 : division du travail entre castes fonctionnellement distinctes. |
| H5 : Causalité bidirectionnelle entre niveaux | 1 | Causalité ascendante : les interactions locales entre individus produisent les patterns collectifs (auto-organisation, Bonabeau ch.1). Causalité descendante : le contexte colonial (taux de rencontre, stimuli globaux, besoins collectifs) modifie le comportement individuel. Gordon ch.2-3 : le taux d'interaction avec les patrouilleuses détermine si une fourrageuse sort du nid ; le retrait d'ouvrières d'un groupe modifie le comportement des autres groupes. |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** Le statut du niveau stigmergique (environnement modifié) comme niveau hiérarchique « interne » au système est discutable. On pourrait argumenter que l'environnement modifié fait partie intégrante du système étendu (extended phenotype), ce qui justifierait 1 pour H3. Score conservateur à 0.5.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère | Score | Justification |
|---|---|---|
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1 | Gordon ch.2 : quand on augmente le nombre d'ouvrières de maintenance (en ajoutant des cure-dents), le nombre de fourrageuses diminue. Le retrait de mineures stimule les majeures à prendre en charge les tâches des mineures (Wilson/Bonabeau ch.3). Une perturbation d'un groupe de tâche se propage aux autres. |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique | 1 | Le retrait d'individus (niveau individu) modifie l'allocation globale de la colonie (niveau colonie). Inversement, un changement environnemental global (ex. nouvelle source de nourriture) modifie les comportements individuels via les pistes phéromonales. Bonabeau ch.2 : la sélection collective du chemin le plus court émerge de boucles de rétroaction traversant individus et pistes. |
| P3 : Propagation modifie l'état global observable | 1 | La découverte d'une source de nourriture par quelques éclaireuses modifie le pattern global de fourragement de toute la colonie (recrutement de masse, Bonabeau ch.2). Le retrait d'une caste modifie l'ensemble de la distribution des tâches à l'échelle coloniale (Wilson 1984 via Bonabeau ch.3). |
| P4 : Isolement difficile sans modification structurelle | 1 | Les modules fonctionnels sont couplés par les taux d'interaction et les signaux chimiques diffus. Gordon ch.2-3 : on ne peut pas isoler le fourragement de la patrouille sans modifier le système, car le déclenchement du fourragement dépend du retour des patrouilleuses. Bonabeau ch.1 : l'auto-organisation repose sur des interactions multiples et la densité minimale d'individus. |
| P5 : Couplage fonctionnel non trivial | 1 | Le couplage entre modules est non linéaire : rétroaction positive (recrutement par phéromone, effet boule de neige) et négative (saturation, compétition entre sources, épuisement). Bonabeau ch.1 : les fonctions de choix probabilistes sont non linéaires (Eq. 2.1 avec exposant n≈2). Le couplage entre groupes de tâches passe par des taux d'interaction, pas par des commandes directes. |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune hésitation majeure. La propagation inter-modules est très bien documentée empiriquement et théoriquement.

---

## A3 — Intégration

| Sous-critère | Score | Justification |
|---|---|---|
| I1 : Mécanisme explicite de coordination | 1 | Deux mécanismes de coordination explicitement identifiés : (1) stigmergie — coordination indirecte via l'environnement modifié (phéromones de piste, pelotes de sol imprégnées ; Grassé/Theraulaz & Bonabeau 1999). (2) interactions directes — antennation, trophallaxie, contact chimique (Bonabeau ch.1, Gordon ch.3 : hydrocarbures cuticulaires spécifiques à la tâche). |
| I2 : Réduction de variance observable | 1 | La sélection collective du chemin le plus court réduit la variance des trajets individuels (Bonabeau ch.2 : convergence vers une branche dominante dans l'expérience du pont à deux branches). L'allocation des tâches produit des ratios stables malgré la variabilité individuelle. Gordon ch.2 : d'un jour à l'autre, en conditions stables, une fourmi continue la même tâche. |
| I3 : Synchronisation multi-niveaux | 0.5 | Il existe une forme de synchronisation : les patrouilleuses déclenchent le fourragement (Gordon ch.3 : le retour des patrouilleuses au taux de ~1/10s déclenche la sortie des fourrageuses). Le polyéthisme temporel coordonne les transitions entre tâches. Cependant, il ne s'agit pas d'une synchronisation au sens strict (horloge globale), mais plutôt d'un entraînement séquentiel par cascades de stimuli. |
| I4 : Boucles de rétroaction globales | 1 | Boucles positives : recrutement par phéromone de piste (plus de fourmis → plus de phéromone → plus de fourmis). Boucles négatives : épuisement des sources, saturation, compétition entre pistes. Bonabeau ch.1 : ces quatre ingrédients (rétroaction +, rétroaction −, fluctuations, interactions multiples) sont les bases de l'auto-organisation. Gordon ch.3 : le taux de retour des fourrageuses avec nourriture régule le taux de départ des nouvelles fourrageuses. |
| I5 : Maintien d'un état global cohérent | 1 | La colonie maintient une allocation cohérente des tâches malgré les perturbations. Gordon ch.2 : quand des fourrageuses sont retirées, la colonie ajuste les effectifs sans qu'aucun individu ne perçoive l'état global. Le nid maintient sa structure architecturale, les pistes de fourragement sont stables. Bonabeau ch.3 : le modèle à seuils de réponse montre que la colonie retrouve un état d'équilibre après perturbation. |

**Score A3 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** I3 à 0.5 car la synchronisation est de nature séquentielle/cascadée plutôt que simultanée. On pourrait argumenter pour 1 si l'on considère la synchronisation fonctionnelle (les niveaux s'ajustent mutuellement en continu), mais le mécanisme reste local et distribué sans véritable signal de synchronisation globale.

---

## A4 — Normativité

| Sous-critère | Score | Justification |
|---|---|---|
| N1 : Attracteur dynamique existant | 1 | Multistabilité documentée : dans l'expérience du pont à deux branches, la colonie converge vers l'exploitation massive d'une branche (Bonabeau ch.2 : deux attracteurs possibles, exploitation de A ou de B). L'allocation des tâches converge vers un ratio stable. Le modèle à seuils de réponse (Bonabeau ch.3) produit des états d'équilibre stables. |
| N2 : Correction active d'écart | 1 | Quand des ouvrières sont retirées, la colonie compense activement. Wilson (via Bonabeau ch.3) : le retrait des mineures provoque l'activation des majeures en moins de deux heures. Gordon ch.2 : le retrait de fourrageuses réduit le taux de sortie (régulation), le retrait de patrouilleuses empêche le fourragement (correction par absence de signal de sécurité). La colonie corrige les déviations du ratio normal de tâches. |
| N3 : Hiérarchie de priorités régulatoires | 0.5 | Il existe un ordre implicite de priorités : la défense prime sur le fourragement (les fourmis alarmées interrompent les autres tâches, Gordon ch.2). Le fourragement agit comme « puits » (sink) dans la séquence des tâches (Gordon ch.2 : une fois fourrageuse, pas de retour). Mais cette hiérarchie est plus un produit émergent qu'un système de priorités explicitement structuré. |
| N4 : Mécanisme interne de stabilisation | 1 | Les rétroactions négatives stabilisent le système : épuisement des sources, compétition entre pistes, saturation des tâches. Bonabeau ch.1 : la rétroaction négative contrebalance la rétroaction positive et stabilise le pattern collectif. Les seuils de réponse individuels fonctionnent comme mécanisme interne de stabilisation de l'allocation des tâches. |
| N5 : Résistance aux perturbations prolongées | 1 | La colonie maintient son fonctionnement face à des perturbations durables. Gordon ch.4 (implicite dans ch.2) : les colonies plus âgées et plus grandes sont plus stables. Bonabeau ch.3 : le modèle à seuils variables avec apprentissage montre une robustesse supérieure aux perturbations prolongées par rapport au modèle à seuils fixes. La plasticité de la division du travail permet une résilience face aux pertes prolongées de travailleurs. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** N3 à 0.5 : la hiérarchie de priorités existe mais émerge des seuils différentiels plutôt que d'un système de priorités explicitement codé. On pourrait argumenter pour 1 si l'on admet que les différences de seuils constituent une hiérarchie fonctionnelle de facto.

**Distinction normativité endogène / imposée :** Normativité entièrement endogène. Aucun agent externe n'impose les normes régulatoires. Les attracteurs, les corrections, et les mécanismes de stabilisation émergent des propriétés intrinsèques des individus (seuils de réponse, réponses chimiques) et de leurs interactions. La sélection naturelle a façonné ces mécanismes, mais la régulation opère de manière autonome sans contrôle central.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère | Score | Justification |
|---|---|---|
| R1 : Ajustement paramétrique local | 1 | Les fourmis ajustent leur comportement en continu en fonction des stimuli locaux. Gordon ch.3 : une fourrageuse inactive est stimulée à sortir par le taux de retour des fourrageuses chargées. Les seuils de réponse individuels modulent la probabilité de réponse. Bonabeau ch.2 : la probabilité de choix d'une branche dépend de la concentration locale de phéromone. |
| R2 : Modification durable de configuration interne | 1 | Bonabeau ch.3 : le modèle à seuils variables montre que l'expérience modifie durablement les seuils individuels (apprentissage par renforcement : le seuil diminue quand la tâche est effectuée, augmente sinon). Withers et al. (via Bonabeau ch.3) : des changements cérébraux durables sont associés à l'expérience de fourragement chez les abeilles, et les fourrageuses précoces montrent la même organisation cérébrale que les fourrageuses normales plus âgées. Applicable par analogie aux fourmis. |
| R3 : Reconfiguration de réseau ou de structure | 1 | La colonie reconfigure ses réseaux de pistes en réponse aux changements environnementaux. Bonabeau ch.2 : quand la qualité relative des sources change, les abeilles (et par extension les fourmis à recrutement de masse) peuvent basculer vers la meilleure source. Gordon ch.2 : les fourmis changent de tâche quand les besoins changent (passage maintenance → patrouille → fourragement). Le réseau d'allocation des tâches est dynamiquement reconfiguré. |
| R4 : Modification des mécanismes de régulation | 0.5 | Gordon ch.4 (évoqué dans ch.1-2) : les colonies plus âgées et plus grandes régulent différemment que les jeunes colonies (les jeunes colonies sont moins stables dans l'allocation des tâches). Cela suggère que les mécanismes de régulation eux-mêmes changent avec la maturation. Cependant, ce changement est lent (ontogénique) et non une véritable modification des règles de régulation au cours de la vie d'une colonie mature. |
| R5 : Capacité à produire de nouvelles règles | 0 | Pas de preuve que la colonie invente de nouvelles règles comportementales. Les règles individuelles (stimulus-réponse, seuils) sont fixées par l'évolution. L'auto-organisation produit de nouveaux patterns, mais pas de nouvelles règles de comportement individuel. La plasticité est paramétrique, pas générative de nouvelles catégories de règles. |

**Score A5 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** R4 est le point le plus débattable. Le changement ontogénique de régulation (colonies jeunes vs. matures) est documenté par Gordon mais relève davantage du développement que de la plasticité adaptative en temps réel. R5 à 0 est net : aucune source ne documente de création endogène de règles nouvelles.

---

## Synthèse

| Axe | Score |
|-----|-------|
| A1 | 0.90 |
| A2 | 1.00 |
| A3 | 0.90 |
| A4 | 0.90 |
| A5 | 0.70 |

### Gradients (calculés)

| Gradient | Valeur |
|----------|--------|
| Δ₂₃ = A2 − A3 | +0.10 |
| Δ₄₅ = A4 − A5 | +0.20 |
| Δ₁₂ = A1 − A2 | −0.10 |
| Δ₃₅ = A3 − A5 | +0.20 |
| Δ₄₃ = A4 − A3 | 0.00 |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système auto-organisé à haute intégration — propagation maximale (A2=1.00), forte normativité endogène (A4=0.90), intégration élevée (A3=0.90).
- **Régime secondaire :** Système à plasticité contrainte — capacité de révision limitée par l'absence de génération de nouvelles règles (A5=0.70).
- **Marge :** Le gradient Δ₄₅ = +0.20 indique un écart modéré entre la capacité normative et la capacité de révision : le système est meilleur à maintenir ses normes qu'à les réviser. Profil typique d'un système biologique évolué mais non cognitif.
- **Surprise par rapport au jugement intuitif :** Pas de surprise majeure. Le score élevé en A2 (propagation maximale) confirme l'intuition que la colonie de fourmis est un système massivement couplé. Le score modérément élevé en A5 (0.70) est peut-être légèrement supérieur à l'attente naïve (on pourrait croire le système plus rigide), mais la plasticité des seuils de réponse et la reconfiguration dynamique des tâches justifient ce score.

---

## Notes libres

- La colonie de fourmis est un cas paradigmatique d'auto-organisation biologique. Les trois sources convergent sur le fait que la coordination émerge sans contrôle central, via des mécanismes stigmergiques et des interactions directes locales.
- Le concept de seuil de réponse variable (Bonabeau/Theraulaz ch.3) est crucial pour comprendre simultanément la normativité (N2, N4) et la plasticité (R1, R2) : le même mécanisme produit à la fois stabilité et flexibilité.
- Gordon insiste sur le fait que le taux d'interaction (et non le contenu du message) est l'information clé pour la régulation collective. Cela renforce le score en I4 et en P5 (couplage non trivial).
- La distinction entre colonies jeunes/petites (moins stables, plus plastiques) et colonies âgées/grandes (plus stables, plus prévisibles) suggère que les scores A3-A4-A5 pourraient varier selon l'âge de la colonie. Le scoring ici vise une colonie mature.
- L'absence de capacité à produire de nouvelles règles (R5=0) est la principale limitation du système et le distingue nettement des systèmes cognitifs ou institutionnels.
