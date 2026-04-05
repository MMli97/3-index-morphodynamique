# Scoring Notes — SYS004 Linux Kernel

## Identification

- **System ID :** SYS004
- **System name :** Linux Kernel
- **Domain :** technological
- **Subdomain :** operating system kernel
- **Scale :** macro
- **Date scored :** 2026-04-01
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Robert Love, *Linux Kernel Development*, 3rd Edition (2010) — Pearson Education [LKD]
2. Jonathan Corbet, Alessandro Rubini, Greg Kroah-Hartman, *Linux Device Drivers*, 3rd Edition (2005) — O'Reilly [LDD3]
3. Jonathan Corbet & Greg Kroah-Hartman, *2017 Linux Kernel Development Report*, The Linux Foundation [LKR2017]

---

## A1 — Profondeur hiérarchique

| Sous-critère | Score | Justification |
|---|---|---|
| H1 : ≥ 2 niveaux causaux distincts | 1 | Distinction fondamentale hardware / kernel space / user space. Le matériel (interruptions, MMU, DMA) agit sur le kernel, qui à son tour gère les processus en user space. [LKD ch.1 : distinction supervisor mode / user mode ; LDD3 : « Unix transfers execution from user space to kernel space whenever an application issues a system call or is suspended by a hardware interrupt »] |
| H2 : ≥ 3 niveaux causaux distincts | 1 | Au minimum : (1) hardware/interrupts → (2) sous-systèmes kernel bas-niveau (scheduler, memory management, VFS, block I/O) → (3) appels système / interface user space. Le kernel lui-même est stratifié : les interrupts déclenchent des bottom halves (softirqs/tasklets), qui alimentent les sous-systèmes, qui servent les processus. [LKD ch.7-8 : interrupts → bottom halves → traitement différé] |
| H3 : ≥ 4 niveaux causaux distincts | 1 | (1) Hardware / interrupts matérielles → (2) Bottom halves / softirqs / tasklets → (3) Sous-systèmes kernel (scheduler CFS, VFS avec superblock/inode/dentry/file, slab allocator, block I/O layer avec I/O schedulers) → (4) Interface syscall / processus user space. Le device model (kobject → ktype → kset → sysfs) ajoute encore un empilement interne. [LKD ch.17 : kobjects/ktypes/ksets ; LKD ch.13 : VFS à 4 objets hiérarchisés] |
| H4 : Niveaux fonctionnellement différenciés | 1 | Chaque niveau remplit une fonction distincte : gestion d'interruptions ≠ ordonnancement de processus ≠ gestion mémoire ≠ abstraction filesystem ≠ interface utilisateur. Le scheduler (CFS) ne fait que l'allocation CPU ; le VFS ne fait que l'abstraction fichier ; la mémoire gère zones/pages/slab séparément. [LDD3 : « the kernel's role can be split into process management, memory management, filesystems, device control, networking »] |
| H5 : Causalité bidirectionnelle entre niveaux | 1 | Exemples multiples : (a) un processus user space fait un syscall → entre en kernel space → peut déclencher I/O → génère interrupt hardware ; inversement, une interruption hardware → remonte via bottom half → réveille un processus bloqué. (b) Le scheduler préempte un processus (top-down) mais un processus peut céder le CPU volontairement via yield (bottom-up). (c) Le page fault : le hardware signale au kernel un défaut, le kernel charge la page puis rend le contrôle au processus. [LKD ch.4 : preemption et wake-up bidirectionnels ; LKD ch.7 : interrupt → bottom half → processus] |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune hésitation majeure. Le kernel Linux est un cas archétypique de système à profondeur hiérarchique élevée. Le nombre réel de niveaux dépasse largement 4 si l'on compte les couches internes (e.g. dans le networking stack : socket → protocol → device → driver → hardware).

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère | Score | Justification |
|---|---|---|
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1 | Un bug dans un driver peut corrompre la mémoire kernel et affecter le scheduler, le VFS, ou tout autre sous-système. Un changement dans le block I/O scheduler affecte les performances du VFS et des processus. [LKD ch.2 : « No Memory Protection » — le kernel n'a pas de protection mémoire interne, tout s'exécute dans le même address space ; LDD3 : « a kernel fault kills the current process at least, if not the whole system »] |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique | 1 | Un OOM (Out-Of-Memory) dans le sous-système mémoire remonte jusqu'à tuer des processus user space (OOM killer). Une interruption hardware traverse bottom halves → scheduler → processus. Un changement de configuration sysfs (niveau user) modifie le comportement des modules kernel (niveau bas). [LKD ch.12 : zones mémoire et allocation ; LKD ch.4 : l'ordonnancement affecte tous les niveaux] |
| P3 : Propagation modifie l'état global observable | 1 | Un kernel panic arrête l'ensemble du système. Une surcharge CPU modifie les latences de tous les processus. L'ajout d'un module (insmod) modifie les symboles exportés et les capacités disponibles globalement. Un changement du scheduler policy affecte l'état global observé par tous les processus. [LDD3 : « Memory violations in the kernel result in an oops, which is a major kernel error » ; LKR2017 : chaque release affecte le comportement global de milliards de dispositifs] |
| P4 : Isolement difficile sans modification structurelle | 1 | Le kernel monolithique rend l'isolement intrinsèquement difficile : tout le code s'exécute dans le même address space. Même les modules loadables partagent l'espace mémoire kernel. Il n'y a pas de protection mémoire entre sous-systèmes. [LKD ch.1 : « Linux is a monolithic kernel; the Linux kernel executes in a single address space entirely in kernel mode » ; LDD3 : « No Memory Protection »] |
| P5 : Couplage fonctionnel non trivial | 1 | Les sous-systèmes sont fortement couplés par des dépendances fonctionnelles complexes : le VFS dépend du block I/O layer, qui dépend des drivers, qui utilisent le memory management ; le scheduler interagit avec le memory management (swap), le VFS (I/O wait), et les interrupts. Le device model (kobject) est transversal à tous les sous-systèmes. [LKD ch.13-14 : VFS↔block I/O ; LKD ch.17 : kobjects utilisés par tous les sous-systèmes ; LDD3 : « the Linux device model is the abstraction layer used by the kernel to describe the hardware and software resources it is managing »] |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** P4 pourrait être discuté si l'on considère les cgroups et namespaces comme des mécanismes d'isolement, mais ceux-ci opèrent au niveau des processus user space, pas entre sous-systèmes kernel. Le kernel lui-même reste monolithique et fortement couplé en interne.

---

## A3 — Intégration

| Sous-critère | Score | Justification |
|---|---|---|
| I1 : Mécanisme explicite de coordination | 1 | Multiples mécanismes de coordination explicites : spinlocks, mutexes, semaphores, RCU, completion variables, sequential locks, atomic operations. Le scheduler lui-même est un mécanisme de coordination globale (CFS distribue le CPU). Le locking infrastructure est un sous-système maintenu dédié. [LKD ch.9-10 : catalogue complet des primitives de synchronisation ; LDD3 ch.5 : concurrency et locking] |
| I2 : Réduction de variance observable | 1 | Le scheduler CFS garantit une distribution « fair » du CPU proportionnelle aux poids, réduisant la variance d'allocation. Le memory management distribue les pages entre zones (DMA, normal, high) selon des politiques stables. Les I/O schedulers (BFQ, Kyber) lissent les performances I/O. Les releases suivent un cycle prévisible de 9-10 semaines. [LKD ch.4 : CFS calcule la proportion de CPU de façon déterministe ; LKR2017 : « The trend toward shorter, more predictable release cycles »] |
| I3 : Synchronisation multi-niveaux | 1 | Interrupts et bottom halves sont synchronisés via des mécanismes spécifiques (disable_irq, spin_lock_bh). Le preemption model synchronise scheduler et kernel code. Le VFS synchronise les accès fichier entre processus via des locks sur inodes/dentries. Le page cache synchronise mémoire et I/O. [LKD ch.7-8 : synchronisation interrupts ↔ softirqs ↔ processus ; LKD ch.10 : « Spin Locks and Bottom Halves »] |
| I4 : Boucles de rétroaction globales | 1 | Le scheduler CFS utilise le virtual runtime comme feedback global pour rééquilibrer l'allocation CPU. Le memory management utilise le kswapd et l'OOM killer comme boucles de rétroaction sur la pression mémoire. Le congestion control réseau (BBR) ajuste les débits en fonction du feedback. La stable update process corrige les régressions comme boucle de feedback qualité. [LKD ch.4 : vruntime comme signal de feedback ; LKR2017 : BBR congestion-control, stable updates] |
| I5 : Maintien d'un état global cohérent | 1 | Le kernel maintient un état global cohérent via : (a) la table des processus (task_struct pour chaque processus), (b) le VFS superblock/inode comme état global du filesystem, (c) le device model (kobject tree) comme représentation cohérente du hardware, (d) sysfs comme reflet en temps réel de l'état interne. La règle « no regressions » garantit la cohérence entre versions. [LKD ch.3 : process descriptor et état global ; LKD ch.17 : sysfs comme miroir de l'état ; LKR2017 : « the kernel's strong no-regressions rule »] |

**Score A3 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune. Le kernel Linux est conçu explicitement pour maintenir un état global cohérent malgré la concurrence massive (SMP, preemption, interrupts asynchrones). C'est sa raison d'être.

---

## A4 — Normativité

| Sous-critère | Score | Justification |
|---|---|---|
| N1 : Attracteur dynamique existant | 1 | Le kernel tend vers un état stable d'exécution : le scheduler converge vers une distribution équitable du CPU (CFS vruntime converge), le memory manager tend vers un équilibre entre pages actives/inactives, le système de fichiers maintient la cohérence via journaling. L'ensemble du système converge vers un fonctionnement nominal après boot. [LKD ch.4 : CFS converge vers l'équité via vruntime ; LKD ch.12 : zones mémoire et équilibre page allocation] |
| N2 : Correction active d'écart | 1 | Le scheduler préempte activement les processus qui ont consommé trop de CPU (CFS : si vruntime > moyenne, préemption). L'OOM killer tue activement les processus pour corriger l'écart de mémoire. Le watchdog détecte les soft lockups. Le stable update process corrige activement les bugs et régressions. [LKD ch.4 : preemption comme correction active ; LKR2017 : « the stable process ensures that important fixes are made available »] |
| N3 : Hiérarchie de priorités régulatoires | 1 | Hiérarchie claire : (a) Real-time processes (SCHED_FIFO/SCHED_RR, priorité 0-99) > Normal processes (SCHED_NORMAL, nice -20 à +19). (b) Les interrupts ont priorité sur tout le reste. (c) Le kernel preempt a priorité sur le user space. (d) Dans le memory management : DMA zone > normal zone > high memory en termes de criticité. [LKD ch.4 : « All real-time processes are at a higher priority than normal processes » ; hiérarchie scheduler classes] |
| N4 : Mécanisme interne de stabilisation | 1 | Multiples mécanismes : le BKL (Big Kernel Lock, historique) puis les spinlocks/mutexes empêchent les data races. Le reference counting (kref) empêche les use-after-free. Les memory barriers garantissent l'ordering. Le slab poisoning détecte les corruptions mémoire. Le vermagic vérifie la compatibilité des modules. [LKD ch.10 : toute la panoplie de synchronisation ; LKD ch.17 : reference counting via kref ; LDD3 : slab poisoning, vermagic] |
| N5 : Résistance aux perturbations prolongées | 0.5 | Le kernel résiste bien aux perturbations « normales » : surcharge CPU (le scheduler continue de fonctionner), pression mémoire (swap + OOM killer), défaillance de drivers (oops sans nécessairement panic). Cependant, certaines perturbations prolongées peuvent être fatales : corruption mémoire kernel, deadlocks dans les locks critiques, panic complet sur erreurs non récupérables. Le modèle monolithique (pas de protection mémoire interne) limite la résistance. [LDD3 : « a kernel fault kills the current process at least, if not the whole system » ; LKD ch.2 : « No Memory Protection »] |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** N5 est le point de discussion principal. Le kernel est extrêmement robuste pour les perturbations « prévues » (charge, OOM, drivers défaillants), mais sa nature monolithique le rend vulnérable aux corruptions internes non récupérables. Score 0.5 plutôt que 1 car un microkernel serait plus résilient aux pannes de composants individuels.

**Distinction normativité endogène / imposée :** La normativité est très largement **endogène**. Le kernel définit lui-même ses attracteurs (scheduler policy, memory zones, process priorities), ses mécanismes de correction (preemption, OOM kill), et ses hiérarchies de priorités. La seule composante « imposée » est le hardware (contraintes physiques de mémoire, interruptions matérielles), mais le kernel transforme ces contraintes en régulations internes actives. Le processus de développement communautaire (consensus, no-regressions rule) est également une normativité endogène au niveau organisationnel.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère | Score | Justification |
|---|---|---|
| R1 : Ajustement paramétrique local | 1 | Le kernel offre de nombreux paramètres ajustables à chaud : sysctl (centaines de paramètres runtime), module parameters via sysfs, /proc/sys tunables, nice values et scheduling policies modifiables par processus, memory overcommit settings. [LKD ch.17 : module parameters via sysfs modifiables à runtime ; LDD3 : « If perm is set, [the parameter] appears under /sys/module with the given set of permissions »] |
| R2 : Modification durable de configuration interne | 1 | Les modules loadables permettent d'ajouter/retirer durablement des fonctionnalités (drivers, filesystems, protocoles réseau) sans recompilation. Le système Kconfig (CONFIG_*) permet de reconfigurer durablement le kernel à la compilation. Les cgroups et namespaces restructurent durablement l'allocation des ressources. [LKD ch.1 : « the capability to dynamically load separate binaries (kernel modules) into the kernel image » ; LKD ch.17 : modules loadables ; LKR2017 : nouveaux features mergés à chaque release] |
| R3 : Reconfiguration de réseau ou de structure | 1 | Le scheduler est modulaire (scheduler classes) : on peut remplacer l'algorithme d'ordonnancement (historiquement O(1) → CFS, ajout de BFQ/Kyber pour block I/O). Le VFS est une abstraction qui permet de brancher n'importe quel filesystem. Le device model (kobject) permet de restructurer dynamiquement la hiérarchie hardware. Les namespaces restructurent la visibilité des ressources. [LKD ch.4 : « The Linux scheduler is modular, enabling different algorithms to schedule different types of processes — scheduler classes » ; LKD ch.13 : VFS comme couche d'abstraction pluggable] |
| R4 : Modification des mécanismes de régulation | 1 | Le kernel permet de changer ses propres mécanismes de régulation : remplacement du timer subsystem (LKR2017 : « the kernel's core timer mechanism was replaced with a far more efficient implementation »), remplacement du scheduler (O(1) → CFS), ajout de nouveaux mécanismes de sécurité (seccomp, KSPP hardening), remplacement de la documentation toolchain. Au niveau du développement, le processus lui-même évolue (passage à Git, stable updates process). [LKR2017 : multiples remplacements de sous-systèmes entiers entre versions] |
| R5 : Capacité à produire de nouvelles règles | 0.5 | Le kernel peut intégrer de nouvelles catégories de régulation (ex: ajout de cgroups, ajout de namespaces, ajout de BPF/eBPF comme machine virtuelle in-kernel pour des règles programmables, ajout de TEE framework). Cependant, ces nouvelles règles sont produites par la communauté humaine de développeurs, pas par le kernel lui-même de façon autonome. Le kernel n'a pas de capacité d'auto-génération de nouvelles règles ; il exécute ce que les développeurs codent. eBPF est le cas le plus proche d'une capacité endogène de nouvelles règles (programmes chargés dynamiquement), mais ils sont écrits par des humains. [LKR2017 : « express data path mechanism enables high-speed packet processing with user-loaded BPF programs »] |

**Score A5 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** R5 est le point délicat. Le kernel est extraordinairement plastique — on peut remplacer pratiquement n'importe quel sous-système. Mais la production de nouvelles règles reste exogène (développeurs humains). eBPF s'approche d'une capacité de production de règles à runtime, mais les programmes BPF sont écrits par des humains, pas générés par le kernel. Score 0.5 car la capacité existe structurellement (le kernel peut accueillir de nouvelles règles via modules, BPF, etc.) mais n'est pas autonome.

---

## Synthèse

| Axe | Score |
|-----|-------|
| A1 | 1.00 |
| A2 | 1.00 |
| A3 | 1.00 |
| A4 | 0.90 |
| A5 | 0.90 |

### Gradients (calculés)

| Gradient | Valeur |
|----------|--------|
| Δ₂₃ = A2 − A3 | 0.00 |
| Δ₄₅ = A4 − A5 | 0.00 |
| Δ₁₂ = A1 − A2 | 0.00 |
| Δ₃₅ = A3 − A5 | +0.10 |
| Δ₄₃ = A4 − A3 | −0.10 |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système intégré hautement complexe — scores plafonnés sur tous les axes
- **Régime secondaire :** Système normatif fort avec plasticité structurelle élevée
- **Marge :** Très faible marge entre axes (max écart = 0.10) — profil remarquablement équilibré
- **Surprise par rapport au jugement intuitif :** Aucune surprise majeure. Le kernel Linux est intuitivement un système très « complet » sur tous les axes, et le scoring confirme cette intuition. La seule nuance est que N5 (résistance aux perturbations prolongées) et R5 (production autonome de nouvelles règles) sont les deux seuls sous-critères à ne pas atteindre le maximum, ce qui est cohérent : (a) la nature monolithique limite la résilience aux corruptions internes, (b) le kernel ne produit pas de nouvelles règles de manière autonome — il reste un artefact piloté par une communauté humaine.

---

## Notes libres

- Le Linux Kernel est probablement l'un des artefacts technologiques les plus « complets » en termes de complexité systémique. Son profil presque maximal sur tous les axes reflète 25+ ans d'ingénierie collaborative à très grande échelle (15 600+ développeurs, 1 400+ entreprises).
- La distinction entre le kernel comme artefact technique et le kernel comme système socio-technique est importante : si l'on intégrait la communauté de développement comme partie du système, R5 monterait à 1 (la communauté produit effectivement de nouvelles règles).
- Le cas du BPF/eBPF est fascinant : c'est un mécanisme qui rapproche le kernel d'une capacité de « programmation à runtime », mais les programmes sont écrits par des humains.
- Comparaison intéressante avec un microkernel (ex: L4, Minix) : on attendrait A2 plus bas (meilleur isolement) mais A4/N5 plus haut (meilleure résistance aux pannes de composants).
- Le modèle de développement (release tous les 9-10 semaines, 8.5 patches/heure, consensus-driven) est lui-même un système normatif remarquable qui mériterait son propre scoring en tant que système institutionnel.
