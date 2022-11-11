from nutritionix import Nutritionix
import json

nix = Nutritionix(app_id="90f77e90", api_key="8580cb66ddeafe2c7e840a3ccdf1073f")

pizza = nix.search("McDonalds", brand_ids = "513fbc1283aa2dc80c000053")

results = pizza.json()

print(results["hits"][0])
print(results["hits"][0]["_id"])

milk = nix.item(id = results["hits"][0]["_id"]).json()
print(milk["nf_protein"])