import pandas as pd
from pymongo import MongoClient


client = MongoClient("mongodb://mongo:super@mongodb:27017/")
database = client["card_data"]
cards_collection = database["Card"]

cards_df = pd.read_csv("data/raw/cards_data.csv")

cards_collection.delete_many({})

card_documents = []

for _, row in cards_df.iterrows():
    doc = {
        "card_id": int(row["id"]),
        "user_id": int(row["client_id"]),
        "card_brand": row["card_brand"],
        "card_type": row["card_type"],
        "card_number": row["card_number"],
        "expires": row["expires"],
        "cvv": int(row["cvv"]),
        "has_chip": row["has_chip"] == "YES",
        "num_cards_issued": int(row["num_cards_issued"]),
        "credit_limit": float(row["credit_limit"].replace("$","")),
        "acct_open_date": row["acct_open_date"],
        "year_pin_last_changed": int(row["year_pin_last_changed"]),
        "card_on_dark_web": row["card_on_dark_web"].strip().lower() == "yes",
        "features": {
            "num_cards_issued": int(row["num_cards_issued"]),
            "year_pin_last_changed": int(row["year_pin_last_changed"]),
            "card_on_dark_web": row["card_on_dark_web"].strip().lower() == "yes"
        }
    }
    card_documents.append(doc)

if card_documents:
    cards_collection.insert_many(card_documents)