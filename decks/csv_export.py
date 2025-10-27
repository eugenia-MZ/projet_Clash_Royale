import json
import csv
"""
# -------------------- All data units -----------------------
# on récupère les données de all_data_units.json
with open('../units/all_data_units.json', 'r') as file:
    units = json.load(file)

# on extrait toutes les clés dans l'ordre du premier objet
colonnes = list(units[0].keys())

# Écrire le CSV en remplissant les valeurs manquantes
with open('../units/all_data_units.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=colonnes)
    writer.writeheader()
    for unit in units:
        ligne = {}
        for col in colonnes:
            if col in unit:
                ligne[col] = unit[col]
            else:
                ligne[col] = ""  # valeur vide si la clé n'existe pas
        writer.writerow(ligne)

print("Le fichier all_data_units.csv a été créé avec succès !")
"""
"""
# -------------------- Deck Méta -----------------------

# on récupère les données de all_decks dans deck_builder.json
with open("deck_meta_data.json", "r") as file:
    decks = json.load(file)

# colonnes dans le csv
colonnes = ["unit1", "unit2", "unit3", "unit4", "unit5", "unit6", "unit7", "unit8", "elixir_moyen"]

# création du CSV
with open("deck_meta_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=colonnes)
    
    writer.writeheader()

    for deck in decks:
        writer.writerow(deck)

print("Le fichier deck_meta_data.csv a été créé avec succès !")
"""

# -------------------- Deck Builder -----------------------

# on récupère les données de all_decks dans deck_builder.json
with open("deck_builder.json", "r") as file:
    all_decks = json.load(file)

# colonnes dans le csv
colonnes = ["deck_number", "unit_1", "unit_2", "unit_3", "unit_4", "unit_5", "unit_6", "unit_7", "unit_8", "elixir_moyen"]

with open("deck_builder.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=colonnes)
    writer.writeheader()

    for deck in all_decks:
        ligne = {
            "deck_number": deck["deck_number"],
            "elixir_moyen": deck["elixir_moyen"],
        }
        # Ajouter les unités dans le row
        for i, unit in enumerate(deck["units"], start=1):
            ligne[f"unit_{i}"] = unit

        writer.writerow(ligne)

print("Le fichier deck_builder.csv a été créé avec succès !")
