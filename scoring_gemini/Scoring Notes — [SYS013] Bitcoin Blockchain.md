# Scoring Notes — [SYS013] Bitcoin Blockchain

## Identification

- **System ID :** SYS013

- **System name :** Réseau et Protocole Bitcoin (Bitcoin Blockchain)

- **Domain :** technological / economic

- **Scale :** macro

- **Date scored :** 2026-04-01

- **Scorer :** Gemini

- **Confidence globale :** high

## Sources

1. Bitcoin: A Peer-to-Peer Electronic Cash System (Satoshi Nakamoto)

2. Bitcoin and Cryptocurrency Technologies: A Comprehensive Introduction (Narayanan et al.)

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                                       |
| --------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | Le système repose sur une couche réseau de diffusion pair-à-pair (P2P) et une couche de consensus par Preuve de Travail (Proof-of-Work).                                                |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | Il intègre également une couche applicative pour l'état du registre, gérée via le modèle des sorties de transactions non dépensées (UTXO) et un langage de script.                      |
| H3 : ≥ 4 niveaux causaux distincts            | 0.5       | Une couche socio-économique (mineurs, développeurs, plateformes d'échange) influence le réseau, bien que cette gouvernance et ces interactions se produisent "off-chain" (hors chaîne). |
| H4 : Niveaux fonctionnellement différenciés   | 1         | Les rôles sont distincts : les nœuds relaient les informations, les mineurs hachent les en-têtes de blocs pour sécuriser le réseau, et les utilisateurs signent des transactions.       |
| H5 : Causalité bidirectionnelle entre niveaux | 1         | La puissance de calcul matérielle sécurise le registre logiciel (bottom-up), tandis que le protocole ajuste la difficulté, dictant la rentabilité économique du matériel (top-down).    |

**Score A1 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** L'évaluation de H3 est pondérée à 0.5 car la couche de gouvernance (communauté, développeurs Core) est indispensable à la maintenance du système, mais elle n'est pas codée directement dans le protocole lui-même.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                                       |
| ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | Des retards dans la propagation des blocs sur le réseau P2P peuvent augmenter le taux de blocs orphelins et provoquer des bifurcations temporaires (forks).             |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | Une congestion des transactions en attente modifie le marché des frais de transaction, affectant les incitations économiques des mineurs.                               |
| P3 : Propagation modifie l'état global observable             | 1         | Chaque bloc validé et ajouté à la chaîne propage une mise à jour globale et permanente du registre des UTXO.                                                            |
| P4 : Isolement difficile sans modification structurelle       | 1         | Un nœud déconnecté perd le consensus ; à sa reconnexion, il doit télécharger et accepter la chaîne la plus longue pour se resynchroniser avec le réseau.                |
| P5 : Couplage fonctionnel non trivial                         | 1         | Les blocs sont liés cryptographiquement par des pointeurs de hachage ; modifier un ancien bloc nécessite de refaire la Preuve de Travail de tous les blocs subséquents. |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune. Le protocole est conçu pour qu'une information valide se propage de manière virale à tous les nœuds participants.

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                                                 |
| ---------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1         | La règle de la chaîne la plus longue, combinée à la Preuve de Travail, sert de mécanisme de coordination pour un réseau décentralisé sans confiance préalable.    |
| I2 : Réduction de variance observable    | 1         | Un algorithme d'ajustement de la difficulté cible un temps moyen de 10 minutes entre chaque bloc, compensant les fluctuations de la puissance de hachage globale. |
| I3 : Synchronisation multi-niveaux       | 1         | Tous les nœuds complets (full nodes) valident indépendamment chaque transaction et bloc pour maintenir une copie identique et synchronisée du registre.           |
| I4 : Boucles de rétroaction globales     | 1         | L'ajustement de la difficulté tous les 2016 blocs constitue une boucle de rétroaction globale parfaite pour stabiliser l'émission monétaire.                      |
| I5 : Maintien d'un état global cohérent  | 1         | Les règles du réseau préviennent cryptographiquement le problème de la double dépense et assurent l'intégrité absolue de l'historique.                            |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Le système représente le paradigme même de l'intégration distribuée d'un état global.

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                      |
| -------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1         | La chaîne valide accumulant le plus grand effort de Preuve de Travail agit comme l'attracteur vers lequel convergent systématiquement les nœuds honnêtes.              |
| N2 : Correction active d'écart               | 1         | Les nœuds rejettent activement tout bloc ou transaction qui enfreint les règles de consensus (ex. fausse signature, récompense de bloc incorrecte).                    |
| N3 : Hiérarchie de priorités régulatoires    | 1         | Les règles de consensus du protocole priment sur les préférences individuelles des nœuds ou la volonté d'un mineur isolé.                                              |
| N4 : Mécanisme interne de stabilisation      | 1         | Le système utilise des incitations économiques (création monétaire et frais de transaction) pour encourager les mineurs à rester honnêtes et à sécuriser le réseau.    |
| N5 : Résistance aux perturbations prolongées | 1         | Le système est conçu de telle sorte qu'une attaque des 51% est économiquement dissuasive, car l'attaquant détruirait la valeur du système qu'il tente de compromettre. |

**Score A4 = 1.00 / 1.00**

**Distinction normativité endogène / imposée :** La normativité est endogène car elle s'auto-entretient par un équilibre de théorie des jeux, bien que les règles initiales aient été gravées dans le code par son créateur.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                                                                        |
| -------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1         | Les paramètres quantitatifs s'ajustent (la difficulté de minage s'adapte automatiquement et les frais de transaction fluctuent selon l'offre et la demande d'espace dans les blocs).                     |
| R2 : Modification durable de configuration interne | 0.5       | Le système accepte des "soft forks" qui restreignent les règles de manière rétrocompatible (ex: Pay-to-Script-Hash), mais cela requiert une action externe coordonnée des mineurs.                       |
| R3 : Reconfiguration de réseau ou de structure     | 0.5       | La topologie du réseau P2P est fluide, les nœuds pouvant rejoindre ou quitter à volonté, mais la structure de données sous-jacente reste strictement inaltérable.                                        |
| R4 : Modification des mécanismes de régulation     | 0         | Le protocole ne peut pas altérer ses propres règles fondamentales (comme la limite d'émission) de manière endogène ; une telle modification exige un "hard fork" impliquant un consensus social externe. |
| R5 : Capacité à produire de nouvelles règles       | 0         | Le système est déterministe et n'a aucune capacité générative interne pour créer de nouvelles règles opérationnelles.                                                                                    |

**Score A5 = 0.40 / 1.00**

**Hésitations / ambiguïtés :** L'incapacité du système à réviser ses propres règles fondamentales de manière autonome est une fonctionnalité de sécurité délibérée ("ossification"), et non un bug.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 0.90      |
| A2      | 1.00      |
| A3      | 1.00      |
| A4      | 1.00      |
| A5      | 0.40      |

### Gradients (calculés)

| **Gradient**  | **Valeur** |
| ------------- | ---------- |
| Δ₂₃ = A2 − A3 | 0.00       |
| Δ₄₅ = A4 − A5 | 0.60       |
| Δ₁₂ = A1 − A2 | -0.10      |
| Δ₃₅ = A3 − A5 | 0.60       |
| Δ₄₃ = A4 − A3 | 0.00       |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système Cybernétique Déterministe / Registre Homéostatique Rigide.

- **Régime secondaire :** Écosystème Socio-Technique (par l'influence humaine "hors-chaîne" sur les forks).

- **Marge :** Le système excelle dans la propagation (A2), l'intégration (A3) et la normativité (A4) au détriment volontaire de sa propre plasticité (A5).

- **Surprise par rapport au jugement intuitif :** Les gradients (notamment Δ₄₅ = 0.60) démontrent mathématiquement à quel point le système privilégie la stabilisation stricte et inaltérable plutôt que l'adaptation évolutive interne.

---

## Notes libres

La consultation des sources confirme que Bitcoin a été conçu architecturalement pour maximiser la sécurité et la prévisibilité. Le livre blanc se concentre massivement sur la résolution cryptographique et probabiliste de l'intégration et de la normativité (A3 et A4). Le manuel académique met en évidence que la rigidité du système (faible A5) est ce qui fonde sa valeur économique en tant que protocole sans confiance.
