# SYS005 — Colonie de fourmis

## Identification

- **System ID :** SYS005

- **System name :** Colonie de fourmis

- **Domain :** biological

- **Subdomain :** insect society / collective organization

- **Scale :** meso

- **Date scored :** 2026-04-02

- **Scorer :** GPT

- **Confidence globale :** high

## Sources

1. Deborah M. Gordon, *Ant Encounters: Interaction Networks and Colony Behavior*.

2. Bonabeau, Dorigo, Theraulaz, *Swarm Intelligence*.

3. Theraulaz & Bonabeau, *A Brief History of Stigmergy*.

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                            |
| --------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Le système articule au minimum le niveau de l’ouvrière individuelle et celui du comportement global de la colonie. Gordon insiste précisément sur le passage « from individual to collective behavior ». |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | On distingue les individus, les groupes de tâche/réseaux d’interaction, puis la colonie comme totalité comportementale.                                                                                  |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | On peut isoler au moins quatre strates : signaux/stimuli locaux, individus, réseaux d’interaction et allocation de tâches, colonie insérée dans une écologie de voisinage et de taille.                  |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les niveaux ne sont pas redondants : les ouvrières exécutent, les réseaux distribuent l’information, la colonie régule l’allocation, la taille/architecture du nid modifient les motifs d’interaction.   |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Le comportement individuel dépend des interactions coloniales, tandis que la taille de colonie, l’architecture du nid et l’état global modifient en retour les interactions et les tâches.               |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Le 4e niveau peut être décrit comme « écologie/architecture/taille » plutôt que comme niveau autonome strict ; mais la profondeur hiérarchique reste clairement élevée.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                  |
| ------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Le retrait d’un groupe de travailleurs ou la variation d’un flux d’interactions entraîne un basculement d’autres groupes de tâche.                                                                             |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Un changement local d’interaction ou de présence d’ouvrières modifie l’allocation de tâches au niveau de la colonie.                                                                                           |
| P3 : Propagation modifie l’état global observable             | 1     | Le motif global de recherche de nourriture, le choix d’une branche, l’orientation du fourragement ou la répartition des tâches changent à l’échelle de la colonie.                                             |
| P4 : Isolement difficile sans modification structurelle       | 0.5   | L’isolement complet est difficile car les tâches se compensent mutuellement, mais certaines manipulations locales restent possibles expérimentalement ; le couplage est fort sans être absolument indivisible. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage n’est pas une simple juxtaposition : interactions, stigmergie, taille du nid, âge et environnement s’enchevêtrent dans la régulation collective.                                                   |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
P4 pourrait monter à 1 dans une lecture très « systémique », mais je garde 0.5 parce que la littérature citée montre aussi des manipulations localisées et des compensations.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                          |
| ---------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Il existe plusieurs mécanismes explicites : réseaux d’interaction, task allocation, pistes chimiques, stigmergie, réponses aux rencontres.                             |
| I2 : Réduction de variance observable    | 1     | La colonie converge vers des solutions collectives stables : exploitation préférentielle d’une branche, orientation du fourragement, répartition de tâches adaptée.    |
| I3 : Synchronisation multi-niveaux       | 0.5   | Il y a coordination entre âge, localisation, interactions et tâches, mais le terme de synchronisation stricte est moins démontré que celui de coordination distribuée. |
| I4 : Boucles de rétroaction globales     | 1     | Les boucles positives et négatives sont centrales : renforcement phéromonal, evaporation/limitation, ajustement par interactions répétées.                             |
| I5 : Maintien d'un état global cohérent  | 1     | Malgré l’absence de centre de commande, la colonie maintient un comportement global cohérent de nutrition, entretien, exploration et reproduction.                     |

**Score A3 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
I3 dépend de ce qu’on entend par synchronisation : forte si on accepte une synchronisation distribuée, plus faible si on exige un alignement temporel strict.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                    |
| -------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1 : Attracteur dynamique existant           | 1     | La colonie présente des attracteurs collectifs nets : branche dominante, sentier entretenu, état de task allocation, motifs spatiaux de construction ou de tri.                                  |
| N2 : Correction active d'écart               | 1     | Lorsqu’un groupe manque ou qu’une tâche devient prioritaire, d’autres ouvrières changent d’activité ; il y a donc correction active des écarts fonctionnels.                                     |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Il existe des priorités pratiques entre tâches selon l’état du nid, du fourragement ou du couvain, mais la hiérarchie n’est pas formalisée comme une architecture normative explicite et stable. |
| N4 : Mécanisme interne de stabilisation      | 1     | La stabilisation interne repose sur les interactions locales, la stigmergie et les boucles de feedback sans contrôle externe.                                                                    |
| N5 : Résistance aux perturbations prolongées | 0.5   | La colonie est robuste, mais cette robustesse a des limites fortes : les jeunes colonies échouent souvent, certaines espèces se piègent sur des trajectoires sous-optimales.                     |

**Score A4 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**  
N5 pourrait être noté plus haut pour les colonies matures, mais les sources montrent clairement que la robustesse varie beaucoup avec la taille et le contexte écologique.

**Distinction normativité endogène / imposée :**  
Normativité très majoritairement **endogène** : pas de chef, pas de plan central, régulation par interactions, structure du nid et traces environnementales.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                  |
| -------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Les ouvrières modifient localement leur réponse selon le contexte d’interactions, la tâche en cours et les signaux rencontrés.                                                                                 |
| R2 : Modification durable de configuration interne | 1     | Les changements de tâche, l’âge polyéthique, la redistribution des rôles et certaines modifications chimiques/comportementales persistent au-delà de l’instant.                                                |
| R3 : Reconfiguration de réseau ou de structure     | 1     | Les réseaux de piste, les motifs d’interaction et parfois l’architecture du nid se reconfigurent avec la taille, l’environnement et les perturbations.                                                         |
| R4 : Modification des mécanismes de régulation     | 0.5   | Les mécanismes régulateurs changent partiellement avec la taille de colonie et l’écologie, mais les sources appuient surtout une modulation du fonctionnement plutôt qu’une refonte explicite des méta-règles. |
| R5 : Capacité à produire de nouvelles règles       | 0     | Je ne vois pas dans les sources de preuve solide d’une production endogène de règles nouvelles au sens fort ; il y a plasticité, pas méta-invention explicite.                                                 |

**Score A5 = 0.70 / 1.00**

**Hésitations / ambiguïtés :**  
R4 pourrait être monté à 1 dans une lecture très large de la plasticité développementale, mais les sources ne documentent pas assez une modification explicite des mécanismes de régulation eux-mêmes.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 1.00  |
| A2  | 0.90  |
| A3  | 0.90  |
| A4  | 0.80  |
| A5  | 0.70  |

### Gradients

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | 0.10   |
| Δ₁₂ = A1 − A2 | 0.10   |
| Δ₃₅ = A3 − A5 | 0.20   |
| Δ₄₃ = A4 − A3 | -0.10  |

### Classification

- **Régime primaire :** Équilibre

- **Régime secondaire :** légère rigidité normative

- **Marge :** modérée

- **Surprise par rapport au jugement intuitif :** la colonie paraît souvent “quasi parfaite” intuitivement, mais les sources poussent à abaisser un peu A4 et surtout A5 : forte coordination ne veut pas dire forte capacité de révision au sens méta-régulatoire.

## Lecture rapide

La **colonie de fourmis** sort ici comme un système **très intégré, fortement hiérarchisé au plan causal, à propagation élevée mais compensée par une intégration tout aussi élevée**. Le point le plus distinctif n’est pas une rigidité absolue, mais une **coordination endogène distribuée** par interactions, traces et architecture. La faiblesse relative porte sur **A5** : il y a beaucoup de plasticité, mais peu d’indices d’une capacité à générer de nouvelles règles de régulation au sens fort.


