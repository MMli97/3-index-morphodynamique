

# Scoring Notes — [SYS022] Cristal NaCl

## Identification

- **System ID :** SYS022

- **System name :** Cristal de Chlorure de Sodium (NaCl)

- **Domain :** scientific / physical

- **Subdomain :** Physique de la matière condensée / Cristallographie

- **Scale :** micro / meso

- **Date scored :** 2026-04-02

- **Scorer :** IA

- **Confidence globale :** high

## Sources

1. Introduction to Dislocations, Fourth Edition (Derek Hull, D J Bacon)

2. Introduction to Solid State Physics (Charles Kittel)

3. Solid State Physics (Neil W. Ashcroft, N. David Mermin)

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                                                                             |
| --------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | Présence de deux niveaux évidents : les ions individuels ($Na^+$ et $Cl^-$) et le réseau cristallin macroscopique périodique.                                                                                                 |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | La hiérarchie comprend les cœurs ioniques, les électrons de valence (qui dictent la répulsion de Pauli à courte portée), et la structure cristalline globale.                                                                 |
| H3 : ≥ 4 niveaux causaux distincts            | 0         | Au-delà des niveaux sous-atomique, ionique et du réseau macroscopique, aucun quatrième niveau fonctionnel indépendant n'émerge.                                                                                               |
| H4 : Niveaux fonctionnellement différenciés   | 0         | Le système est un réseau de Bravais cubique à faces centrées (CFC) avec une base diatomique ; il est homogène et répétitif, sans différenciation fonctionnelle des zones.                                                     |
| H5 : Causalité bidirectionnelle entre niveaux | 0.5       | Les interactions coulombiennes locales forment la géométrie globale du cristal, et cette géométrie globale impose en retour des contraintes strictes sur les vecteurs d'onde permis pour les électrons et les phonons locaux. |

**Score A1 = 0.50 / 1.00**

**Hésitations / ambiguïtés :** L'approche d'Ashcroft & Mermin confirme que la "causalité" dans un solide repose sur des contraintes électrostatiques et thermodynamiques, ce qui valide le demi-point en H5 sans pour autant impliquer une causalité systémique active.

---

## A2 — Capacité de propagation (invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                                                               |
| ------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | L'agitation thermique se propage sous forme de phonons (acoustiques et optiques) qui interagissent entre eux en raison de l'anharmonicité du potentiel cristallin.                              |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | Le mouvement et la multiplication des dislocations à l'échelle atomique (plans de glissement) se traduisent directement par une déformation plastique macroscopique du matériau.                |
| P3 : Propagation modifie l'état global observable             | 0.5       | Les excitations thermiques mineures n'altèrent pas l'état global, mais l'accumulation de contraintes mécaniques ou thermiques importantes entraîne une fracture ou une fusion.                  |
| P4 : Isolement difficile sans modification structurelle       | 1         | L'énergie de cohésion repose sur l'interaction coulombienne à longue portée (calculée via la constante de Madelung) ; isoler une partie du cristal rompt irrémédiablement cet équilibre global. |
| P5 : Couplage fonctionnel non trivial                         | 0         | Bien que la sommation de Madelung soit complexe mathématiquement, le couplage reste fondamentalement de nature physique (électrostatique linéaire) et non "informationnel".                     |

**Score A2 = 0.70 / 1.00**

**Hésitations / ambiguïtés :** L'anharmonicité décrite par Ashcroft & Mermin (qui explique la dilatation thermique et la conductivité thermique) montre une propagation très efficace (P1, P2) inhérente aux cristaux réels.

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                                                                        |
| ---------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 0         | L'ordre à longue distance résulte de la minimisation passive de l'énergie libre thermodynamique, sans mécanisme de coordination ou de signalisation active.                              |
| I2 : Réduction de variance observable    | 1         | La cristallisation fige les ions dans des puits de potentiel profonds, réduisant massivement l'entropie et les degrés de liberté translationnels par rapport aux états fluide ou gazeux. |
| I3 : Synchronisation multi-niveaux       | 0.5       | Le cristal de NaCl, ayant une base de deux atomes différents, permet l'existence de branches de phonons optiques où les ions de signes opposés vibrent en opposition de phase.           |
| I4 : Boucles de rétroaction globales     | 0         | Aucune boucle de rétroaction cybernétique ; le cristal est un système purement réactif.                                                                                                  |
| I5 : Maintien d'un état global cohérent  | 1         | L'énergie de cohésion du réseau (Madelung + répulsion de Born-Mayer) assure une intégrité structurelle massive face aux fluctuations de l'environnement standard.                        |

**Score A3 = 0.50 / 1.00**

**Hésitations / ambiguïtés :** Les phonons optiques (I3 = 0.5) sont une excellente illustration d'une synchronisation physique "câblée" dans la structure de NaCl.

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                                                           |
| -------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1 : Attracteur dynamique existant           | 1         | La configuration spatiale du réseau est un puits de potentiel (attracteur énergétique) résultant de l'équilibre exact entre l'attraction coulombienne et la répulsion due au principe d'exclusion de Pauli. |
| N2 : Correction active d'écart               | 0         | La restauration d'une liaison élastique suite à une contrainte dépend des forces de rappel harmoniques passives, ce n'est pas un processus actif.                                                           |
| N3 : Hiérarchie de priorités régulatoires    | 0         | N/A pour un système physique inerte.                                                                                                                                                                        |
| N4 : Mécanisme interne de stabilisation      | 0.5       | L'anharmonicité des liaisons (qui s'écarte de la loi de Hooke pure) permet au système de stabiliser sa structure face aux augmentations de température via la dilatation thermique.                         |
| N5 : Résistance aux perturbations prolongées | 0         | Face à une élévation de température au-delà de son point de fusion ou à un solvant polaire, le cristal se désintègre sans résistance adaptative.                                                            |

**Score A4 = 0.30 / 1.00**

**Hésitations / ambiguïtés :** L'apport d'A&M permet de justifier N4 via l'anharmonicité, qui offre une forme "primitive" de stabilisation thermique évitant l'effondrement immédiat du réseau.

---

## A5 — Capacité de révision (plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                                       |
| -------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 0.5       | La distance d'équilibre du réseau augmente continuement avec la température (dilatation thermique) en raison de l'asymétrie du potentiel interatomique.                 |
| R2 : Modification durable de configuration interne | 0.5       | Création thermodynamique de défauts ponctuels (défauts de Schottky) ou écrouissage via l'enchevêtrement de dislocations, modifiant l'état interne de manière rémanente. |
| R3 : Reconfiguration de réseau ou de structure     | 0         | Incapable d'initier une transition de phase structurelle de lui-même (les changements de réseau nécessitent des pressions externes extrêmes).                           |
| R4 : Modification des mécanismes de régulation     | 0         | Les lois de l'électrostatique quantique régissant le système sont immuables.                                                                                            |
| R5 : Capacité à produire de nouvelles règles       | 0         | Système abiotique inerte, aucune capacité évolutive ou cognitive.                                                                                                       |

**Score A5 = 0.20 / 1.00**

**Hésitations / ambiguïtés :** R2 est bien soutenu par la littérature sur la thermodynamique des défauts de Schottky dans les cristaux ioniques.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 0.50      |
| A2      | 0.70      |
| A3      | 0.50      |
| A4      | 0.30      |
| A5      | 0.20      |

### Gradients (calculés)

| **Gradient**  | **Valeur** |
| ------------- | ---------- |
| Δ₂₃ = A2 − A3 | 0.20       |
| Δ₄₅ = A4 − A5 | 0.10       |
| Δ₁₂ = A1 − A2 | -0.20      |
| Δ₃₅ = A3 − A5 | 0.30       |
| Δ₄₃ = A4 − A3 | -0.20      |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Entité hautement structurée par des lois thermodynamiques. L'apport d'Ashcroft & Mermin met en évidence un système dominé par la minimisation de l'énergie (A1, A3) et fortement conducteur de perturbations mécaniques et thermiques (A2) grâce à la dynamique de ses réseaux quantifiés (phonons) et de ses dislocations.

- **Régime secondaire :** Système strictement réactif et dénué d'autonomie, de finalité ou d'adaptabilité algorithmique (A4, A5 très faibles).

- **Marge :** La robustesse du cristal repose entièrement sur la profondeur des puits de potentiel électrostatique, sans aucune plasticité systémique de haut niveau.

- **Surprise par rapport au jugement intuitif :** L'analyse détaillée des textes de physique du solide montre qu'un "simple" grain de sel possède une dynamique interne (anharmonicité, phonons optiques, défauts thermodynamiques) extrêmement riche pour un objet inanimé, justifiant des scores non nuls dans des catégories inattendues comme la "stabilisation" ou "l'ajustement paramétrique".
