

# Scoring Notes — [SYS007] Internet BGP Routing

## Identification

- **System ID :** SYS007

- **System name :** Internet Border Gateway Protocol (BGP) Routing

- **Domain :** technological / infrastructure

- **Subdomain :** Réseaux informatiques (Routage inter-domaine)

- **Scale :** macro

- **Date scored :** 2026-04-01

- **Scorer :** IA (Gemini)

- **Confidence globale :** high

## Sources

1. `BGP_BU~1.txt` (Documentation/Bugs BGP)

2. `rfc1771.txt.txt` (RFC 1771 : A Border Gateway Protocol 4 - BGP-4)

3. `s1389-1286(99)00108-5` (Internet Routing Instability, Labovitz et al., 1999)

---

## A1 — Profondeur hiérarchique

| **Sous-critère**                              | **Score** | **Justification**                                                                                                                                                     |
| --------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1 : ≥ 2 niveaux causaux distincts            | 1         | Les routeurs (BGP speakers) forment le premier niveau, et les Systèmes Autonomes (AS) forment le second niveau logique.                                               |
| H2 : ≥ 3 niveaux causaux distincts            | 1         | Le système intègre les interfaces physiques/liens (niveau 1), les processus de routage locaux (niveau 2), et les politiques inter-AS (niveau 3).                      |
| H3 : ≥ 4 niveaux causaux distincts            | 1         | L'échelle s'étend à la table de routage globale d'Internet (Default-Free Zone) qui émerge des interactions inter-AS.                                                  |
| H4 : Niveaux fonctionnellement différenciés   | 1         | Les routeurs traitent les paquets de données et maintiennent les sessions TCP, tandis que le niveau AS définit les politiques (policies) économiques et de transit.   |
| H5 : Causalité bidirectionnelle entre niveaux | 1         | Une instabilité de lien local remonte vers la table globale (bottom-up), et un retrait de route (WITHDRAW) global modifie les tables locales des routeurs (top-down). |

**Score A1 = 5.0 / 5 = 1.00**

**Hésitations / ambiguïtés :** Aucune. La structure d'Internet via BGP est intrinsèquement hiérarchique et multi-échelles.

---

## A2 — Capacité de propagation (invariance d'échelle)

| **Sous-critère**                                              | **Score** | **Justification**                                                                                                                                        |
| ------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 : Perturbation locale affecte ≥ 1 autre module fonctionnel | 1         | Une modification d'état sur une interface déclenche immédiatement un message UPDATE ou NOTIFICATION vers les pairs adjacents.                            |
| P2 : Propagation traverse ≥ 1 niveau hiérarchique             | 1         | Les "flaps" (battements) d'un routeur isolé se propagent et modifient l'attribut de chemin (AS_PATH) au niveau macroscopique.                            |
| P3 : Propagation modifie l'état global observable             | 1         | Les mises à jour pathologiques peuvent provoquer une instabilité du routage à l'échelle de l'Internet entier (variance de la table globale).             |
| P4 : Isolement difficile sans modification structurelle       | 1         | Il est nécessaire d'introduire des mécanismes spécifiques (comme le Route Flap Damping) pour tenter d'isoler ces propagations.                           |
| P5 : Couplage fonctionnel non trivial                         | 1         | BGP dépend d'une session TCP (port 179) sous-jacente et interagit étroitement avec l'IGP (Internal Gateway Protocol) pour la résolution des "next-hops". |

**Score A2 = 5.0 / 5 = 1.00**

**Hésitations / ambiguïtés :** L'étude de Labovitz illustre parfaitement la propagation non triviale des pannes locales.

---

## A3 — Intégration

| **Sous-critère**                         | **Score** | **Justification**                                                                                                                                                                         |
| ---------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I1 : Mécanisme explicite de coordination | 1         | L'intégration est gérée par une machine à états finis stricte et des messages de contrôle continus (KEEPALIVE, UPDATE).                                                                   |
| I2 : Réduction de variance observable    | 0.5       | Le processus de sélection choisit *une seule* meilleure route (réduisant la complexité), mais les "flaps" augmentent la variance observable de manière pathologique.                      |
| I3 : Synchronisation multi-niveaux       | 1         | Protocole divisé en iBGP (synchronisation au sein de l'AS, souvent en full-mesh) et eBGP (synchronisation entre les AS).                                                                  |
| I4 : Boucles de rétroaction globales     | 0.5       | BGP est un protocole à vecteur de chemin. Les informations se propagent de manière linéaire/diffuse ; la rétroaction globale existe, mais de manière retardée et indirecte (convergence). |
| I5 : Maintien d'un état global cohérent  | 0.5       | Bien que BGP converge vers une base d'informations de routage (RIB) stable, il existe des asymétries transitoires, des trous noirs et des boucles momentanées durant la convergence.      |

**Score A3 = 3.5 / 5 = 0.70**

**Hésitations / ambiguïtés :** BGP garantit la cohérence éventuelle (eventual consistency), pas la cohérence instantanée.

---

## A4 — Normativité

| **Sous-critère**                             | **Score** | **Justification**                                                                                                                                                                                |
| -------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1 : Attracteur dynamique existant           | 1         | Le système tend toujours vers l'état de convergence totale de la table de routage (équilibre dynamique).                                                                                         |
| N2 : Correction active d'écart               | 1         | La perte d'un KEEPALIVE entraîne une purge immédiate des routes associées et le recalcul via le Decision Process pour trouver un chemin alternatif.                                              |
| N3 : Hiérarchie de priorités régulatoires    | 1         | Le "BGP Decision Process" est une hiérarchie stricte d'attributs (Local Preference > AS_PATH > Origin > MED > eBGP > iBGP).                                                                      |
| N4 : Mécanisme interne de stabilisation      | 1         | BGP inclut des compteurs (Hold Timer) et des mécanismes de pénalité (Route Dampening) pour supprimer les routes instables.                                                                       |
| N5 : Résistance aux perturbations prolongées | 0.5       | Le système résiste bien aux coupures physiques, mais est vulnérable aux perturbations logiques prolongées (fuites de routes, asymétries de politiques entraînant des instabilités persistantes). |

**Score A4 = 4.5 / 5 = 0.90**

**Hésitations / ambiguïtés :**

**Distinction normativité endogène / imposée :** La normativité est *imposée* par le code du protocole et la RFC, mais la correction en temps réel est opérée de façon endogène par le système.

---

## A5 — Capacité de révision (plasticité endogène)

| **Sous-critère**                                   | **Score** | **Justification**                                                                                                                                       |
| -------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1 : Ajustement paramétrique local                 | 1         | Les routeurs mettent à jour dynamiquement leur Loc-RIB et ajustent les routes en fonction des UPDATE reçus.                                             |
| R2 : Modification durable de configuration interne | 0.5       | Les tables d'adjacence évoluent, mais les règles de filtrage (route-maps, prefix-lists) doivent être modifiées manuellement par des opérateurs humains. |
| R3 : Reconfiguration de réseau ou de structure     | 0.5       | Le trafic bascule dynamiquement sur de nouveaux chemins, mais l'établissement de nouvelles sessions (peerings) nécessite une intervention exogène.      |
| R4 : Modification des mécanismes de régulation     | 0         | Un routeur BGP ne peut pas modifier seul son propre "Decision Process" (l'algorithme de sélection est statique et dicté par la RFC).                    |
| R5 : Capacité à produire de nouvelles règles       | 0         | Le système BGP ne génère aucune nouvelle règle protocolaire de lui-même.                                                                                |

**Score A5 = 2.0 / 5 = 0.40**

**Hésitations / ambiguïtés :** BGP est dynamique dans le routage du trafic, mais extrêmement statique dans sa propre logique opérationnelle et métaprotocolaire.

---

## Synthèse

| **Axe** | **Score** |
| ------- | --------- |
| A1      | 1.00      |
| A2      | 1.00      |
| A3      | 0.70      |
| A4      | 0.90      |
| A5      | 0.40      |

### Gradients (calculés)

| **Gradient**  | **Valeur** |
| ------------- | ---------- |
| Δ₂₃ = A2 − A3 | 0.30       |
| Δ₄₅ = A4 − A5 | 0.50       |
| Δ₁₂ = A1 − A2 | 0.00       |
| Δ₃₅ = A3 − A5 | 0.30       |
| Δ₄₃ = A4 − A3 | 0.20       |

### Classification (rempli APRÈS scoring)

- **Régime primaire :** Infrastructure hiérarchique et propagation rapide (A1 et A2 dominants).

- **Régime secondaire :** Haute normativité algorithmique (A4) freinée par un déficit d'intégration globale parfaite (A3).

- **Marge :** La plasticité endogène (A5) est très faible, typique d'un système cybernétique classique (non IA).

- **Surprise par rapport au jugement intuitif :** On pourrait penser que BGP est très résilient, mais le gradient A4-A5 et les sources (notamment l'étude de Labovitz) rappellent que le système dépend massivement de l'intervention humaine pour la révision et la gestion des crises graves de routage.

---

## Notes libres

Le routage BGP d'Internet est un exemple parfait de système complexe à l'échelle macroscopique. Sa propagation des pannes (A2) est très rapide, ce qui explique pourquoi une erreur de configuration humaine (AS de transit) peut provoquer une panne mondiale d'Internet en quelques minutes. La rigidité du système (A5 faible) est paradoxalement à la fois sa force (prédictibilité algorithmique de base) et sa principale faille face aux attaques de type BGP Hijacking.
