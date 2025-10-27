import requests
from bs4 import BeautifulSoup
import json

# Charger les données d'élixir depuis elixir_data.json
with open("elixir_data.json", "r") as file:
    elixir_data = json.load(file)

# Charger les données de taux depuis rate_use_data.json
with open("rate_use_data.json", "r") as file:
    rate_use_data = json.load(file)

# Créer un dictionnaire pour retrouver rapidement le coût d’élixir par carte
elixir_lookup = {unit: entry["elixir"] for entry in elixir_data for unit in entry["units"]}

# Créer un lookup pour accéder rapidement aux taux par nom
rate_lookup = {unit["name"]: {"win_rate": unit["win_rate"], "use_rate": unit["use_rate"]} 
               for unit in rate_use_data}

# Toutes les catégories
anti_air_troop_units = ["fire-spirit", "spear-goblins", "bats", "archers", "minions", "goblin-gang", "firecracker", "skeleton-dragons", "tesla", "minion-horde", "rascals", "ice-golem", "mega-minion", "dart-goblin", "musketeer", "goblin-hut", "flying-machine", "furnace", "zappies", "inferno-tower", "wizard", "three-musketeers", "baby-dragon", "hunter", "witch", "electro-dragon", "executioner", "goblin-giant", "princess", "ice-wizard", "electro-wizard", "inferno-dragon", "phoenix", "magic-archer", "night-witch", "mother-witch", "ram-rider", "spirit-empress", "little-prince", "archer-queen", "goblinstein"]
big_tank_units = ["royal-giant", "elixir-golem", "giant", "rune-giant", "giant-skeleton", "goblin-giant", "pekka", "electro-giant", "golem", "mega-knight", "lava-hound", "goblinstein"]
building_units = ["cannon", "mortar", "tesla", "tombstone", "goblin-cage", "goblin-hut", "bomb-tower", "inferno-tower", "barbarian-hut", "elixir-collector", "goblin-drill", "x-bow"]
mini_tank_units = ["knight", "rascals", "elite-barbarians", "ice-golem", "mini-pekka", "goblin-cage", "valkyrie", "battle-ram", "hog-rider", "battle-healer", "goblin-demolisher", "baby-dragon", "dark-prince", "prince", "bowler", "executioner", "cannon-cart", "miner", "royal-ghost", "bandit", "fisherman", "lumberjack", "ram-rider", "goblin-machine", "spirit-empress", "golden-knight", "skeleton-king", "mighty-miner", "monk", "boss-bandit"]
spell_units = ["zap", "giant-snowball", "arrows", "royal-delivery", "earthquake", "fireball", "rocket", "mirror", "barbarian-barrel", "goblin-curse", "rage", "goblin-barrel", "vines", "clone", "tornado", "void", "freeze", "poison", "lightning", "the-log", "graveyard"]
win_condition_units = ["skeleton-barrel", "mortar", "royal-giant", "elixir-golem", "battle-ram", "hog-rider", "giant", "royal-hogs", "three-musketeers", "wall-breakers", "goblin-barrel", "goblin-drill", "balloon", "goblin-giant", "x-bow", "electro-giant", "golem", "miner", "ram-rider", "graveyard", "lava-hound"]

# Correspondance catégorie
category_lookup = {}

for unit in anti_air_troop_units:
    category_lookup[unit] = "anti-air-troop"

for unit in big_tank_units:
    category_lookup[unit] = "big-tank"

for unit in building_units:
    category_lookup[unit] = "building"

for unit in mini_tank_units:
    category_lookup[unit] = "mini-tank"

for unit in spell_units:
    category_lookup[unit] = "spell"

for unit in win_condition_units:
    category_lookup[unit] = "win-condition"

# Récupération des données depuis Deckshop
all_units = list(category_lookup.keys())
all_data_units = []

for unit in all_units:
    url_unit = f"https://www.deckshop.pro/card/detail/{unit}"
    response = requests.get(url_unit)
    soup = BeautifulSoup(response.text, "html.parser")

    # lookup pour accéder et récupérer les win rate et use rate de chaque unité
    win_rate = rate_lookup.get(unit, {}).get("win_rate")
    use_rate = rate_lookup.get(unit, {}).get("use_rate")

    win_rate_value = float(str(win_rate).replace("%", ""))
    use_rate_value = float(str(use_rate).replace("%", ""))

    # pondération pour la stat efficacity
    efficacity = f"{round(0.75 * win_rate_value + 0.25 * use_rate_value, 2)}%"

    data_unit = {
        "name": unit,
        "category": category_lookup.get(unit),
        "elixir": elixir_lookup.get(unit),
        "win_rate": rate_lookup.get(unit, {}).get("win_rate"),
        "use_rate": rate_lookup.get(unit, {}).get("use_rate"),
        "efficacity (75% WR + 25% UR)": efficacity
    }

    # Ajouter les stats depuis le tableau
    for row in soup.find_all("tr"):
        th = row.find("th", class_="text-gray-muted font-normal")
        td = row.find("td", class_="text-right")
        if th and td:
            key = ''.join(th.find_all(string=True, recursive=False)).strip()
            value = td.get_text(strip=True)
            data_unit[key] = value

    all_data_units.append(data_unit)

with open("all_data_units.json", "w") as file:
    json.dump(all_data_units, file)
print("Fichier créé avec succès !")
