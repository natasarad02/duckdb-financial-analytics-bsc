import pandas as pd
import requests
import random
import time

def get_city_state_from_coords(lat, lon):
    try:
        url = "https://nominatim.openstreetmap.org/reverse"
        params = {
            "lat": lat,
            "lon": lon,
            "format": "json",
            "zoom": 10,
            "addressdetails": 1
        }
        headers = {"User-Agent": "Mozilla/5.0 (compatible; address-geocoder/1.0)"}
        response = requests.get(url, params=params, headers=headers, timeout=5)

        if response.status_code == 200:
            data = response.json()
            address = data.get("address", {})

            city = address.get("city") or address.get("town") or address.get("village") or ""
            state = address.get("state") or ""

            return city, state
        else:
            return "", ""
    except Exception:
        return "", ""


## Splitting users_data.csv

users = pd.read_csv("data/raw/users_data.csv")

# Creating user.csv (data for User entity in PostgreSQL)

user_df = users[["id", "birth_year", "birth_month", "gender", "current_age", "retirement_age"]].copy()
user_df = user_df.rename(columns={"id": "user_id"})
user_df.to_csv("data/raw/user.csv", index=False)

# Creating address.csv (data for Address entity in PostgreSQL)

address_df = users[["id", "address", "latitude", "longitude", "per_capita_income"]].copy()
address_df = address_df.rename(columns={"id": "user_id"})
address_df.insert(0, "address_id", range(1, len(address_df) + 1))

cities = []
states = []
total = len(address_df)

for i, row in address_df.iterrows():
    city, state = get_city_state_from_coords(row["latitude"], row["longitude"])
    cities.append(city)
    states.append(state)
    progress = ((i + 1) / total) * 100
    print(city)
    print(state)
    print(f"Progress: {progress:.2f}% ({i + 1}/{total})", end="\r")

    time.sleep(1)

address_df["city"] = cities
address_df["state"] = states
address_df.to_csv("data/raw/address.csv", index=False)


# Creating account.csv (data for Account entity in PostgreSQL)

account_df = users[[
    "id", "yearly_income", "total_debt",
    "credit_score", "num_credit_cards"
]].copy()
account_df = account_df.rename(columns={"id": "user_id"})
account_df.insert(0, "account_id", range(1, len(account_df) + 1))
account_df.to_csv("data/raw/account.csv", index=False)