# SYS008 — Banque centrale européenne

## Identification

- **System ID :** SYS008

- **System name :** Banque centrale européenne

- **Domain :** institutional

- **Subdomain :** institution monétaire supranationale

- **Scale :** macro

- **Date scored :** 2026-04-02

- **Scorer :** GPT

- **Confiance globale :** medium

## Sources

1. *The Birth of the Euro*, Otmar Issing.

2. *Economics of Monetary Union*, Paul De Grauwe.

3. *Whatever it takes. Mario Draghi in parole sue*.

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                                    |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1     | Au minimum, on a un niveau central BCE/Conseil des gouverneurs et un niveau des banques centrales nationales chargées aussi de la mise en œuvre.                                                                                                                 |
| H2 : ≥ 3 niveaux causaux distincts            | 1     | On distingue au moins : Conseil des gouverneurs, Directoire/Executive Board, BCN nationales ; De Grauwe décrit explicitement décision puis implémentation.                                                                                                       |
| H3 : ≥ 4 niveaux causaux distincts            | 1     | On peut ajouter les marchés financiers et, dans le cadre élargi, les nouvelles autorités de supervision européennes / mécanismes de banking union, qui interagissent causalement avec la BCE.                                                                    |
| H4 : Niveaux fonctionnellement différenciés   | 1     | Les fonctions sont nettement différenciées : formulation de la politique monétaire, mise à l’agenda, implémentation via BCN, supervision macroprudentielle et bancaire à partir des réformes post-crise.                                                         |
| H5 : Causalité bidirectionnelle entre niveaux | 1     | La structure n’est pas purement descendante : les BCN siègent au Conseil des gouverneurs et participent à la décision, tandis que la décision centrale est ensuite implémentée par ces mêmes BCN. Il y a donc remontée d’information et descente d’instructions. |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Le quatrième niveau causal est moins “organiquement” stabilisé que les trois premiers si l’on restreint strictement le système à la BCE au sens juridique étroit. Le 1 ici suppose qu’on score la BCE opératoire dans l’Eurosystème et son environnement institutionnel immédiat.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score | Justification                                                                                                                                                                                                              |
| ------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1     | Une tension sur un compartiment (marché obligataire souverain, crise bancaire, inflation, crise de liquidité) affecte immédiatement décision monétaire, supervision, transmission, et BCN.                                 |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1     | Les décisions du Conseil se transmettent aux BCN ; inversement, les conditions nationales et financières pèsent sur la délibération du Conseil.                                                                            |
| P3 : Propagation modifie l’état global observable             | 1     | Les décisions BCE modifient les taux, la liquidité, les spreads souverains, la stabilité financière et les conditions macroéconomiques à l’échelle de la zone euro. L’exemple OMT est typique.                             |
| P4 : Isolement difficile sans modification structurelle       | 1     | De Grauwe insiste précisément sur l’interdépendance systémique d’une union monétaire incomplète, et sur le fait que les crises souveraines et bancaires se propagent difficilement sans changement institutionnel profond. |
| P5 : Couplage fonctionnel non trivial                         | 1     | Le couplage entre politique monétaire, marchés obligataires, supervision, moral hazard, gouvernance budgétaire et banking union est hautement non trivial.                                                                 |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Aucune majeure. La BCE est clairement un système à très forte propagation transversale.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                                                   |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1     | Le mécanisme de coordination est formel : Conseil des gouverneurs, Directoire, Eurosystème, réunions régulières, chaîne décision/implémentation.                                                                                |
| I2 : Réduction de variance observable    | 0.5   | La BCE vise explicitement la stabilité des prix et la réduction des divergences déstabilisantes, mais les sources montrent aussi la persistance de fortes asymétries intra-zone et les limites de l’union monétaire incomplète. |
| I3 : Synchronisation multi-niveaux       | 1     | Il existe une synchronisation entre niveau central, BCN, marchés monétaires et dispositifs prudentiels ; la politique unique suppose justement cette coordination multi-niveaux.                                                |
| I4 : Boucles de rétroaction globales     | 1     | Les rétroactions sont manifestes : marchés → BCE → États/banques → marchés ; en crise, la BCE réagit à l’élargissement des spreads et modifie le système.                                                                       |
| I5 : Maintien d’un état global cohérent  | 1     | Malgré tensions et critiques, le système maintient un état monétaire commun cohérent : une politique monétaire unique, une cible de stabilité et une capacité de maintien de l’intégrité de l’euro.                             |

**Score A3 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
Le 0.5 en I2 vient du fait que l’intégration réduit certaines variances nominales, mais ne résorbe pas automatiquement les divergences réelles, budgétaires ou bancaires.

---

## A4 — Normativité

| Sous-critère                                 | Score | Justification                                                                                                                                                                                                                   |
| -------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1     | L’attracteur central est explicite : la stabilité des prix, formulée comme objectif primaire.                                                                                                                                   |
| N2 : Correction active d’écart               | 1     | La BCE ajuste activement ses taux, sa liquidité et ses instruments non conventionnels pour corriger les écarts perçus à son mandat ou à la transmission de la politique monétaire.                                              |
| N3 : Hiérarchie de priorités régulatoires    | 1     | Les textes soulignent une hiérarchie nette : priorité à la stabilité des prix, autres objectifs subordonnés.                                                                                                                    |
| N4 : Mécanisme interne de stabilisation      | 1     | Conseil des gouverneurs, stratégie monétaire, open market operations, cadres prudentiels et, en crise, OMT/mesures non conventionnelles.                                                                                        |
| N5 : Résistance aux perturbations prolongées | 1     | La BCE a résisté à des perturbations prolongées majeures : crise financière, crise des dettes souveraines, fragmentation financière ; les sources insistent sur le rôle décisif de l’OMT et des instruments non conventionnels. |

**Score A4 = 1.00 / 1.00**

**Hésitations / ambiguïtés :**  
Aucune majeure : c’est probablement l’axe le plus élevé du système.

**Distinction normativité endogène / imposée :**  
Normativité **majoritairement endogène institutionnalisée**, mais juridiquement enchâssée par le traité. Elle n’est donc ni purement auto-produite ni purement externe : elle est intériorisée dans l’architecture décisionnelle.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score | Justification                                                                                                                                                                                                                                             |
| -------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1     | Changement des taux, modulation de la liquidité, réglages opérationnels : évident.                                                                                                                                                                        |
| R2 : Modification durable de configuration interne | 1     | Les pratiques de transparence évoluent, par exemple la publication des minutes à partir de 2015 selon De Grauwe.                                                                                                                                          |
| R3 : Reconfiguration de réseau ou de structure     | 1     | Après 2008, refonte de la supervision et montée vers une banking union ; la BCE acquiert de nouvelles responsabilités structurantes.                                                                                                                      |
| R4 : Modification des mécanismes de régulation     | 1     | OMT, quantitative easing, rôle de prêteur en dernier ressort de facto sur les marchés souverains : ce sont des inflexions majeures du régime de régulation.                                                                                               |
| R5 : Capacité à produire de nouvelles règles       | 0.5   | La BCE peut produire de nouvelles doctrines, procédures et cadres opérationnels, mais reste contrainte par le traité et n’a pas une souveraineté constituante complète. Elle révise fortement les pratiques sans refonder seule l’ordre juridique global. |

**Score A5 = 0.90 / 1.00**

**Hésitations / ambiguïtés :**  
R5 pourrait être mis à 1 si l’on interprète “nouvelles règles” de manière fonctionnelle plutôt que constituante. Je reste à 0.5 car la BCE innove puissamment, mais dans des bornes juridiques et politiques qui ne dépendent pas d’elle seule.

---

## Synthèse

| Axe | Score |
| --- | ----- |
| A1  | 1.00  |
| A2  | 1.00  |
| A3  | 0.90  |
| A4  | 1.00  |
| A5  | 0.90  |

### Gradients

| Gradient      | Valeur |
| ------------- | ------ |
| Δ₂₃ = A2 − A3 | 0.10   |
| Δ₄₅ = A4 − A5 | 0.10   |
| Δ₁₂ = A1 − A2 | 0.00   |
| Δ₃₅ = A3 − A5 | 0.00   |
| Δ₄₃ = A4 − A3 | 0.10   |

### Lecture rapide

Le profil est celui d’un système **très structuré, fortement propagatif, très normatif, hautement intégré mais imparfaitement unifié, et révisable de manière importante sans être pleinement auto-constituant**. Les sources convergent sur un point : la BCE est une architecture institutionnelle exceptionnellement robuste, mais opérant dans une union monétaire incomplète, ce qui limite partiellement l’intégration et la révision systémique complète.

### Classification

- **Régime primaire :** normativité intégrée à haute cohérence

- **Régime secondaire :** architecture institutionnelle révisable mais juridiquement contrainte

- **Marge :** faible à moyenne, car A1/A2/A4 sont très clairement élevés, mais la frontière A3/A5 dépend de la définition stricte du périmètre “BCE seule” ou “BCE opératoire dans l’Eurosystème”

- **Surprise par rapport au jugement intuitif :** faible ; le point peut surprendre seulement sur A5, qui ressort plus élevé qu’une intuition “institution rigide” ne le laisserait penser, en raison des révisions post-crise, de l’OMT, du QE, et de l’extension prudentielle.

## Notes libres

Deux points me paraissent importants pour l’interprétation morphodynamique :

D’abord, **la BCE a une normativité très forte sans être un système totalement autosuffisant**. Les textes de De Grauwe insistent sur la fragilité d’une union monétaire sans union budgétaire complète ; cela signifie que la puissance normative de la BCE coexiste avec une dépendance structurelle à un environnement politique inachevé.

Ensuite, **la capacité de révision existe surtout sous forme d’innovation doctrinale, instrumentale et organisationnelle**, pas comme pouvoir souverain absolu de refonte. La BCE change beaucoup, mais souvent en tension avec le traité, les juridictions, les États membres et le problème du moral hazard.


