import requests

def get_gold_price():

    try:

        # Gold price
        gold = requests.get(
            "https://api.gold-api.com/price/XAU",
            timeout=10
        ).json()

        # USD to PKR exchange rate
        forex = requests.get(
            "https://open.er-api.com/v6/latest/USD",
            timeout=10
        ).json()

        usd_pkr = forex["rates"]["PKR"]

        return f"""
Live Gold Data

Gold Price (USD per Troy Ounce):
{gold["price"]}

USD to PKR Exchange Rate:
1 USD = {usd_pkr} PKR
"""

    except Exception as e:

        return f"Unable to fetch live data.\n{e}"