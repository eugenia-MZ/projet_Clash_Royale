import json
import random

with open("../units/all_data_units.json", "r") as file:
    all_units = json.load(file)

units_category = {
    "win-condition": [],
    "big-tank": [],
    "mini-tank": [],
    "building": [],
    "spell": [],
    "anti-air-troop": []
}

for unit in all_units:
    category = unit["category"]

    if category in units_category:
        efficacity = unit["efficacity (75% WR + 25% UR)"]

        if isinstance(efficacity, str) and efficacity.endswith("%"):
            efficacity = float(efficacity.replace("%", ""))

        unit["efficacity_value"] = efficacity
        units_category[category].append(unit)

# tri par 'efficacity'
for category in units_category:
    units_category[category].sort(key=lambda x: x["efficacity_value"], reverse=True)


# fonction permettant de générer des decks aléatoires de 8 cartes en fonction des catégories
def deck_builder():

    while True:
        deck = [
            random.choice(units_category["win-condition"]),
            random.choice(units_category["big-tank"]),
            random.choice(units_category["mini-tank"]),
            random.choice(units_category["building"]),
            *random.sample(units_category["spell"], 2),
            *random.sample(units_category["anti-air-troop"], 2)
        ]
        
        # cas où l'elixir n'est pas défini (ex : l'unité "miroir")
        for unit in deck:
            if unit["elixir"] is None:
                unit["elixir"] = 0

        elixir_total = sum(float(unit["elixir"]) for unit in deck)
        elixir_moyen = elixir_total / len(deck)

        # Faire des decks entre 2.8 et 4.2 d'elixir (la moyenne des decks meta étant d'environ 3.5)
        if 2.8 <= elixir_moyen <= 4.2:
            return deck, elixir_moyen


all_decks = []

# Générer les decks (ici 200)
for i in range(200):
    deck, elixir_moy = deck_builder()
    all_decks.append({
        "deck_number": i + 1,
        "elixir_moyen": round(elixir_moy, 2),
        "units": [unit["name"] for unit in deck]
    })

for deck in all_decks:
    print(f"\nDeck {deck['deck_number']} (elixir moyen: {deck['elixir_moyen']:.2f})")
    for unit in deck["units"]:
        print(unit)

# les decks sont mis dans deck_builder.json
with open("deck_builder.json", "w") as file:
    json.dump(all_decks, file)

print("Les decks ont été sauvegardés dans deck_builder.json")
