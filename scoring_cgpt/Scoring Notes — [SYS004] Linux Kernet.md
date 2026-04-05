# Scoring note [SYS004] — LINUX KERNEL

## Identification

- **System ID :** SYS004

- **System name :** Linux Kernel

- **Domain :** technological

- **Subdomain :** operating system kernel / large-scale open-source infrastructure

- **Scale :** macro

- **Date scored :** 2026-04-02

- **Confidence globale :** high

## Sources

1. Robert Love, *Linux Kernel Development*

2. Corbet & Kroah-Hartman, *Linux Kernel Development Report 2017*

3. Corbet, Rubini, Kroah-Hartman, *Linux Device Drivers*

---

## A1 — Profondeur hiérarchique

| Sous-critère                                  | Score | Justification                                                                                                                                                                                                                                       |
| --------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | **1** | Le noyau articule au minimum matériel / kernel-space / user-space ; Love décrit explicitement l’exécution en user-space, en kernel-space en contexte de processus, et en contexte d’interruption.                                                   |
| H2 : ≥ 3 niveaux causaux distincts            | **1** | Au-delà de cette tripartition, les sources distinguent plusieurs sous-niveaux : scheduler, mémoire, VFS, block I/O, pilotes, modules, appels système, etc.                                                                                          |
| H3 : ≥ 4 niveaux causaux distincts            | **1** | On peut identifier sans forcer : matériel, interruptions/bottom halves, sous-systèmes cœur (scheduler/mémoire/VFS), interfaces système/modules, espace utilisateur. Les chapitres du livre de Love attestent cette stratification.                  |
| H4 : Niveaux fonctionnellement différenciés   | **1** | Les niveaux ne sont pas redondants : interruptions, synchronisation, mémoire, système de fichiers, I/O bloc, pilotes, réseau remplissent des fonctions distinctes.                                                                                  |
| H5 : Causalité bidirectionnelle entre niveaux | **1** | Les applications agissent sur le noyau via les syscalls ; le matériel interrompt le noyau ; le noyau arbitre ensuite les ressources et renvoie ses effets vers les processus et périphériques. La causalité est clairement montante et descendante. |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** très faibles. Le Linux kernel est un cas presque canonique de système hiérarchique multi-niveaux.

---

## A2 — Capacité de propagation

| Sous-critère                                                  | Score   | Justification                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | **1**   | Un changement local dans un driver, dans la mémoire ou dans le block layer peut affecter d’autres parties du système ; les sources insistent sur la forte interdépendance des sous-systèmes et sur l’importance de la revue/maintenance à travers les arbres de sous-système. |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | **1**   | Une perturbation peut remonter du matériel vers les handlers, puis vers les sous-systèmes cœur et jusqu’au comportement observable par les processus utilisateurs.                                                                                                            |
| P3 : Propagation modifie l’état global observable             | **1**   | Le noyau « détermine how well the system will work » ; un changement ou bug local peut modifier performances, stabilité, sécurité, support matériel et comportement global.                                                                                                   |
| P4 : Isolement difficile sans modification structurelle       | **0.5** | Le noyau est modulaire et hiérarchisé, ce qui aide à isoler certains changements ; mais la documentation souligne aussi qu’un projet de cette ampleur ne peut fonctionner sans coordination distribuée et outils adaptés, signe d’un isolement imparfait des perturbations.   |
| P5 : Couplage fonctionnel non trivial                         | **1**   | Le couplage est élevé : ordonnanceur, mémoire, VFS, I/O, pilotes, réseau et sécurité interagissent en permanence. Le livre de Love et *Linux Device Drivers* décrivent ces dépendances comme structurelles.                                                                   |

**Score A2 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** P4 pourrait être monté à 1 si l’on prend surtout la dimension runtime ; je le laisse à 0.5 parce que la modularité réelle du noyau empêche de parler d’une propagation totalement inarrêtable.

---

## A3 — Intégration

| Sous-critère                             | Score | Justification                                                                                                                                                                                     |
| ---------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | **1** | Le noyau possède des mécanismes explicites de coordination : scheduler, sync primitives, VFS commun, block layer, device model, arbres de mainteneurs, stable process.                            |
| I2 : Réduction de variance observable    | **1** | Le modèle de releases courtes, la discipline par patchs atomiques et la stable team visent précisément à limiter les divergences, les régressions et les différences entre distributions.         |
| I3 : Synchronisation multi-niveaux       | **1** | Les chapitres entiers sur les atomic ops, spinlocks, semaphores, mutexes, barriers, bottom halves et work queues attestent une synchronisation multi-niveaux explicite.                           |
| I4 : Boucles de rétroaction globales     | **1** | Tests automatiques, bug reports, revue de patchs, maintenance stable et intégration continue constituent des boucles de retour globales qui réinjectent les écarts dans la régulation du système. |
| I5 : Maintien d’un état global cohérent  | **1** | La cohérence globale du système est une fonction centrale du noyau : gestion matérielle, sécurité, exécution des programmes, intégrité du système.                                                |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** faibles.

---

## A4 — Normativité

| Sous-critère                                 | Score   | Justification                                                                                                                                                                                                                                   |
| -------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | **1**   | Il existe un attracteur clair : un noyau stable, intégrable, non régressif, publiable dans le cycle principal puis stable. Les sources décrivent ce modèle comme structurant tout le projet.                                                    |
| N2 : Correction active d’écart               | **1**   | Le stable team applique activement des correctifs ; le zéro-day robot détecte des bugs qui sont ensuite corrigés ; les patchs sont revus avant intégration.                                                                                     |
| N3 : Hiérarchie de priorités régulatoires    | **1**   | La chaîne mainteneurs → arbres de sous-systèmes → mainteneur principal, avec règles de signoff et consensus, constitue une hiérarchie régulatoire nette.                                                                                        |
| N4 : Mécanisme interne de stabilisation      | **1**   | Revue de code, cycles courts, tests automatiques, maintenance stable, règle de non-régression : tout cela relève d’une stabilisation interne, non d’un simple contrôle externe.                                                                 |
| N5 : Résistance aux perturbations prolongées | **0.5** | La résistance est forte, mais pas absolue : le rapport souligne que des milliers de fixes post-release restent nécessaires à cause de la diversité matérielle et des workloads réels. Le système tient, mais au prix d’une correction continue. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** N5 pourrait être mis à 1 si l’on valorise l’endurance historique du projet ; je le maintiens à 0.5 pour garder visible le caractère jamais totalement stabilisé du noyau.

**Distinction normativité endogène / imposée :** normativité majoritairement **endogène**. Elle est produite par les mécanismes internes du projet et du code lui-même : mainteneurs, signoffs, consensus, stable process, tests, règle de non-régression. Les entreprises comptent, mais aucune ne doit dominer l’orientation du noyau.

---

## A5 — Capacité de révision

| Sous-critère                                       | Score   | Justification                                                                                                                                                                                                                                              |
| -------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | **1**   | Le noyau supporte abondamment des ajustements locaux : configuration, modules, paramètres, compilation conditionnelle, activation de fonctionnalités, tuning de sous-systèmes.                                                                             |
| R2 : Modification durable de configuration interne | **1**   | Les releases intègrent durablement de nouvelles options, nouveaux drivers, nouvelles implémentations et correctifs stables.                                                                                                                                |
| R3 : Reconfiguration de réseau ou de structure     | **1**   | Les sources décrivent l’ajout de centaines de drivers, de nouveaux frameworks, le remplacement de mécanismes internes, la documentation Sphinx, et une architecture modulaire extensible.                                                                  |
| R4 : Modification des mécanismes de régulation     | **1**   | Les outils et processus de régulation évoluent eux-mêmes : passage à Git, amélioration de la culture de test, refinement du release model, revue distribuée, stable process.                                                                               |
| R5 : Capacité à produire de nouvelles règles       | **0.5** | Oui, mais surtout au niveau du projet socio-technique plutôt qu’au niveau du noyau “runtime” lui-même. Le système génère de nouvelles conventions, workflows et critères d’intégration, mais cette production de règles n’est pas autonome au sens strict. |

**Score A5 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** si tu réduis strictement la frontière au binaire en exécution, A5 baisse fortement ; avec la frontière socio-technique attestée par les sources, 0.90 me paraît juste.

---

## Synthèse

| Axe | Score    |
| --- | -------- |
| A1  | **1.00** |
| A2  | **0.90** |
| A3  | **1.00** |
| A4  | **0.90** |
| A5  | **0.90** |

### Gradients

| Gradient      | Valeur    |
| ------------- | --------- |
| Δ₂₃ = A2 − A3 | **-0.10** |
| Δ₄₅ = A4 − A5 | **0.00**  |
| Δ₁₂ = A1 − A2 | **0.10**  |
| Δ₃₅ = A3 − A5 | **0.10**  |
| Δ₄₃ = A4 − A3 | **-0.10** |

### Lecture rapide

Le **Linux kernel** apparaît ici comme un système :

- **très profondément hiérarchisé**,

- **très fortement intégré**,

- **hautement normé mais pas rigide au point d’empêcher la révision**,

- avec une **propagation élevée** mais partiellement contenue par sa modularité et son organisation distribuée.

Autrement dit, ce n’est ni une simple “architecture pure”, ni un système figé. C’est un **système hautement intégré, normatif et révisable**, avec une tension productive entre stabilité et transformation. Les sources insistent précisément sur cette combinaison : cycles courts, non-régression, revue distribuée, maintenance stable, tests, croissance continue, ajout de nouvelles capacités sans perte complète de cohérence globale.


