# SYS007 — INTERNET BGP

## Identification

- **System ID :** SYS007

- **System name :** Internet BGP

- **Domain :** infrastructure / technological

- **Scale :** macro

- **Date scored :** 2026-04-02

- **Confidence globale :** medium-high

## Sources

1. RFC 1771, *A Border Gateway Protocol 4 (BGP-4)*.

2. Varadhan, Govindan, Estrin, *Persistent route oscillations in inter-domain routing* (2000).

3. van Beijnum, *BGP: Building Reliable Networks with the Border Gateway Protocol* (O’Reilly, 2002).

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                        |
| --------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | **1** | Le système articule au minimum des **pairs/sessions BGP** et des **AS** ; les routes sont échangées entre speakers mais sélectionnées dans un cadre inter-AS.                                                        |
| H2 : ≥ 3 niveaux causaux distincts            | **1** | On distingue au moins : **transport TCP/session**, **speaker BGP avec RIBs et décision**, **AS/politiques inter-domaines**. Le RFC sépare aussi Adj-RIBs-In, Loc-RIB et Adj-RIBs-Out.                                |
| H3 : ≥ 4 niveaux causaux distincts            | **1** | On peut identifier : transport TCP, messages BGP, structures internes du speaker (RIB/decision process), organisation intra-AS, réseau inter-AS global. Les fichiers montrent clairement ces couches fonctionnelles. |
| H4 : Niveaux fonctionnellement différenciés   | **1** | Les niveaux n’ont pas la même fonction : TCP assure la fiabilité, le speaker sélectionne, l’AS applique une politique, le système inter-AS assure l’acheminement global.                                             |
| H5 : Causalité bidirectionnelle entre niveaux | **1** | Les politiques locales déterminent les routes choisies, puis les effets globaux reviennent sur les speakers sous forme de mises à jour, retraits, oscillations ou changements de meilleur chemin.                    |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** faibles ; la hiérarchie est bien documentée.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score | Justification                                                                                                                                                                       |
| ------------------------------------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | **1** | Un changement de route chez un peer déclenche mise à jour, retrait ou remplacement, affectant les autres speakers.                                                                  |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | **1** | Une perturbation session/routage locale remonte au niveau AS puis au graphe inter-AS ; les phases de décision et diffusion relaient ces effets entre niveaux.                       |
| P3 : Propagation modifie l’état global observable             | **1** | Le meilleur chemin dans la Loc-RIB, puis les Adj-RIBs-Out et la FIB, changent ; à grande échelle cela peut produire des oscillations persistantes observables.                      |
| P4 : Isolement difficile sans modification structurelle       | **1** | L’article sur les oscillations montre qu’une politique locale peut créer des rétroactions distribuées ; le manuel évoque aussi les cascades de route flaps dans les grands réseaux. |
| P5 : Couplage fonctionnel non trivial                         | **1** | Le couplage dépend de la combinaison entre politiques locales, sélection indépendante des routes, AS_PATH, NEXT_HOP, MED, iBGP/eBGP.                                                |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** faibles.

---

## A3 — Intégration

| Sous-critère                             | Score   | Justification                                                                                                                                                                                                                                    |
| ---------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| I1 : Mécanisme explicite de coordination | **1**   | Oui : décision en trois phases, RIBs distinctes, keepalives, notifications, sessions internes/externes.                                                                                                                                          |
| I2 : Réduction de variance observable    | **0.5** | BGP réduit la multiplicité des routes en sélectionnant un meilleur chemin pour la Loc-RIB, mais cette réduction reste partielle car le système peut rester instable sous certaines politiques.                                                   |
| I3 : Synchronisation multi-niveaux       | **0.5** | Il existe une coordination entre speakers d’un même AS et entre BGP et IGP pour présenter une vue cohérente, mais pas de synchronisation globale forte ; le RFC insiste justement sur les précautions nécessaires pour garder une vue cohérente. |
| I4 : Boucles de rétroaction globales     | **1**   | Très net : les oscillations persistantes décrites par Varadhan et al. sont précisément des boucles de rétroaction globales dues aux politiques inter-dépendantes.                                                                                |
| I5 : Maintien d'un état global cohérent  | **0.5** | Le système vise la cohérence, mais elle n’est pas garantie pour toutes les politiques ; le RFC pose une architecture de cohérence locale/intra-AS, tandis que l’article montre des cas de non-convergence.                                       |

**Score A3 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** la note dépend surtout du poids qu’on donne aux cas pathologiques de non-convergence.

---

## A4 — Normativité

| Sous-critère                                 | Score   | Justification                                                                                                                                                                                                                     |
| -------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | **1**   | Le système cherche un ensemble de meilleurs chemins stables via la décision locale et la diffusion des routes ; il possède bien des attracteurs, même s’ils ne sont pas toujours uniques ni stables.                              |
| N2 : Correction active d'écart               | **1**   | Retraits, remplacements de routes, keepalive, notification, recalcul de préférence : le système corrige activement les écarts entre état courant et état routable.                                                                |
| N3 : Hiérarchie de priorités régulatoires    | **1**   | Très explicite : degré de préférence, LOCAL_PREF, AS_PATH, MED, coût interne vers NEXT_HOP, puis tie-breakers.                                                                                                                    |
| N4 : Mécanisme interne de stabilisation      | **1**   | Le protocole intègre sélection, pruning des boucles, messages de contrôle ; en exploitation, on ajoute aussi flap dampening, route reflectors, confederations pour stabiliser et scaler.                                          |
| N5 : Résistance aux perturbations prolongées | **0.5** | Résistance réelle mais incomplète : le système peut absorber beaucoup de changements, cependant les oscillations persistantes et cascades de flaps montrent une fragilité structurelle sous certaines politiques ou instabilités. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** la robustesse est forte en pratique, mais pas universelle en théorie.

**Distinction normativité endogène / imposée :**  
La normativité est en grande partie **endogène au protocole et à l’architecture de décision** : préférence, sélection, diffusion, tie-breaks, structures RIB. Mais une part importante est aussi **imposée ou configurée localement** par les opérateurs via les politiques.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score   | Justification                                                                                                                                                                                              |
| -------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | **1**   | Oui : politiques locales, préférences, MED, timers, filtres, dampening.                                                                                                                                    |
| R2 : Modification durable de configuration interne | **1**   | Les configurations BGP modifient durablement la sélection et la propagation des routes. Le manuel montre des réglages stables de confédération, dampening, sessions iBGP/eBGP.                             |
| R3 : Reconfiguration de réseau ou de structure     | **1**   | Oui : route reflectors, confederations, changements de peering et de topologie de contrôle modifient la structure du système.                                                                              |
| R4 : Modification des mécanismes de régulation     | **0.5** | Partiellement : on peut modifier les filtres, préférences et dispositifs de stabilisation, mais la logique fondamentale du protocole n’est pas reconfigurée par le système lui-même.                       |
| R5 : Capacité à produire de nouvelles règles       | **0**   | Les sources montrent surtout des **règles préconfigurées** par opérateurs et politiques externes ; je ne vois pas de capacité endogène du système BGP à générer lui-même de nouvelles règles régulatoires. |

**Score A5 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** c’est l’axe le plus ambigu, car tout dépend de ce qu’on inclut dans le système : protocole seul ou sociotechnique protocole + opérateurs.

---

## Synthèse

| Axe | Score    |
| --- | -------- |
| A1  | **1.00** |
| A2  | **1.00** |
| A3  | **0.70** |
| A4  | **0.90** |
| A5  | **0.70** |

### Gradients

| Gradient      | Valeur   |
| ------------- | -------- |
| Δ₂₃ = A2 − A3 | **0.30** |
| Δ₄₅ = A4 − A5 | **0.20** |
| Δ₁₂ = A1 − A2 | **0.00** |
| Δ₃₅ = A3 − A5 | **0.00** |
| Δ₄₃ = A4 − A3 | **0.20** |

## Lecture rapide

Le profil qui ressort est celui d’un système **très hiérarchisé**, **très propagatif**, **fortement normé**, mais dont l’intégration globale reste **imparfaite** parce qu’elle repose sur des politiques locales indépendantes pouvant produire de la non-convergence. La révision est **réelle mais surtout configurative**, donc moins endogène qu’au sein d’un système auto-adaptatif fort. Cela ressort très clairement du contraste entre le RFC, qui formalise une architecture de décision et de diffusion très structurée, et l’article sur les oscillations, qui montre que cette structure ne suffit pas à garantir la convergence sous toutes les politiques.


