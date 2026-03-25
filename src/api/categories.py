# scraper/monsters.py
import requests

API_URL = "https://monsterhunter.fandom.com/api.php"


def categories() -> None:
    params = {
        "action": "query",
        "format": "json",
        "list": "allcategories",
        "aclimit": 500,  # Request a limit of 50 categories
        "formatversion": 2,
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        for category in data["query"]["allcategories"]:
            print(category)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
