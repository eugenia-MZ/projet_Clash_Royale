import requests
from bs4 import BeautifulSoup
import json

url = "https://www.deckshop.pro/card/list"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

elixir_data = []

# Chaque coût d’élixir est indiqué par la classe text-fuchsia-600
for elixir_section in soup.find_all("div", class_="mb-4 flex items-center"):
    # Trouver la valeur du coût d’élixir
    elixir_value = elixir_section.find("span", class_="text-fuchsia-600")
    if not elixir_value:
        continue
    elixir_value = elixir_value.text.strip()

    # Trouver le bloc de cartes associé
    units_div = elixir_section.find_next("div", class_="flex flex-wrap items-center")
    if not units_div:
        continue

    # Extraire tous les liens des cartes
    unit_links = [a["href"].split("/")[-1] for a in units_div.find_all("a", href=True)]

    # Sauvegarder dans la liste
    elixir_data.append({
        "elixir": elixir_value,
        "units": unit_links
    })

print(elixir_data)
with open("elixir_data.json", "w") as file:
    json.dump(elixir_data, file)