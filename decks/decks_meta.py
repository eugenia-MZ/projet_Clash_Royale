import requests
from bs4 import BeautifulSoup
import json

with open("../units/all_data_units.json", "r") as file:
    all_data_units = json.load(file)

# Créer un lookup pour accéder rapidement au coût d'élixir
elixir_lookup = {unit["name"]: unit["elixir"] for unit in all_data_units if unit.get("elixir")}

url_deck_meta = "https://www.deckshop.pro/best-decks/for/new-meta"
url_deck_meta_response = requests.get(url_deck_meta)
soup = BeautifulSoup(url_deck_meta_response.text, "html.parser")

deck_meta_data = []

decks = soup.find_all("div", class_="deck-container-wide")

for deck in decks:
    # Liste des unités du deck
    deck_units = [img["alt"].strip().lower().replace(" ", "-") for img in deck.find_all("img", alt=True)]
    
    # Calcul de l'élixir moyen
    total_elixir = 0
    count = 0
    for unit in deck_units:
        if unit in elixir_lookup:
            total_elixir += float(elixir_lookup[unit])
            count += 1
    elixir_moyen = round(total_elixir / count, 2) if count else None

    # dictionnaire pour le deck
    deck_dict = {f"unit{i+1}": unit for i, unit in enumerate(deck_units)}
    deck_dict["elixir_moyen"] = elixir_moyen

    deck_meta_data.append(deck_dict)

for i, deck in enumerate(deck_meta_data, start=1):
    print(f"Deck {i}: {deck}")

# les decks métas sont mis dans deck_meta_data.json
with open("deck_meta_data.json", "w") as file:
    json.dump(deck_meta_data, file)
