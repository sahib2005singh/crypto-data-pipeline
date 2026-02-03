import requests
import json
import os
from datetime import datetime
import sys

def fetch_crypto(api_key=None):
    url = "https://api.coingecko.com/api/v3/coins/markets"

    headers = {"accept": "application/json"}
    if api_key:
        headers["x-cg-demo-api-key"] = api_key

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()

    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M")
    date = timestamp.split("_")[0]

    base_path = "/opt/airflow/data/raw"
    os.makedirs(f"{base_path}/{date}", exist_ok=True)

    file_path = f"{base_path}/{date}/{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f)

    print(f"Saved {len(data)} records to {file_path}")

if __name__ == "__main__":
    api_key = sys.argv[1] if len(sys.argv) > 1 else None
    fetch_crypto(api_key)
