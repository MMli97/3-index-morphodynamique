# Scoring Notes — [SYS002] Global supply chain

## Identification

- **System ID :** SYS002

- **System name :** Global supply chain

- **Domain :** economic / infrastructure

- **Scale :** macro

- **Date scored :** 2026-04-03

- **Confidence globale :** High

## Sources

1. Christopher, M. — Logistics and Supply Chain Management

2. Chopra, S. & Meindl, P. — Supply Chain Management

3. Sheffi, Y. — The Resilient Enterprise

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                                     |
| --------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1.0       | Les chaînes d'approvisionnement comportent l'entreprise focale et ses relations directes avec ses fournisseurs ou clients.                                                            |
| H2 : ≥ 3 niveaux causaux distincts            | 1.0       | Le réseau d'approvisionnement comprend de multiples étapes interconnectées, par exemple : usines, assembleurs et distributeurs.                                                       |
| H3 : ≥ 4 niveaux causaux distincts            | 1.0       | Une chaîne complète inclut de façon typique : les fournisseurs de composants/matières premières, les fabricants, les grossistes/distributeurs, les détaillants et les clients finaux. |
| H4 : Niveaux fonctionnellement différenciés   | 1.0       | Les divers niveaux de la chaîne ont des rôles fonctionnels très distincts tels que l'extraction, la fabrication, la distribution et la vente au détail.                               |
| H5 : Causalité bidirectionnelle entre niveaux | 1.0       | Les flux de produits physiques descendent généralement la chaîne, tandis que les informations sur la demande et les fonds financiers la remontent.                                    |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune. La profondeur hiérarchique d'une chaîne logistique mondiale moderne est structurellement établie à plus de 4 niveaux.

---

## A2 — Capacité de propagation

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                                                           |
| ------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1.0       | Un incendie mineur dans une usine de puces Philips à Albuquerque a causé des dommages matériels qui ont directement perturbé l'approvisionnement de multiples autres entreprises.           |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1.0       | Une défaillance au niveau d'une usine locale remonte la hiérarchie pour atteindre la production de l'assembleur final (Nokia, Ericsson) puis affecter les consommateurs.                    |
| P3 : Propagation modifie l'état global observable             | 1.0       | L'incendie chez Philips a causé de graves pénuries pour Ericsson, ce qui a entraîné sa sortie du marché des téléphones portables et modifié la répartition globale des parts de marché.     |
| P4 : Isolation est difficile sans modification structurelle   | 1.0       | Les opérations à flux tendus ont supprimé les stocks de sécurité tampons, rendant la chaîne très vulnérable aux propagations de chocs sans que l'on y ajoute de la redondance structurelle. |
| P5 : Couplage fonctionnel non-trivial                         | 1.0       | Les chaînes mondiales constituent une toile complexe de nœuds interconnectés, et ces fortes dépendances croisées exacerbent la difficulté à contenir les chocs.                             |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune. Les sources décrivent parfaitement la façon dont un incident mineur et localisé a le potentiel de se propager de manière systémique.

---

## A3 — Intégration

| **Sous-critère**                                  | **Score** | **Justification**                                                                                                                                                      |
| ------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme de coordination explicite existant | 0.5       | Des mécanismes d'intégration existent (ex. CPFR, partage d'informations), mais cette intégration échoue très souvent en raison d'obstacles comportementaux.            |
| I2 : Réduction de la variance observable          | 0.0       | Conformément aux instructions critiques : le système amplifie la variance de la demande en amont via l'effet coup de fouet.                                            |
| I3 : Synchronisation multi-niveaux                | 0.5       | Bien que la synchronisation multi-niveaux soit un objectif, elle reste particulièrement difficile à atteindre globalement face à l'incertitude.                        |
| I4 : Boucles de rétroaction globales              | 0.5       | Des boucles de rétroaction et des signaux de demande existent, mais ils subissent de graves distorsions lorsqu'ils traversent la chaîne.                               |
| I5 : Maintien d'un état global cohérent           | 0.5       | Conformément aux instructions critiques : les entreprises individuelles tendent à optimiser leurs résultats localement, ce qui sabote la cohérence globale du système. |

**Score A3 = 0.40 / 1.00**

**Hésitations / ambiguïtés :** Les instructions strictes forcent une notation sanctionnant l'intégration (A3 représente l'intégration défaillante due à l'effet coup de fouet et aux optimisations purement locales).

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                                             |
| -------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1.0       | L'attracteur dynamique central du système est l'équilibre consistant à faire correspondre l'offre à la demande, tout en trouvant le juste point entre réactivité et efficacité.               |
| N2 : Correction active d'écart               | 1.0       | Le système utilise des leviers managériaux tels que l'ajustement des stocks de sécurité et des capacités de production pour corriger activement les erreurs de prévision.                     |
| N3 : Hiérarchie de priorités régulatoires    | 0.5       | Idéalement, la stratégie concurrentielle devrait dicter la stratégie logistique, mais l'alignement échoue régulièrement lorsque les fonctions poursuivent des objectifs financiers distincts. |
| N4 : Mécanisme interne de stabilisation      | 0.5       | Bien que les stocks de sécurité agissent comme stabilisateurs, ces mécanismes sont de plus en plus supprimés par la recherche d'efficacité, fragilisant l'ensemble.                           |
| N5 : Résistance aux perturbations prolongées | 0.5       | Lors de perturbations longues, certains acteurs s'effondrent et sont éliminés du marché (comme Ericsson), bien que d'autres entreprises très résilientes (comme Nokia) puissent s'adapter.    |

**Score A4 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** La réduction des tampons de sécurité affaiblit fortement la résilience interne du système.

---

## A5 — Capacité de révision

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                                 |
| -------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1.0       | Les opérateurs modifient continuellement les prix, modifient les niveaux de stock de sécurité, et revoient les tailles de lots.                                   |
| R2 : Modification durable de configuration interne | 1.0       | Les chaînes procèdent à des changements profonds comme l'externalisation de la production et le report de la différenciation des produits finaux.                 |
| R3 : Reconfiguration de réseau ou de structure     | 1.0       | La conception des réseaux logistiques permet l'ouverture, la fermeture d'usines, ainsi que la restructuration totale du circuit de distribution.                  |
| R4 : Modification des mécanismes de régulation     | 1.0       | Le système est capable de passer de règles d'optimisation purement locales à de nouveaux protocoles de collaboration et de partage des risques inter-entreprises. |
| R5 : Capacité à produire de nouvelles règles       | 1.0       | Les entreprises refaçonnent complètement leurs stratégies pour survivre, comme Dell passant des ventes directes au modèle de la grande distribution.              |

**Score A5 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Les chaînes logistiques globales, sous pression darwinienne constante, font preuve d'une excellente plasticité et capacité de révision systémique.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 1.00      |
| A2      | 1.00      |
| A3      | 0.40      |
| A4      | 0.70      |
| A5      | 1.00      |

**Confidence globale :** High
