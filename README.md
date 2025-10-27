# Projet Clash Royale
--- Groupe 7 : Alexis S., Rubens, Mehdi ---

Ce projet permet de **scraper, analyser et générer des decks Clash Royale** depuis [DeckShop.pro](https://www.deckshop.pro) et [StatsRoyale](https://statsroyale.com) puis de compiler les données en JSON et CSV.  
Ce README inclut un **diagramme des dépendances et flux de données** pour une compréhension rapide.

---

## 📂 Structure du projet

```
.
├── main.py                     # Scrape cartes par catégorie
├── units/
│   ├── rate_use.py              # Extrait win/use rate depuis HTML
│   ├── elixir.py                # Scrape cartes par coût en élixir
│   └── all_data_units.py        # Compile toutes les données des cartes
├── decks/
│   ├── decks_meta.py            # Scrape les decks du nouveau méta
│   ├── deck_builder.py          # Génère des decks aléatoires équilibrés
│   └── csv_export.py            # Convertit les fichiers JSON en CSV
├── html_scrap/                  # (Optionnel) fichiers HTML sauvegardés
├── data/                        # (Optionnel) fichiers JSON générés
└── README.md
```

---

## 🔄 Flux de données & dépendances

```text
main.py               ──┐
                        │
units/elixir.py       ──┼─> units/all_data_units.py ──> data/all_data_units.json ──┐
units/rate_use.py     ──┘                                                          │
                                                                                   ▼
decks/decks_meta.py ──> data/deck_meta_data.json                                   decks/deck_builder.py ──> data/deck_builder.json
                                                                                   │
                                                                                   ▼
                                                                                   decks/csv_export.py
```

### Explications
1. **main.py** → récupère les cartes par catégorie.  
2. **units/elixir.py** → récupère le coût en élixir par carte.  
3. **units/rate_use.py** → extrait les taux de victoire et d’utilisation depuis HTML.  
4. **units/all_data_units.py** → combine catégories, élixir, win/use rate et calcule l’efficacité pondérée → `data/all_data_units.json`.  
5. **decks/decks_meta.py** → scrape les decks méta → `data/deck_meta_data.json`.  
6. **decks/deck_builder.py** → génère des decks aléatoires équilibrés → `data/deck_builder.json`.  
7. **decks/csv_export.py** → convertit tous les JSON générés en CSV (`all_data_units.csv`, `deck_meta_data.csv`, `deck_builder.csv`).

---

## 🧩 Description des fichiers

### 1️⃣ `main.py`
- **Rôle :** Scraper les cartes par catégorie depuis DeckShop.  
- **Sortie :** console / optionnel HTML dans `html_scrap/`.

### 2️⃣ `units/rate_use.py`
- **Rôle :** Extrait les taux de victoire et d’utilisation depuis le fichier HTML des statistiques (`Stats_Royale_english.html`).  
- **Sortie :** `rate_use_data.json`.

### 3️⃣ `units/elixir.py`
- **Rôle :** Scrape les cartes par coût en élixir depuis DeckShop.  
- **Sortie :** `elixir_data.json`.

### 4️⃣ `units/all_data_units.py`
- **Rôle :** Combine les données des cartes (catégorie, élixir, win/use rate, efficacité pondérée) et ajoute des statistiques supplémentaires depuis DeckShop.  
- **Sortie :** `all_data_units.json`.

### 5️⃣ `decks/decks_meta.py`
- **Rôle :** Scrape les decks du nouveau méta et calcule leur élixir moyen.  
- **Sortie :** `deck_meta_data.json`.

### 6️⃣ `decks/deck_builder.py`
- **Rôle :** Génère 200 decks aléatoires équilibrés par catégorie et élixir moyen.  
- **Sortie :** `deck_builder.json`.

### 7️⃣ `decks/csv_export.py`
- **Rôle :** Convertit les JSON générés en fichiers CSV pour une utilisation facile dans Excel ou autres outils.  
- **Sortie :** `all_data_units.csv`, `deck_meta_data.csv`, `deck_builder.csv`.

---

## ⚙️ Installation

Cloner le dépôt :
```bash
git clone https://https://github.com/eugenia-MZ/projet_Clash_Royale.git
cd projet_Clash_Royale
```

---

## 🚀 Utilisation générale

```bash
python3 main.py
python3 units/rate_use.py
python3 units/elixir.py
python3 units/all_data_units.py
python3 decks/decks_meta.py
python3 decks/deck_builder.py
python3 decks/csv_export.py
```

---

## 🧠 Exemple de structure JSON

- **Carte (`all_data_units.json`) :**
```json
{
  "name": "archers",
  "category": "anti-air-troop",
  "elixir": "3",
  "win_rate": "52%",
  "use_rate": "18%",
  "efficacity (75% WR + 25% UR)": "46.5%"
}
```

- **Deck méta (`deck_meta_data.json`) :**
```json
{
  "unit1": "archers",
  "unit2": "baby-dragon",
  "unit3": "miner",
  "unit4": "zap",
  "elixir_moyen": 3.75
}
```

- **Deck aléatoire (`deck_builder.json`) :**
```json
{
  "deck_number": 1,
  "elixir_moyen": 3.65,
  "units": ["archers", "hog-rider", "cannon", "zap", "fireball", "minions", "baby-dragon", "musketeer"]
}
```
## CSV
Lien des CSV
https://docs.google.com/spreadsheets/d/1JNpWF3e28Uv3Px7UJx4xj_fGXOnz3ujcG-osAA4mRU8/edit?usp=sharing

---
## 👤 Auteurs
Alexis S., Rubens, Mehdi
💻 [GitHub](https://github.com/eugenia-MZ/)

