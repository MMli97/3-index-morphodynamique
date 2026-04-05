

# Scoring Notes — [SYS021] THERMOSTAT

## Identification

- **System ID :** SYS021

- **System name :** Thermostat domestique (on-off control)

- **Domain :** technological

- **Scale :** micro / meso

- **Confidence :** high

## Sources

1. Åström & Murray — *Feedback Systems*

2. Wiener — *Cybernetics* (implicite : paradigme feedback)

3. Bejan — (contexte thermodynamique)

---

# **A1 — Profondeur hiérarchique**

| Sous-critère | Score | Justification                                                               |
| ------------ | ----- | --------------------------------------------------------------------------- |
| H1           | 1     | Capteur / contrôleur / actionneur = ≥2 niveaux                              |
| H2           | 0.5   | Niveau physique (température) + niveau logique (comparaison erreur)         |
| H3           | 0     | Pas de 4 niveaux distincts                                                  |
| H4           | 0.5   | Différenciation fonctionnelle (mesure vs action)                            |
| H5           | 0.5   | Boucle fermée → causalité bidirectionnelle (température ↔ action chauffage) |

**Score A1 = 0.5**

**Lecture :** hiérarchie minimale, typique des systèmes cybernétiques simples.

---

# **A2 — Propagation**

| Sous-critère | Score | Justification                                             |
| ------------ | ----- | --------------------------------------------------------- |
| P1           | 1     | Variation locale (température) déclenche action chauffage |
| P2           | 0.5   | Traverse capteur → contrôleur → actionneur                |
| P3           | 1     | Impact global : température de la pièce modifiée          |
| P4           | 0.5   | Isolement possible (débrancher thermostat)                |
| P5           | 1     | Couplage non trivial via boucle de feedback               |

**Score A2 = 0.8**

**Lecture :** propagation forte mais confinée (système local fermé).

---

# **A3 — Intégration**

| Sous-critère | Score | Justification                                   |
| ------------ | ----- | ----------------------------------------------- |
| I1           | 1     | Comparaison explicite erreur (r − y)            |
| I2           | 1     | Réduction de variance thermique                 |
| I3           | 0     | Pas de multi-niveaux                            |
| I4           | 1     | Boucle de rétroaction globale centrale          |
| I5           | 1     | Maintien d’un état cohérent (température cible) |

**Score A3 = 0.8**

**Lecture :** intégration très forte malgré simplicité structurelle.

---

# **A4 — Normativité**

| Sous-critère | Score | Justification                                           |
| ------------ | ----- | ------------------------------------------------------- |
| N1           | 1     | Attracteur = température de consigne                    |
| N2           | 1     | Correction active via on-off control                    |
| N3           | 0     | Pas de hiérarchie de normes                             |
| N4           | 1     | Stabilisation par feedback                              |
| N5           | 0.5   | Résistance limitée (oscillations, instabilité possible) |

**Score A4 = 0.7**

**Normativité :** endogène (boucle interne), mais très simple.

---

# **A5 — Capacité de révision**

| Sous-critère | Score | Justification                              |
| ------------ | ----- | ------------------------------------------ |
| R1           | 0.5   | Ajustement possible (consigne utilisateur) |
| R2           | 0     | Pas de mémoire structurelle                |
| R3           | 0     | Pas de reconfiguration                     |
| R4           | 0     | Mécanisme fixe                             |
| R5           | 0     | Aucune production de nouvelles règles      |

**Score A5 = 0.1**

**Lecture :** quasi absence de plasticité.

---

# **Synthèse**

| Axe | Score |
| --- | ----- |
| A1  | 0.5   |
| A2  | 0.8   |
| A3  | 0.8   |
| A4  | 0.7   |
| A5  | 0.1   |

---

## **Gradients**

- Δ₂₃ = 0.8 − 0.8 = **0.0**

- Δ₄₅ = 0.7 − 0.1 = **+0.6**

- Δ₁₂ = 0.5 − 0.8 = **−0.3**

- Δ₃₅ = 0.8 − 0.1 = **+0.7**

- Δ₄₃ = 0.7 − 0.8 = **−0.1**

---

# **Classification**

- **Régime primaire :** Équilibre (forte intégration + normativité simple)

- **Régime secondaire :** Rigidité normative

- **Marge :** élevée

---

# **Lecture morphodynamique**

Le thermostat est un cas presque **canonique** dans ton espace :

### 1. Système de référence pour A3–A4

- Boucle de feedback pure

- Norme simple (setpoint)

- Intégration maximale pour une structure minimale

→ C’est une sorte de **point de calibration du plan Δ₂₃ ≈ 0**

---

### 2. Dissociation forte A4 vs A5

- Normativité élevée

- Plasticité quasi nulle

→ Δ₄₅ très positif = signature de **rigidité fonctionnelle**

---

### 3. Limite structurelle claire

- Pas de montée en complexité

- Pas d’apprentissage

- Pas de multi-niveaux

→ système **clos, local, non évolutif**

---

### 4. Cas théorique important pour ton modèle

Le thermostat joue un rôle crucial dans ton corpus :

- **prototype du feedback pur**

- **borne basse de A1 et A5**

- **référence pour distinguer :**
  
  - systèmes cybernétiques simples
  
  - vs systèmes adaptatifs (immunitaire, LLM…)

---


