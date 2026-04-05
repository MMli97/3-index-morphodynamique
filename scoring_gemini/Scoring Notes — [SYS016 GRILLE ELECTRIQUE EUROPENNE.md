

# Scoring Notes — SYS016 GRILLE ELECTRIQUE EUROPENNE

## Identification

- **System ID :** SYS016

- **System name :** Grille Électrique Européenne (Réseau synchrone continental et cyber-infrastructure)

- **Domain :** technological / infrastructure

- **Scale :** macro

- **Date scored :** 2026-04-02

- **Confidence globale :** high

## Sources

1. Grid Modernization Strategy 2024.txt (Stratégie de modernisation, intégration DER, aspects macro)

2. Smart_Grid_Intrusion_Detection_for_IEC_60870-5-104_With_Feature_Optimization_Privacy_Protection_and_Honeypot-Firewall_Integration.txt (Cybersécurité, SCADA, protocoles)

3. Power System Stability and Control -- Kundur -- 2007 (Dynamique physique des réseaux, stabilité électromécanique, contrôles hiérarchiques)

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                                                                                                                                                    |
| --------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | La grille est fondamentalement composée de millions d'appareils physiques connectés et reliés par des systèmes de contrôle, formant des systèmes intégrés. Kundur détaille par exemple l'interaction entre la machine (générateur) et le réseau.                                                     |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | Le réseau intègre physiquement les niveaux de production (generation), de transport (transmission), et de distribution jusqu'à l'utilisation finale. Sur le plan du contrôle, Kundur décrit la boucle locale (AVR/régulateur de vitesse), le contrôle de la centrale, et le contrôle régional (AGC). |
| H3 : ≥ 4 niveaux causaux distincts            | 1         | Outre l'infrastructure physique, le système est structuré par des couches cyber-physiques : les appareils et systèmes intégrés, les opérations, la planification, ainsi que les marchés, politiques et réglementations.                                                                              |
| H4 : Niveaux fonctionnellement différenciés   | 1         | Ces différents niveaux servent des fonctions très distinctes, telles que la production, le transfert, le stockage et la consommation d'électricité à travers de vastes régions géographiques.                                                                                                        |
| H5 : Causalité bidirectionnelle entre niveaux | 1         | Les ressources énergétiques distribuées au niveau local (Grid Edge) impactent directement les opérations globales du système (Bulk Power System). En retour, les signaux du réseau modulent les charges locales.                                                                                     |

**Score A1 = 5.0 / 5.0 = 1.00**

**Hésitations / ambiguïtés :** Aucune. L'ajout de Kundur renforce l'évidence d'une hiérarchie stricte du point de vue électromécanique (de la dynamique du rotor individuel jusqu'aux oscillations interzones du réseau continental).

---

## A2 — Capacité de propagation (invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | Les pannes dans d'autres infrastructures peuvent avoir des impacts majeurs sur la sécurité, la fiabilité et la résilience du réseau électrique. De même, les vulnérabilités du protocole IEC 60870-5-104 peuvent entraîner des temps d'arrêt du système et des pannes d'infrastructures critiques. (Kundur explique ceci par la propagation des défauts causant des pertes de stabilité transitoire). |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | Les nouvelles charges et les ressources distribuées impactent le système principal en augmentant la variation de la charge et l'incertitude des prévisions à de multiples échelles.                                                                                                                                                                                                                   |
| P3 : Propagation modifie l'état global observable             | 1         | Le remplacement des générateurs massifs (et de leur inertie mécanique) par des onduleurs modifie fondamentalement la dynamique des futurs systèmes électriques à l'échelle globale. (Kundur décrit parfaitement comment une perte d'inertie modifie l'équation d'oscillation du réseau).                                                                                                              |
| P4 : Isolement difficile sans modification structurelle       | 0.5       | Bien qu'il existe de profondes interdépendances entre le réseau, les systèmes de communication et d'autres infrastructures rendant l'isolement complexe , le système permet des modifications structurelles dynamiques, comme les micro-réseaux qui peuvent fonctionner de manière autonome en tant que systèmes indépendants en cas d'urgence.                                                       |
| P5 : Couplage fonctionnel non trivial                         | 1         | Le système devient extrêmement complexe : potentiellement des millions d'appareils intelligents devront être coordonnés avec les systèmes de contrôle existants.                                                                                                                                                                                                                                      |

**Score A2 = 4.5 / 5.0 = 0.90**

**Hésitations / ambiguïtés :** Le score de P4 reste à 0.5 car l'islanding (îlotage) nécessite une modification structurelle active (ouverture de disjoncteurs, activation de schémas de protection spéciaux décrits par Kundur) pour protéger et isoler le réseau.

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                                                                                                                                                                |
| ---------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1         | Les systèmes SCADA offrent la capacité de surveiller, contrôler et automatiser les infrastructures critiques comme les réseaux électriques en temps réel. L'ouvrage de Kundur détaille également le Contrôle Automatique de Génération (AGC) qui coordonne la fréquence globale. |
| I2 : Réduction de variance observable    | 1         | Des technologies de contrôle étendu (wide-area control) sont déployées spécifiquement pour assurer la stabilité de la tension et de la fréquence.                                                                                                                                |
| I3 : Synchronisation multi-niveaux       | 1         | La synchronisation est surveillée par des mesures de phaseurs (synchrophasors) en temps réel à des vitesses de 30 à 120 échantillons par seconde. (Le synchronisme AC est la propriété fondamentale du réseau européen selon Kundur).                                            |
| I4 : Boucles de rétroaction globales     | 1         | Des charges actives participent à la régulation via des boucles de rétroaction : les climatiseurs ou chauffe-eau ajustent leurs thermostats pour réduire la consommation lorsque le réseau est sous tension.                                                                     |
| I5 : Maintien d'un état global cohérent  | 1         | Toute l'intégration vise à gérer les variations afin de maintenir un réseau moderne qui soit résilient, fiable, sécurisé et abordable.                                                                                                                                           |

**Score A3 = 5.0 / 5.0 = 1.00**

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1         | Le système est conçu pour fonctionner de manière fiable dans des conditions normales ou en régime permanent ("steady-state"). (L'attracteur physique est la fréquence de 50Hz de l'ENTSO-E).                                                                                                                                       |
| N2 : Correction active d'écart               | 1         | Historiquement, l'inertie mécanique ralentit la dynamique du système en réponse aux perturbations. Les onduleurs "Grid-forming" participent désormais activement à la régulation de la fréquence et de la tension.                                                                                                                 |
| N3 : Hiérarchie de priorités régulatoires    | 1         | En cas de défaillance, le système priorise les opérations : les micro-réseaux d'urgence maintiennent l'alimentation électrique des charges critiques pendant que le réseau principal est attaqué ou en panne.                                                                                                                      |
| N4 : Mécanisme interne de stabilisation      | 1         | Le réseau inclut des algorithmes pour stabiliser activement les opérations, par exemple via le lissage exponentiel (EWMA) ou des filtres de corrélation de Pearson pour détecter et rejeter les anomalies cyber-physiques. Sur le plan électrotechnique (Kundur), ce sont les couples de synchronisation et d'amortissement (PSS). |
| N5 : Résistance aux perturbations prolongées | 0.5       | Bien que de nombreuses défenses existent, les menaces croissantes (attaques physiques/cyber, climat) causent encore des pannes dévastatrices de longue durée et sur de vastes zones.                                                                                                                                               |

**Score A4 = 4.5 / 5.0 = 0.90**

**Distinction normativité endogène / imposée :** La nouveauté apportée par les apports combinés de Kundur (physique) et des Smart Grids (cyber) montre que si la norme est imposée (cahier des charges), la force de rappel (couple électromécanique, régulations PID, détections SCADA) est viscéralement endogène.

---

## A5 — Capacité de révision (plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                                                                                                                                 |
| -------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1         | Le système ajuste ses paramètres localement de façon autonome, par exemple avec un "Adaptive thresholding" qui recalcule le seuil d'anomalie en fonction de l'évolution du trafic bénin. (Côté équipement, Kundur détaille l'ajustement local des gains des AVR). |
| R2 : Modification durable de configuration interne | 1         | De nouvelles approches opérationnelles intègrent des schémas d'action corrective avancés ("remedial action schemes"), l'îlotage adaptatif et des micro-réseaux auto-organisés.                                                                                    |
| R3 : Reconfiguration de réseau ou de structure     | 1         | La structure elle-même est en révision constante via l'intégration massive de réseaux HVDC et MVDC pour relier de nouveaux terminaux multiples.                                                                                                                   |
| R4 : Modification des mécanismes de régulation     | 0.5       | Les conceptions de marché, ainsi que les politiques et les réglementations, doivent être mises à jour pour intégrer de nouveaux objectifs comme la décarbonation. Cette plasticité existe, mais elle est institutionnelle et lente.                               |
| R5 : Capacité à produire de nouvelles règles       | 0.5       | Les agents d'intelligence artificielle (par exemple l'adaptation à la dérive de concept via la divergence de Kullback-Leibler) génèrent de nouvelles règles de classification de comportement, bien que les lois fondamentales du réseau soient immuables.        |

**Score A5 = 4.0 / 5.0 = 0.80**

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 1.00      |
| A2      | 0.90      |
| A3      | 1.00      |
| A4      | 0.90      |
| A5      | 0.80      |

### Gradients (calculés)

| **Gradient**  | **Valeur** |
| ------------- | ---------- |
| Δ₂₃ = A2 − A3 | -0.10      |
| Δ₄₅ = A4 − A5 | +0.10      |
| Δ₁₂ = A1 − A2 | +0.10      |
| Δ₃₅ = A3 − A5 | +0.20      |
| Δ₄₃ = A4 − A3 | -0.10      |

### Classification

- **Régime primaire :** *Régulation infrastructurelle massivement intégrée.* La grille électrique (surtout européenne/continentale, A1=1, A3=1) représente l'archétype du système cyber-physique macroscopique rigoureusement asservi au maintien d'une seule variable critique (le synchronisme/la fréquence).

- **Régime secondaire :** *Complexification et apprentissage adaptatif.* Avec la transition énergétique et les Smart Grids, le système acquiert une capacité de plasticité adaptative et de résistance (A2=0.90, A4=0.90, A5=0.80) via la distribution de "l'intelligence" en bordure de réseau (inverters, SCADA dynamiques, IA distribuée).

---

## Notes libres

L'intégration de la source de Kundur permet de sceller définitivement les fondations physiques de la grille électrique. Le système n'est pas seulement un réseau de données qui "planterait" (comme un réseau internet), c'est un ensemble de masses tournantes couplées électromécaniquement. La transition évoquée dans le document stratégique américain (le passage des générateurs à forte inertie vers des onduleurs électroniques de puissance ) constitue une transformation ontologique du système : la normativité purement inertielle (décrite par Kundur) cède progressivement la place à une normativité algorithmique active, pilotée par les nouveaux systèmes cybernétiques et les modèles de machine learning décrits dans la deuxième source.
