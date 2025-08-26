import sys
import requests
import json

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey="
api = "7639d0adb4281457d64bc05a627633c83effb76882d924cb963521df1c16745f"
# python bitcoin.py 1

try:

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    response = requests.get(f"{url}{api}")
    response.raise_for_status()
    bitcoin_data = response.json()

    # print(json.dumps(bitcoin_data, indent=2))
    result = n * float(bitcoin_data["data"]["priceUsd"])
    print(f"${result:,.4f}")


except requests.RequestException:
    sys.exit("API request failed")
