# Scoring Notes — SYS009 Global Supply Chain

## Identification

- **System ID :** SYS009
- **System name :** Global Supply Chain
- **Domain :** economic
- **Subdomain :** logistics / operations management
- **Scale :** macro
- **Date scored :** 2026-04-01
- **Scorer :** CL
- **Confidence globale :** high

## Sources

1. Christopher, M. — *Logistics and Supply Chain Management* (Pearson, 4th ed., 2011). Bullwhip effect, cascade propagation, integration stages, synchronisation, risk management.
2. Chopra, S. & Meindl, P. — *Supply Chain Management: Strategy, Planning, and Operation* (Pearson, 6th ed., 2016). Coordination, bullwhip effect, network design, push/pull, safety inventory.
3. Sheffi, Y. — *The Resilient Enterprise* (MIT Press, 2005). Disruption, vulnerability, redundancy, flexibility, culture of resilience.

---

## A1 — Profondeur hiérarchique

| Sous-critère | Score | Justification |
|---|---|---|
| H1 : ≥ 2 niveaux causaux distincts | 1 | La supply chain comporte au minimum le niveau opérationnel (flux physiques : approvisionnement, production, distribution) et le niveau stratégique (planification, conception réseau). Christopher distingue explicitement ces couches (ch. 1, 6, 7). Chopra structure l'ouvrage autour de trois phases décisionnelles : stratégie, planification, opération (ch. 1.4). |
| H2 : ≥ 3 niveaux causaux distincts | 1 | Au moins trois niveaux sont clairement différenciés : (1) flux physiques locaux (production, transport), (2) coordination inter-firmes (VMI, CPFR, synchronisation — Christopher ch. 4, 7), (3) conception stratégique du réseau (localisation, capacité, sourcing global — Chopra ch. 5-6). Sheffi ajoute le niveau gestion des risques/résilience comme couche distincte. |
| H3 : ≥ 4 niveaux causaux distincts | 1 | Quatre niveaux identifiables : (1) processus opérationnels internes (production, entreposage), (2) coordination dyadique buyer-supplier (contrats, VMI), (3) orchestration du réseau étendu (CPFR, extended enterprise — Christopher ch. 7, 11), (4) gouvernance stratégique et gestion de la vulnérabilité (risk profiling, scenario modeling — Sheffi ch. 2-3 ; Christopher ch. 10). Christopher présente aussi quatre stades d'intégration (Fig. 1.9). |
| H4 : Niveaux fonctionnellement différenciés | 1 | Chaque niveau exerce des fonctions qualitativement distinctes : les flux physiques transforment/déplacent la matière ; la coordination synchronise l'information entre partenaires ; l'orchestration réseau conçoit l'architecture des relations ; la gouvernance stratégique gère l'incertitude et la résilience. Chopra distingue explicitement fonctions facilities, inventory, transportation, information, sourcing, pricing (ch. 3). |
| H5 : Causalité bidirectionnelle entre niveaux | 1 | Forte bidirectionnalité documentée. L'effet bullwhip illustre la propagation bottom-up : la variabilité de la demande locale s'amplifie vers les niveaux amont (Chopra ch. 10 ; Christopher ch. 7 — logistics systems dynamics). Inversement, les décisions stratégiques de conception réseau (top-down) contraignent les possibilités opérationnelles (Chopra ch. 5 ; Sheffi — decisions on sourcing affect operational vulnerability). |

**Score A1 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Aucune hésitation majeure. Le système est un cas d'école de profondeur hiérarchique multi-niveaux. La seule nuance est que la hiérarchie n'est pas strictement emboîtée (c'est un réseau plus qu'une pyramide), mais les niveaux causaux sont clairement distincts et documentés.

---

## A2 — Capacité de propagation (formulation V2.1.1 : invariance d'échelle)

| Sous-critère | Score | Justification |
|---|---|---|
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1 | Amplement documenté. Christopher (ch. 8) : le volcan islandais 2010 perturbe un fournisseur de composants aériens et se propage jusqu'aux usines Nissan au Japon. Sheffi : le tremblement de terre de Taiwan 1999 stoppe la ligne d'assemblage Dell aux USA via TSMC. Une perturbation chez un fournisseur de 2e rang affecte production, distribution, ventes. |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique | 1 | L'effet bullwhip est le mécanisme canonique : la variabilité de la demande au niveau retail se propage et s'amplifie au niveau manufacturer puis supplier (Chopra ch. 10). Christopher (ch. 7) décrit la dynamique des systèmes logistiques où de petites fluctuations en aval provoquent des oscillations majeures en amont, traversant tous les échelons de la chaîne. |
| P3 : Propagation modifie l'état global observable | 1 | Les disruptions majeures modifient l'état global de la supply chain de façon observable : arrêt de production, ruptures de stock généralisées, variations de prix globales. Sheffi documente comment la fermeture d'une usine Philips (incendie 2000) a perturbé l'ensemble du marché mondial des puces RF. Christopher (ch. 10) : les disruptions se propagent à l'ensemble du réseau et affectent la performance financière globale. |
| P4 : Isolement difficile sans modification structurelle | 1 | L'interdépendance fonctionnelle rend l'isolement très difficile. Christopher (ch. 8) : la complexité réseau (outsourcing, tiers 2-3 invisibles) empêche de contenir les perturbations. Sheffi : les supply chains lean éliminent les buffers, rendant l'isolement encore plus difficile. Même des décisions volontaires de dual-sourcing ou de safety stock constituent des « modifications structurelles » pour créer de l'isolement. |
| P5 : Couplage fonctionnel non trivial | 1 | Le couplage est hautement non trivial : il repose sur des flux physiques, informationnels et financiers simultanés (Chopra ch. 1). Christopher (ch. 7) : la synchronisation de la supply chain exige le partage d'information de demande, de schedules de production, de BOM changes. Les couplages sont souvent non linéaires (bullwhip amplification) et émergents (cascades imprévues via fournisseurs de rang 2-3). |

**Score A2 = 1.00 / 1.00**

**Hésitations / ambiguïtés :** Score maximum sans ambiguïté. La supply chain globale est un cas paradigmatique de propagation multi-échelle. La seule nuance : la propagation est souvent plus rapide et plus intense dans les supply chains lean que dans celles avec buffers significatifs, mais le phénomène est documenté dans tous les cas.

---

## A3 — Intégration

| Sous-critère | Score | Justification |
|---|---|---|
| I1 : Mécanisme explicite de coordination | 1 | De nombreux mécanismes explicites existent : CPFR (Collaborative Planning, Forecasting & Replenishment — Christopher ch. 4 ; Chopra ch. 10), VMI (Vendor Managed Inventory), S&OP (Sales & Operations Planning — Chopra ch. 9), systèmes ERP, EDI, extranets. Christopher (ch. 7) décrit en détail les fondements de la synchronisation. |
| I2 : Réduction de variance observable | 1 | La réduction de variance est un objectif explicite et documenté. Christopher (ch. 10) : le six sigma vise à réduire la variabilité des processus SC. Le CPFR réduit la variance des prévisions et des stocks (Christopher ch. 4 : réduction de 20-25% des coûts de stock). La synchronisation réduit l'amplification bullwhip. Chopra (ch. 10) : les leviers de coordination réduisent la distorsion d'information. |
| I3 : Synchronisation multi-niveaux | 0.5 | La synchronisation multi-niveaux est un objectif poursuivi mais imparfaitement atteint. Christopher (ch. 7) présente la supply chain synchrone comme idéal, avec transparence réseau et partage d'information à travers les tiers. En pratique, la synchronisation complète reste difficile (Christopher ch. 12 : barriers to integration). Chopra (ch. 10) : les obstacles à la coordination persistent (incentive obstacles, information processing obstacles). Score 0.5 car le mécanisme existe mais avec des limitations significatives documentées. |
| I4 : Boucles de rétroaction globales | 0.5 | Des boucles de rétroaction globales existent (SCEM — Supply Chain Event Management, Christopher ch. 9 ; monitoring des KPIs globaux ; alertes automatisées). Cependant, Sheffi documente que beaucoup d'entreprises n'ont pas de visibilité au-delà du tier 1 (Dell ignorait sa dépendance à TSMC). Christopher (ch. 10) : la visibilité réseau reste un défi. Les boucles sont souvent incomplètes et retardées. |
| I5 : Maintien d'un état global cohérent | 0.5 | Le système tend vers un état global cohérent (matching offre-demande) mais cet état est fragile et fréquemment perturbé. Le bullwhip effect (Chopra ch. 10) montre justement l'échec partiel du maintien de cohérence. Les disruptions documentées par Sheffi montrent que la cohérence globale se rompt régulièrement. Le système est en tension permanente entre forces intégratrices et forces de fragmentation. |

**Score A3 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** Hésitation sur I3 entre 0.5 et 1 : la synchronisation est techniquement possible et documentée chez les leaders (Dell, Tesco, 7-Eleven), mais la majorité des supply chains restent partiellement synchronisées. Le score 0.5 reflète cette réalité mixte. I5 est le sous-critère le plus discutable : le système vise la cohérence globale mais l'atteint imparfaitement ; c'est une propriété émergente fragile plutôt qu'un état maintenu de façon robuste.

---

## A4 — Normativité

| Sous-critère | Score | Justification |
|---|---|---|
| N1 : Attracteur dynamique existant | 1 | L'attracteur principal est le matching offre-demande avec minimisation des coûts totaux et maximisation du surplus SC (Chopra ch. 1 : « l'objectif de toute supply chain est de maximiser la valeur globale générée »). Christopher (ch. 1) : la supply chain converge vers un état de service client optimal à coût minimal. C'est un attracteur fonctionnel clair vers lequel le système gravite. |
| N2 : Correction active d'écart | 1 | De multiples mécanismes de correction active sont documentés : reorder points et safety stock pour corriger les écarts d'inventaire (Chopra ch. 12), SCEM qui détecte les déviations plan-réel et déclenche des actions correctives (Christopher ch. 9), six sigma DMAIC pour corriger les écarts de processus (Christopher ch. 10). Dell ajuste ses prix en temps réel pour corriger les déséquilibres offre-demande (Christopher ch. 4). |
| N3 : Hiérarchie de priorités régulatoires | 1 | Une hiérarchie de priorités est clairement documentée. Chopra (ch. 2) : le strategic fit hiérarchise les objectifs (responsiveness vs. efficiency). Christopher (ch. 2) : la matrice de service-coût priorise les actions selon les segments clients (Pareto — clients prioritaires vs. autres). Sheffi : la hiérarchie likelihood/severity structure la réponse aux disruptions (Fig. 15.1 UPS). Les entreprises maintiennent des priorités explicites entre service level, coût, et résilience. |
| N4 : Mécanisme interne de stabilisation | 1 | Safety stock (Chopra ch. 12), postponement/delayed configuration (Christopher ch. 9 ; Sheffi ch. 12), flexible contracts (Sheffi ch. 6 — HP spécifie des rampes de 50% en 2 semaines), dual sourcing, redundant capacity (Sheffi ch. 10 — Boston Scientific maintient des lignes de production redondantes). Ces mécanismes stabilisent activement le système face aux perturbations. |
| N5 : Résistance aux perturbations prolongées | 0.5 | Le système résiste aux perturbations courtes et modérées grâce aux buffers et à la flexibilité (Sheffi ch. 10-13). Cependant, face aux perturbations prolongées (pandémies, guerres commerciales, disruptions majeures de type Kobe/9-11), la résistance est partielle. Sheffi documente que les entreprises peinent à absorber les disruptions de longue durée sans modifications structurelles. Christopher (ch. 10) : la résilience de la SC est souvent insuffisante face aux perturbations systémiques. Score 0.5 car la résistance existe mais avec des limites claires pour les perturbations prolongées. |

**Score A4 = 0.90 / 1.00**

**Hésitations / ambiguïtés :** N5 est le point d'hésitation principal. Les supply chains les plus matures (Toyota, Dell, UPS) résistent remarquablement bien, mais le système « global supply chain » dans son ensemble inclut aussi des acteurs moins résilients. Le score 0.5 pour N5 reflète cette hétérogénéité.

**Distinction normativité endogène / imposée :** La normativité est largement **imposée** (designed) plutôt qu'endogène. Les objectifs de matching offre-demande, les KPIs, les procédures CPFR, les contrats — tout cela est conçu et imposé par des agents décisionnels humains. Cependant, certains comportements normatifs sont émergents : l'attracteur offre-demande émerge de l'interaction des agents même sans coordination centrale parfaite (mécanisme de prix). Le bullwhip effect est lui-même une normativité émergente dysfonctionnelle. L'essentiel de la normativité opérationnelle reste néanmoins d'origine exogène/humaine.

---

## A5 — Capacité de révision (formulation V2.1.1 : plasticité endogène)

| Sous-critère | Score | Justification |
|---|---|---|
| R1 : Ajustement paramétrique local | 1 | Ajustements fréquents et bien documentés : modification des reorder points, ajustement des safety stocks selon la variabilité observée (Chopra ch. 12), modification des prix en temps réel (Dell — Christopher ch. 4), ajustement des fréquences de livraison. Ces ajustements sont continus et locaux. |
| R2 : Modification durable de configuration interne | 1 | Passage d'un mode forecast-driven à demand-driven (Christopher ch. 4-5 — cas WDF), adoption de VMI remplaçant le système de commandes classique (Christopher ch. 4), intégration fonctionnelle progressive (stages 1→4, Fig. 1.9). Dell a modifié durablement sa configuration avec le build-to-order et les vendor hubs. |
| R3 : Reconfiguration de réseau ou de structure | 1 | Reconfiguration documentée à grande échelle : relocalisation de production (offshoring puis reshoring — Christopher ch. 9), restructuration des réseaux de distribution (Chopra ch. 4-5), passage de single-source à multi-source (Sheffi ch. 6), ajout/retrait de tiers logistiques (3PL → 4PL, Christopher ch. 11). Toyota a reconfiguré ses usines globales pour la flexibilité multi-marchés (Chopra ch. 5). |
| R4 : Modification des mécanismes de régulation | 0.5 | Les mécanismes de régulation évoluent : passage de l'inspection qualité au six sigma/process control (Christopher ch. 10), adoption du SCEM remplaçant la visibilité statique (Christopher ch. 9), évolution des métriques de performance vers des mesures time-based et customer-based (Christopher ch. 5). Cependant, ces modifications sont principalement initiées par des décisions managériales externes au système plutôt que par le système lui-même de façon autonome. Score 0.5 car la modification existe mais sa dimension « endogène » est discutable. |
| R5 : Capacité à produire de nouvelles règles | 0.5 | Le système produit de nouvelles pratiques et standards : émergence du CPFR comme nouveau protocole de coordination (Christopher ch. 4), développement de la notion de supply chain resilience post-9/11 (Sheffi), création de nouveaux modèles hybrides lean-agile (Christopher ch. 5). Toutefois, ces innovations sont portées par des acteurs humains (chercheurs, managers, consortiums industriels comme VICS) et non par le système de façon autonome. Score 0.5 car la production de nouvelles règles est réelle mais dépend de l'intervention humaine consciente. |

**Score A5 = 0.80 / 1.00**

**Hésitations / ambiguïtés :** R4 et R5 posent la question fondamentale de l'agentivité : la supply chain globale modifie-t-elle ses propres règles, ou bien ce sont les agents humains qui la composent qui modifient les règles ? La distinction est importante pour la plasticité « endogène ». On accorde 0.5 car le système, en tant que réseau d'organisations, produit effectivement de nouvelles configurations et règles, mais cette production passe par des processus de décision humains délibérés. Si l'on considère le système comme incluant ses agents humains, R4 et R5 mériteraient 1 ; si l'on considère le système comme infrastructure technique pure, ils mériteraient 0.

---

## Synthèse

| Axe | Score |
|-----|-------|
| A1 | 1.00 |
| A2 | 1.00 |
| A3 | 0.70 |
| A4 | 0.90 |
| A5 | 0.80 |

### Gradients (calculés)

| Gradient | Valeur |
|----------|--------|
| Δ₂₃ = A2 − A3 | +0.30 |
| Δ₄₅ = A4 − A5 | +0.10 |
| Δ₁₂ = A1 − A2 | 0.00 |
| Δ₃₅ = A3 − A5 | −0.10 |
| Δ₄₃ = A4 − A3 | +0.20 |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Système complexe à haute propagation et normativité forte, mais intégration imparfaite
- **Régime secondaire :** Système adaptatif à plasticité modérée (révision dépendante de l'intervention humaine)
- **Marge :** Le gradient Δ₂₃ = +0.30 est le plus significatif : la capacité de propagation excède nettement l'intégration, ce qui est la signature du bullwhip effect et des cascades de disruption. Le système propage mieux qu'il n'intègre.
- **Surprise par rapport au jugement intuitif :** Non. Le profil est conforme à l'intuition : une supply chain globale est un système hautement structuré (A1 max) avec une propagation extrême (A2 max), des mécanismes de contrôle normatif puissants mais une intégration effective inférieure aux ambitions déclarées. L'écart A2 > A3 capture précisément la fragilité systémique documentée par les trois sources.

---

## Notes libres

- **Profil caractéristique :** Le pattern {A1=1, A2=1, A3<A2, A4 élevé, A5 modéré} semble typique des grands systèmes économiques distribués : forte structure, forte propagation, mais l'intégration ne suit pas la propagation, et la plasticité dépend d'interventions humaines délibérées.
- **Tension lean vs. resilient :** Sheffi documente explicitement la tension entre efficience (lean, low inventory) et résilience (buffers, redundancy). Cette tension est au cœur de la normativité du système : les priorités régulatoires sont elles-mêmes en conflit.
- **Question ouverte — frontière du système :** Inclut-on les agents humains décisionnaires dans le « système » ? Si oui, A5 (plasticité) augmente significativement. Si non, le système est surtout une infrastructure dont la plasticité est externalisée vers ses opérateurs.
- **Le bullwhip comme marqueur systémique :** L'effet bullwhip (Chopra ch. 10, Christopher ch. 7) est le phénomène le plus révélateur du profil : il montre que la propagation (A2) excède l'intégration (A3) — les perturbations se propagent plus vite et plus fort que le système ne peut les absorber et les coordonner.
- **Comparaison possible :** À comparer avec SYS047 (European electrical grid) qui devrait présenter un profil similaire en A1-A2 mais potentiellement une meilleure intégration (A3) grâce aux mécanismes de contrôle automatique de fréquence.
