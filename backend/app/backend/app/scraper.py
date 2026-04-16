import requests
import json
from bs4 import BeautifulSoup


def extract_recipe(url: str):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        scripts = soup.find_all("script", type="application/ld+json")

        for script in scripts:
            try:
                if not script.string:
                    continue

                data = json.loads(script.string)

                if isinstance(data, list):
                    data = data[0]

                if data.get("@type") == "Recipe":

                    return {
                        "title": data.get("name"),
                        "ingredients": data.get("recipeIngredient", []),
                        "steps": [
                            step.get("text") if isinstance(step, dict) else step
                            for step in data.get("recipeInstructions", [])
                        ],
                        "message": "Recipe extracted successfully"
                    }

            except:
                continue

        return {
            "title": "Recipe not found",
            "ingredients": [],
            "steps": [],
            "message": "No structured recipe data found"
        }

    except Exception as e:
        return {
            "title": "Error",
            "ingredients": [],
            "steps": [],
            "message": str(e)
        }
