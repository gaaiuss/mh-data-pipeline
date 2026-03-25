import json

import requests
from bs4 import BeautifulSoup


def get_monsters() -> list[str]:
    url = "https://monsterhunter.fandom.com/wiki/Monster_List"

    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.title)

    links = soup.select("#mw-content-text > div > table > tbody > tr > td > a")

    monsters: list[str] = []

    for link in links:
        monsters.append(link.text)

    with open("output/monsters.json", "w") as file:
        json.dump(monsters, file)

    return monsters
