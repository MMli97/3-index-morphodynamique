

# Scoring Notes — SYS013 BITCOIN BLOCKCHAIN

## Identification

- **System ID :** SYS013

- **System name :** Bitcoin blockchain

- **Domain :** technological

- **Subdomain :** distributed ledger / cryptocurrency infrastructure

- **Scale :** macro

- **Date scored :** 2026-04-02

- **Scorer :** Noé

- **Confidence globale :** medium-high

## Sources

1. Satoshi Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System*

2. Arvind Narayanan et al., *Bitcoin and Cryptocurrency Technologies*

3. Template de scoring fourni par l’utilisateur

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Au minimum, le système articule transactions et blocs, les transactions étant agrégées dans des blocs.                                                                                                                       |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | On peut distinguer transactions, blocs, puis chaîne la plus longue comme niveau de validation historique.                                                                                                                    |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | Un quatrième niveau apparaît avec les nœuds/miners et la couche d’incitation/proof-of-work qui conditionne la production des blocs et donc l’état global du registre.                                                        |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les transactions transfèrent la valeur, les blocs ordonnent et scellent localement, la chaîne longue stabilise l’histoire globale, les mineurs assurent sélection/proposition par travail et incitations.                    |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | Les nœuds/miners produisent la chaîne via le proof-of-work, mais la chaîne et la difficulté ajustée modifient en retour les comportements et coûts de minage ; la structure globale rétroagit donc sur le niveau opératoire. |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Le point le plus discutable est H5 : la bidirectionnalité est nette si l’on inclut la difficulté, les récompenses et l’état de la chaîne dans le niveau supérieur ; elle l’est moins si l’on réduit le système à une pure séquence technique de blocs.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                    |
| ------------------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une transaction ou un bloc reçu localement modifie les mempools voisins et peut influencer le choix du prochain bloc.                                                                                            |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Une perturbation locale passe du niveau transactionnel au niveau bloc, puis au niveau chaîne consensuelle.                                                                                                       |
| P3 : Propagation modifie l'état global observable             | 1     | L’inclusion d’un bloc dans la chaîne la plus longue modifie l’état global du ledger et l’état reconnu des UTXO/confirmations.                                                                                    |
| P4 : Isolement difficile sans modification structurelle       | 1     | Le réseau diffuse en best effort à tous les nœuds ; les blocs et transactions se propagent largement et l’isolement réel supposerait une intervention structurelle sur le réseau ou une domination de hashpower. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage entre propagation réseau, validation locale, minage, confirmations et sélection par chaîne la plus longue est central et irréductible à un simple pipeline linéaire.                                 |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Le réseau n’est pas parfaitement couplé : il est explicitement “best effort” et tolère des messages manqués. Mais cela ne réduit pas la forte capacité de propagation ; cela en est plutôt la modalité concrète.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                           |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | La coordination est explicite : validation des transactions, preuve de travail, puis extension de la chaîne la plus longue.                                                                             |
| I2 : Réduction de variance observable    | 1     | Les désaccords locaux sur transactions conflictuelles ou blocs concurrents sont résolus par inclusion dans un bloc puis par convergence vers la branche longue ; les autres blocs deviennent orphelins. |
| I3 : Synchronisation multi-niveaux       | 1     | Il y a synchronisation entre propagation réseau, validation transactionnelle, agrégation en blocs, puis consensus probabiliste sur la chaîne.                                                           |
| I4 : Boucles de rétroaction globales     | 1     | La difficulté est réajustée selon le rythme global de création de blocs ; les récompenses et coûts de minage réinjectent aussi une rétroaction systémique.                                              |
| I5 : Maintien d'un état global cohérent  | 1     | Le système maintient un ledger consensuel probabiliste : la propriété de confirmation croissante rend l’histoire globale de plus en plus stable.                                                        |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
La cohérence n’est pas instantanée ni absolue : elle est probabiliste et passe par confirmations successives. Mais pour un scoring morphodynamique, cela reste une intégration très forte.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                                                                  |
| -------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1 : Attracteur dynamique existant           | 1     | L’attracteur principal est la chaîne valide la plus longue / avec le plus de proof-of-work, vers laquelle convergent les nœuds.                                                                                                                                                |
| N2 : Correction active d'écart               | 1     | Les nœuds rejettent les transactions invalides ou déjà dépensées, abandonnent les branches plus courtes et basculent quand une branche devient dominante.                                                                                                                      |
| N3 : Hiérarchie de priorités régulatoires    | 0.5   | Il existe bien un ordre implicite : validité cryptographique et non-double-spend d’abord, puis règle de la chaîne la plus longue, puis incitations par fees/récompenses. Mais cette hiérarchie est relativement compacte, moins stratifiée que dans un système institutionnel. |
| N4 : Mécanisme interne de stabilisation      | 1     | Proof-of-work, règle de la chaîne la plus longue, confirmations et ajustement de difficulté forment un noyau stabilisateur interne.                                                                                                                                            |
| N5 : Résistance aux perturbations prolongées | 0.5   | La résistance est réelle tant que la majorité de puissance de calcul reste honnête ; mais elle est conditionnelle et vulnérable à une prise de majorité hashpower.                                                                                                             |

**Score A4 = 0.80 / 1.00**

**Hésitations / ambiguïtés :**  
Le score de N5 pourrait être monté à 1 si l’on score la robustesse “dans ses hypothèses nominales”. Je le laisse à 0.5 car la robustesse reste explicitement conditionnée à la majorité honnête de puissance de calcul.

**Distinction normativité endogène / imposée :**  
La normativité est **largement endogène** au niveau opératoire : validité des transactions, sélection de la chaîne, difficulté, incitations. En revanche, la modification des règles fondamentales du protocole reste en pratique **partiellement exogène**, portée par la couche sociale et logicielle des développeurs, nœuds et mineurs.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                      |
| -------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| R1 : Ajustement paramétrique local                 | 1     | Le système ajuste un paramètre crucial, la difficulté de proof-of-work, en fonction du rythme observé de production des blocs.                                                                                     |
| R2 : Modification durable de configuration interne | 1     | Chaque nouveau bloc modifie durablement l’état de la chaîne et l’ensemble des sorties dépensables ; la configuration interne du ledger est continuellement révisée.                                                |
| R3 : Reconfiguration de réseau ou de structure     | 0.5   | Il y a une certaine reconfiguration via forks, orphelins, arrivée/départ de nœuds et recomposition de la branche active, mais l’architecture de base reste assez rigide.                                           |
| R4 : Modification des mécanismes de régulation     | 0.5   | Les mécanismes économiques évoluent partiellement de l’intérieur via la montée relative des frais quand la récompense décroît ; mais la logique fondamentale de régulation n’est pas auto-réécrite par le système. |
| R5 : Capacité à produire de nouvelles règles       | 0     | Le système ne génère pas de nouvelles règles protocolaires de façon endogène ; les changements de règles relèvent d’une coordination socio-technique externe au ledger lui-même.                                   |

**Score A5 = 0.60 / 1.00**

**Hésitations / ambiguïtés :**  
R2 dépend de la lecture retenue : si l’on réserve “révision” à une plasticité des mécanismes régulateurs eux-mêmes, il faudrait le baisser. Je l’ai gardé à 1 parce que l’état interne du système est durablement reconfiguré à chaque bloc, ce qui constitue bien une modification interne persistante.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 1.00  |
| A2  | 1.00  |
| A3  | 1.00  |
| A4  | 0.80  |
| A5  | 0.60  |

### Gradients

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.00   |
| Δ₄₅ = A4 − A5 | 0.20   |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | 0.40   |
| Δ₄₃ = A4 − A3 | -0.20  |

### Classification

- **Régime primaire :** à remplir après passage dans votre classifieur

- **Régime secondaire :** à remplir après passage dans votre classifieur

- **Marge :** non calculée ici

- **Surprise par rapport au jugement intuitif :** faible ; le système apparaît très intégré, très propagatif, fortement normé, mais seulement moyennement plastique au niveau de ses règles internes.

---

## Notes libres

Le profil qui ressort est celui d’un système **très fortement intégré et coordonné**, mais dont la **plasticité endogène** reste limitée. Bitcoin sait très bien stabiliser une histoire commune et corriger les écarts tant que ses hypothèses de sécurité tiennent ; en revanche, il ne sait pas vraiment se refonder lui-même de l’intérieur. Sa révision profonde dépend d’une couche socio-technique extérieure au mécanisme strict de consensus. Cela tend à produire un système très robuste dans son régime nominal, mais relativement rigide au niveau métarégulatoire.


