# SYS014 — Réseau neuronal cérébral

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                              |
| --------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Oui sans ambiguïté : neurones/synapses, circuits locaux, régions, systèmes à grande échelle. Le cerveau est explicitement décrit comme « a network of networks ».          |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | Oui : les sources décrivent l’emboîtement neurones → populations locales → régions → grands systèmes cérébraux.                                                            |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | Oui : Sporns insiste sur les échelles micro, méso, macro et sur les interactions cerveau-corps-environnement.                                                              |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Oui : les niveaux ne sont pas seulement empilés, ils sont spécialisés; circuits locaux, modules, hubs, aires sensorielles et systèmes cognitifs ont des rôles distincts.   |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Oui : la littérature citée met l’accent sur la récurrence, la réentrée, le feedforward et le feedback comme processus unifié, avec influences ascendantes et descendantes. |

**Score A1 = 1.00**

**Hésitations / ambiguïtés :** très faibles. La seule ambiguïté tient au périmètre exact du système retenu : réseau anatomique seul, réseau fonctionnel, ou cerveau incarné. Mais dans tous les cas, la profondeur hiérarchique reste très élevée.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score | Justification                                                                                                                                                                        |
| ------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Oui : les hubs relient les modules et une perturbation d’un nœud central peut se diffuser rapidement dans le réseau.                                                                 |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Oui : les sources décrivent la propagation entre échelles, des interactions neuronales locales aux dynamiques de populations et de systèmes larges.                                  |
| P3 : Propagation modifie l’état global observable             | 1     | Oui : la dynamique cérébrale comporte des états métastables globaux, des fluctuations de cohérence, de connectivité fonctionnelle et de synchronisation.                             |
| P4 : Isolement difficile sans modification structurelle       | 1     | Oui : du fait de la récurrence, des hubs, des chemins courts et de l’interdépendance des modules, isoler un sous-système sans altérer la structure générale est difficile.           |
| P5 : Couplage fonctionnel non trivial                         | 1     | Oui très clairement : petit monde, modularité hiérarchique, hubs, synchronisation partielle, réentrance, états métastables. On est très loin d’un couplage simple ou purement local. |

**Score A2 = 1.00**

**Hésitations / ambiguïtés :** faibles. On pourrait nuancer selon qu’on parle d’un microcircuit isolé ou du réseau cérébral entier, mais pour le système formulé comme « réseau neuronal cérébral », la propagation est manifestement forte et multi-échelle.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                           |
| ---------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Oui : réentrée, synchronisation, hubs intégrateurs, coordination inter-modulaire, intégration sensorimotrice et coordination de circuits distribués.                    |
| I2 : Réduction de variance observable    | 1     | Oui, au moins au sens fonctionnel : la coordination réduit les degrés de liberté et projette la dynamique sur un espace plus bas dimensionnel de variables collectives. |
| I3 : Synchronisation multi-niveaux       | 1     | Oui : les sources décrivent synchronisation intra- et interrégionale, cohérence large échelle, assemblées cellulaires, et dépendance inter-échelles.                    |
| I4 : Boucles de rétroaction globales     | 1     | Oui : feedback, récurrence et réentrée sont constitutifs de l’architecture cérébrale étudiée.                                                                           |
| I5 : Maintien d’un état global cohérent  | 1     | Oui : malgré la modularité, les hubs et les dynamiques de coordination assurent cohérence système-wide et intégration de l’information.                                 |

**Score A3 = 1.00**

**Hésitations / ambiguïtés :** très faibles. La seule réserve est que la cohérence cérébrale est souvent métastable plutôt que fixe, mais cela confirme l’intégration dynamique plutôt que l’infirme.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                     |
| -------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | Oui : les sources évoquent explicitement attractor dynamics, états métastables et dynamiques récurrentes stabilisées.                                                                                                                                                             |
| N2 : Correction active d’écart               | 1     | Oui : le cerveau agit par boucles de contrôle sensorimoteur, estimation d’état, correction d’erreur, ajustements par feedback et apprentissage.                                                                                                                                   |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Présente mais moins directement explicite dans les sources réseau. On voit des priorités de maintien, de coordination, de sélection, de contrôle top-down, mais la hiérarchie régulatoire n’est pas formulée aussi nettement que dans un système homéostatique institutionnalisé. |
| N4 : Mécanisme interne de stabilisation      | 1     | Oui : récurrence, inhibition, synchronisation, équilibre modulaire, petits mondes, hubs et circuits d’intégration/stabilisation.                                                                                                                                                  |
| N5 : Résistance aux perturbations prolongées | 0.5   | Oui partiellement : le cerveau possède plasticité, redondance et compensation, mais il reste aussi vulnérable aux lésions, crises, dégénérescences et dysconnexions. Je mets 0.5 plutôt que 1.                                                                                    |

**Score A4 = 0.80**

**Hésitations / ambiguïtés :** c’est l’axe le plus dépendant du cadrage. Si on entend la normativité comme homéostasie fonctionnelle du cerveau vivant dans un organisme, A4 pourrait monter très haut. Si on la restreint au seul réseau neuronal comme architecture de connectivité, le 0.8 me paraît plus prudent.

**Distinction normativité endogène / imposée :** principalement **endogène**. Les mécanismes de stabilisation, de coordination, de plasticité et de correction sont internes au système nerveux; ils ne sont pas imposés de l’extérieur comme dans une institution. Mais cette normativité s’articule aussi à l’environnement, au corps et à l’expérience.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                           |
| -------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Oui : ajustements de poids synaptiques, excitabilité, modulation locale, tuning de réseaux.                                                                                                                                             |
| R2 : Modification durable de configuration interne | 1     | Oui : plasticité synaptique durable, mémoire, changements de connectivité liés à l’expérience.                                                                                                                                          |
| R3 : Reconfiguration de réseau ou de structure     | 1     | Oui : remodelage synaptique, réécriture de circuits, changements de structure de la matière blanche, croissance et réorganisation développementale.                                                                                     |
| R4 : Modification des mécanismes de régulation     | 1     | Oui : l’apprentissage modifie les modalités mêmes de traitement et de contrôle; la plasticité agit sur les circuits qui régulent ensuite la dynamique future.                                                                           |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | Oui partiellement : le réseau peut créer de nouvelles configurations fonctionnelles et de nouveaux schèmes de réponse, mais parler de « nouvelles règles » au sens fort reste plus inférentiel que directement établi dans les sources. |

**Score A5 = 0.90**

**Hésitations / ambiguïtés :** la principale hésitation porte sur R5. Le cerveau produit clairement de nouvelles configurations et routines, mais la formulation « nouvelles règles » est plus forte que « nouveaux patrons de connectivité ou de réponse ». D’où 0.5 plutôt que 1.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 1.00  |
| A2  | 1.00  |
| A3  | 1.00  |
| A4  | 0.80  |
| A5  | 0.90  |

### Lecture rapide

Le **réseau neuronal cérébral** apparaît ici comme un système :

- **très profondément hiérarchisé**,

- **très fortement propagatif**,

- **très fortement intégré**,

- **normatif de manière robuste mais moins “rigide” qu’un système homéostatique simple**,

- **hautement révisable par plasticité**.

### Profil global proposé

Le profil le plus marquant est celui d’un système **hautement intégré et hautement révisable**, avec **propagation forte**, **hiérarchie forte**, et **normativité élevée mais non absolue**. Il se distingue d’un système très normatif mais peu révisable par son caractère plastiquement reconfigurable. Cette combinaison ressort directement des descriptions de réentrée, hubs, modularité hiérarchique, synchronisation et plasticité structurelle/synaptique.


