

# Scoring Notes — [SYS004] Linux Kernel

## Identification

- **System ID :** SYS004

- **System name :** Noyau Linux (Linux Kernel)

- **Domain :** Technologique / Informatique

- **Subdomain :** Noyau de système d'exploitation monolithique modulaire

- **Scale :** Macro

- **Date scored :** 2026-04-02

- **Scorer :** Gemini

- **Confidence globale :** High

## Sources

1. `Linux Device Drivers, 3rd Edition (Jonathan Corbet, Alessandro Rubini etc.).txt`

2. `Linux Kernel Development (Developers Library) (Robert Love).txt`

3. `LinuxKernelReport_2017.txt`

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                                                    |
| --------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | Une séparation stricte et fondamentale existe entre l'espace utilisateur (user-space) et l'espace noyau (kernel-space) pour des raisons de sécurité et d'accès.                                      |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | Architecture stratifiée comprenant le matériel physique, le code noyau de base (gestion mémoire/processus), et l'espace utilisateur.                                                                 |
| H3 : ≥ 4 niveaux causaux distincts            | 1         | La hiérarchie inclut le matériel, les pilotes de périphériques spécifiques, les sous-systèmes d'abstraction (comme le VFS), et les appels système (syscalls) qui font le pont avec les applications. |
| H4 : Niveaux fonctionnellement différenciés   | 1         | Chaque sous-système (ordonnanceur CFS, gestionnaire de mémoire virtuelle, pile réseau) possède des responsabilités uniques et strictement délimitées.                                                |
| H5 : Causalité bidirectionnelle entre niveaux | 1         | Les applications initient des requêtes descendantes via les appels système, tandis que le matériel déclenche des événements ascendants via les interruptions matérielles.                            |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune. Le noyau est structurellement hiérarchisé par sa conception même.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                                                                              |
| ------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | Une forte pression sur la mémoire virtuelle (manque de RAM) force les autres sous-systèmes, comme le cache du système de fichiers, à vider leurs données pour libérer de l'espace.                             |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | Une erreur matérielle remontée par un pilote (driver) va traverser la couche bloc, puis le système de fichiers, pour finalement aboutir à une erreur I/O dans une application utilisateur.                     |
| P3 : Propagation modifie l'état global observable             | 1         | Une erreur critique de synchronisation ou d'accès mémoire entraîne un "Kernel Panic", qui stoppe intentionnellement la machine entière pour éviter la corruption de données.                                   |
| P4 : Isolement difficile sans modification structurelle       | 0.5       | Bien que les modules de périphériques puissent être déchargés à la volée (LKM), le cœur du noyau reste monolithique : l'ordonnanceur et le gestionnaire de mémoire ne peuvent être isolés du reste du système. |
| P5 : Couplage fonctionnel non trivial                         | 1         | Le code utilise des primitives de synchronisation partagées et complexes (spinlocks, sémaphores, RCU) rendant le couplage temporel entre les processeurs (SMP) hautement interdépendant.                       |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** La nature hybride (monolithique mais modulaire) empêche un isolement total, justifiant le 0.5 sur P4.

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                                                                            |
| ---------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1         | Les "bottom halves" (softirqs, tasklets, work queues) coordonnent explicitement le travail différé après une interruption matérielle.                                                        |
| I2 : Réduction de variance observable    | 1         | Les mécanismes d'équilibrage de charge (load balancing) sur les systèmes multi-cœurs (SMP) redistribuent continuellement les processus pour lisser l'utilisation globale du CPU.             |
| I3 : Synchronisation multi-niveaux       | 1         | La gestion des horloges (timers), de l'interruption d'horloge système (timer interrupt), et l'ordonnancement maintiennent la cohérence temporelle entre le matériel et l'espace utilisateur. |
| I4 : Boucles de rétroaction globales     | 1         | Le "OOM Killer" (Out of Memory) analyse l'état global de la mémoire du système et intervient drastiquement en tuant des processus pour empêcher l'effondrement total de la machine.          |
| I5 : Maintien d'un état global cohérent  | 1         | Les barrières de mémoire, les opérations atomiques (type `atomic_t`) et la gestion stricte de la concurrence garantissent un état prévisible lors de l'exécution en parallèle.               |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Les ouvrages de référence démontrent que l'intégration et la synchronisation sécurisée (concurrency) sont le cœur même du développement noyau.

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                                                                                        |
| -------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1         | Le comportement du noyau est un arbitrage permanent cherchant un compromis idéal entre la réactivité du système (faible latence) et son débit global (throughput).                                                                       |
| N2 : Correction active d'écart               | 1         | Le noyau gère activement le transfert (swapping) des pages de mémoire inutilisées vers le disque (page-out) pour maintenir une réserve de RAM physique libre constante.                                                                  |
| N3 : Hiérarchie de priorités régulatoires    | 1         | L'exécution respecte une priorité absolue : le matériel préempte le noyau (interruptions), et le noyau préempte les applications (selon les valeurs *nice* et l'algorithme CFS).                                                         |
| N4 : Mécanisme interne de stabilisation      | 1         | Le modèle de développement ouvert intègre de multiples tests et la règle stricte des "zéro régressions", stabilisant le système à l'échelle de l'ingénierie.                                                                             |
| N5 : Résistance aux perturbations prolongées | 1         | La résilience est assurée par l'écosystème de développement collaboratif très actif (plus de 4300 développeurs) qui corrige continuellement et rapidement les failles et instabilités découvertes dans des environnements de production. |

**Score A4 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** L'aspect "socio-technique" (N4 et N5) transparaît via le document de 2017, montrant que la "survie" du système aux perturbations est assurée tant par le code que par la structure humaine qui le maintient.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                                                                |
| -------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| R1 : Ajustement paramétrique local                 | 1         | Les répertoires `/proc` et `/sys` (sysfs) exposent massivement l'état interne du système et permettent d'en ajuster les variables à la volée.                                                    |
| R2 : Modification durable de configuration interne | 1         | L'architecture permet le chargement et le déchargement de modules (LKM) sans redémarrage, reconfigurant les capacités du système en temps réel.                                                  |
| R3 : Reconfiguration de réseau ou de structure     | 1         | À l'échelle macroscopique, le code source du noyau évolue à un rythme extrême (environ 8,5 patches par heure, près de 10 000 patches par version en 2017), modifiant sa structure en permanence. |
| R4 : Modification des mécanismes de régulation     | 0.5       | Bien que les algorithmes internes évoluent avec les versions (comme l'ordonnanceur CFS), modifier ces mécanismes centraux exige généralement de recompiler le code et de redémarrer le système.  |
| R5 : Capacité à produire de nouvelles règles       | 0.5       | Le code ne s'écrit pas seul, mais il agit comme un framework extensif facilitant l'intégration continue de nouveaux protocoles, pilotes et fonctionnalités par les contributeurs.                |

**Score A5 = 0.80 / 1.00**

**Hésitations / ambiguïtés :** Les limites de la plasticité (R4, R5) viennent du fait qu'il reste un programme statique une fois chargé en mémoire (hors écosystèmes plus récents comme eBPF qui ne sont pas le focus principal des références 1 et 2).

---

## Synthèse

| **Axe**          | **Score** |
| ---------------- | --------- |
| A1 (Hiérarchie)  | 1.00      |
| A2 (Propagation) | 0.90      |
| A3 (Intégration) | 1.00      |
| A4 (Normativité) | 1.00      |
| A5 (Révision)    | 0.80      |

### Gradients (calculés)

| **Gradient**  | **Valeur** | **Interprétation logicielle**                                                                                                    |
| ------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Δ₂₃ = A2 − A3 | -0.10      | L'intégration mécanique est supérieure à la capacité de propagation, ce qui prévient l'effondrement en cascade en cas de bug.    |
| Δ₄₅ = A4 − A5 | 0.20       | La stabilité (normativité stricte) prime sur la plasticité interne. Le noyau privilégie la fiabilité sur le changement autonome. |
| Δ₁₂ = A1 − A2 | 0.10       | La hiérarchisation forte aide à circonscrire la propagation des états d'erreur.                                                  |
| Δ₃₅ = A3 − A5 | 0.20       | Le couplage fonctionnel est bien plus robuste que la capacité de reconfiguration à la volée du code de base.                     |
| Δ₄₃ = A4 − A3 | 0.00       | Équilibre absolu entre le maintien de l'état cohérent (A3) et la réponse régulatoire aux événements matériels (A4).              |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Entité socio-technique hyper-intégrée (A3, A4 = 1.00). Le noyau est un bloc de contrôle déterministe optimisé pour la stabilité et la coordination matérielle.

- **Régime secondaire :** Révisable par externalité modulaire (A5 = 0.80). Sa plasticité provient à la fois de son architecture modulaire et de la cadence colossale d'intégration continue de son écosystème de développement.

- **Marge :** Le système se comporte comme un organisme cybernétique hautement organisé dont le "système immunitaire" et la "capacité évolutive" reposent en partie sur les milliers d'ingénieurs humains qui produisent des patches en continu.

- **Surprise par rapport au jugement intuitif :** On attribue souvent une faible capacité d'adaptation "en direct" au code de bas niveau. Or, les fonctionnalités de modularité (LKM) et l'exportation des métriques via `/proc` lui confèrent une véritable capacité de correction de cap dynamique par l'utilisateur.
