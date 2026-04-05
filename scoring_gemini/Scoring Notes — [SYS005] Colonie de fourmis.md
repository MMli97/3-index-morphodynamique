# Scoring Notes — [SYS005] Colonie de fourmis

## Identification

- **System ID :** SYS005

- **System name :** Colonie de fourmis (Ant colony)

- **Domain :** biological

- **Subdomain :** Insectes sociaux / Systèmes complexes

- **Scale :** meso / macro

- **Date scored :** 2026-04-01

- **Scorer :** IA

- **Confidence globale :** high

## Sources

1. 106454699568700 -- f6e81f5da67f36dd0cbdfe2316b79dfa -- Anna’s Archive.txt (Theraulaz & Bonabeau, 1999, *A Brief History of Stigmergy*)

2. Ant Encounters_ Interaction Networks and Colony Behavior_ -- Deborah M_ Gordon -- 2010 -- PrincetonUP -- 48f10bd46975b10efec44f32907fbe71 -- Anna’s Archive.txt (Gordon, D.M., 2010, *Ant Encounters*)

3. SWARMI~1.txt (Bonabeau, Dorigo, Theraulaz, 1999, *Swarm Intelligence: From Natural to Artificial Systems*)

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                                                                                                                             |
| --------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | L'étude des colonies relie explicitement le niveau de l'individu (micro) et le niveau de la colonie (macro). Le comportement global n'est pas réductible à l'individu.                                                                                                        |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | On observe le niveau de l'individu, le niveau des sous-groupes de tâches ou réseaux d'interactions temporels, et le niveau global de la colonie.                                                                                                                              |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5       | Bien que les individus, les groupes, et les colonies soient bien définis, le 4ème niveau (super-colonies interconnectées ou interaction au niveau de l'écosystème) existe chez certaines espèces mais n'est pas le standard de régulation interne de la plupart des colonies. |
| H4 : Niveaux fonctionnellement différenciés   | 1         | Les individus exécutent des tâches simples basées sur des signaux locaux (phéromones, interactions antennaires), tandis que la colonie, vue comme un organisme écologique, gère la survie, la reproduction et l'allocation dynamique des tâches.                              |
| H5 : Causalité bidirectionnelle entre niveaux | 1         | L'action individuelle modifie l'environnement et l'état de la colonie (causalité ascendante par stigmergie ou réseaux de contacts), ce qui modifie en retour la probabilité des comportements des autres individus (causalité descendante).                                   |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** L'attribution du 4ème niveau hiérarchique dépend de la considération du tissu écologique ou des super-colonies (comme chez *Formica lugubris* ou la fourmi d'Argentine) comme niveau d'organisation causal direct de l'entité de base.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                                                                   |
| ------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | Le retrait d'un groupe d'ouvrières affectées à une tâche pousse d'autres ouvrières à changer de rôle pour compenser cette absence.                                                                  |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | Une perturbation locale, comme la découverte de nourriture ou un obstacle, remonte le réseau d'interaction et modifie la dynamique de recrutement et l'allocation des tâches de toute la colonie.   |
| P3 : Propagation modifie l'état global observable             | 1         | La modification d'un stimulus local s'amplifie (effet boule de neige) jusqu'à modifier l'état et l'architecture macroscopique, par exemple dans la création de ponts, de pistes ou de nids.         |
| P4 : Isolement difficile sans modification structurelle       | 1         | Les fourmis fonctionnent par interactions constantes ; un individu isolé ne peut ni maintenir une dynamique normale, ni effectuer les choix nécessaires à sa survie qui dépendent du réseau social. |
| P5 : Couplage fonctionnel non trivial                         | 1         | Le système repose sur des "toiles denses de contingence" où les taux de rencontres et la stigmergie ajustent dynamiquement le système de manière complexe.                                          |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune. La propagation ascendante des perturbations et l'auto-organisation sont des caractéristiques majeures de ce système.

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                                                                                          |
| ---------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1         | La coordination se fait sans contrôle central via la stigmergie (communication indirecte par modification de l'environnement) et les réseaux de contacts directs.                                          |
| I2 : Réduction de variance observable    | 1         | Le processus d'auto-organisation, malgré des fluctuations et erreurs individuelles (hasard, bruits), permet l'émergence de structures macroscopiques stables, robustes et cohérentes (ex. sentiers, nids). |
| I3 : Synchronisation multi-niveaux       | 1         | Les taux d'interaction synchronisent et ajustent le nombre d'individus alloués aux différentes tâches selon les fluctuations internes (faim des larves) et externes.                                       |
| I4 : Boucles de rétroaction globales     | 1         | Le maintien des schémas collectifs dépend de l'équilibre entre rétroactions positives (recrutement, amplification) et rétroactions négatives (évaporation des phéromones, compétition).                    |
| I5 : Maintien d'un état global cohérent  | 1         | La colonie régule de façon homéostatique ses réserves, son architecture et sa défense en temps réel afin de maintenir la viabilité du superorganisme.                                                      |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Le mécanisme "explicite" de coordination n'est pas un contrôleur central, mais la définition du critère accepte les protocoles de coordination distribuée (comme la stigmergie).

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                                                      |
| -------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1 : Attracteur dynamique existant           | 1         | La multistabilité est documentée : en cas de pistes ou de sources multiples, le système peut converger vers l'un des nombreux états stables possibles, agissant comme un attracteur pour le système.   |
| N2 : Correction active d'écart               | 1         | En cas de perturbations perturbant le bon fonctionnement du nid, la colonie compense activement via la flexibilité comportementale de ses membres (changement de tâches).                              |
| N3 : Hiérarchie de priorités régulatoires    | 1         | La colonie gère des priorités de haut niveau ; par exemple, en présence de multiples perturbations importantes, une grande colonie va prioriser la recherche de nourriture sur la maintenance du nid.  |
| N4 : Mécanisme interne de stabilisation      | 1         | Les boucles de rétroaction négative stabilisent les structures : l'évaporation des phéromones ou la saturation des sources empêche le système de s'emballer de façon sous-optimale de façon prolongée. |
| N5 : Résistance aux perturbations prolongées | 1         | L'évolution de l'âge d'une colonie lui permet de résister de plus en plus efficacement aux perturbations de l'environnement, sans nécessiter d'instructions extérieures.                               |

**Score A4 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Distinction normativité endogène / imposée : La normativité de la colonie est purement endogène, produite par la sélection naturelle écologique, opérant via les dynamiques interactionnelles, sans aucun "ingénieur" humain.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                                                                                                                                  |
| -------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| R1 : Ajustement paramétrique local                 | 1         | L'insecte modifie la probabilité de ses réponses et seuils d'activation (par exemple en s'habituant, ou par son propre vieillissement) face aux stimuli locaux et aux taux d'interaction.                                                                          |
| R2 : Modification durable de configuration interne | 1         | Le comportement global et la gestion des tâches changent durablement à mesure que la colonie devient plus grande et plus mature ; le profil et le rythme du système évoluent.                                                                                      |
| R3 : Reconfiguration de réseau ou de structure     | 1         | Lorsqu'une branche d'un réseau (comme un réseau de nids interconnectés ou de pistes) est sectionnée, les fourmis trouvent et redirigent leur trafic vers un nouveau réseau fonctionnel optimisé.                                                                   |
| R4 : Modification des mécanismes de régulation     | 1         | Dans une grande colonie (vieille), l'expérience statistique de chaque fourmi est modifiée (le nombre de rencontres augmente massivement), ce qui modifie la robustesse et la régulation mêmes des réseaux face au monde extérieur.                                 |
| R5 : Capacité à produire de nouvelles règles       | 0.5       | Bien qu'une grande plasticité et des réponses émergentes complexes (ex. effets non-additifs aux stimuli) existent, les algorithmes sous-jacents de la fourmi (règles locales) évoluent peu à l'échelle de la vie de la colonie, leur nouveauté est situationnelle. |

**Score A5 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** L'attribution du critère R5 est délicate. Si le système d'interaction peut produire des stratégies très inattendues en s'adaptant à des environnements inédits, les "règles" neuronales ou de base des individus restent dictées par la phylogenèse. Un score de 0.5 reflète cette émergence d'adaptations nouvelles mais non génératives au sens symbolique.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 0.90      |
| A2      | 1.00      |
| A3      | 1.00      |
| A4      | 1.00      |
| A5      | 0.90      |

### Gradients (calculés)

| **Gradient**  | **Valeur** |
| ------------- | ---------- |
| Δ₂₃ = A2 − A3 | 0.00       |
| Δ₄₅ = A4 − A5 | 0.10       |
| Δ₁₂ = A1 − A2 | -0.10      |
| Δ₃₅ = A3 − A5 | 0.10       |
| Δ₄₃ = A4 − A3 | 0.00       |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Auto-organisation biologique (Système complexe distribué et hautement intégré)

- **Régime secondaire :** Adaptation plastique endogène

- **Marge :** Le système se situe aux limites supérieures de la régulation et de la propagation décentralisées.

- **Surprise par rapport au jugement intuitif :** Une intégration (A3) aussi parfaite (1.0) dans un système où chaque élément est réputé "aveugle" à la situation globale illustre très fortement la puissance de la causalité asymétrique et de la stigmergie.

---

## Notes libres

Les modèles d'intelligence en essaim (Swarm Intelligence) confirment tous que la colonie de fourmis accomplit des tâches globales (comme le problème du plus court chemin, l'homéostasie, le tri complexe) sans jamais recourir à un contrôle descendant direct. C'est l'un des archétypes absolus des systèmes complexes normatifs endogènes de la biologie, caractérisé par un A2 et un A3 maximaux.
