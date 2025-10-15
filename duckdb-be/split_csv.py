import pandas as pd
import random

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
address_df.to_csv("data/raw/address.csv", index=False)


# Creating account.csv (data for Account entity in PostgreSQL)

account_df = users[[
    "id", "yearly_income", "total_debt",
    "credit_score", "num_credit_cards"
]].copy()
account_df = account_df.rename(columns={"id": "user_id"})
account_df.insert(0, "account_id", range(1, len(account_df) + 1))
account_df.to_csv("data/raw/account.csv", index=False)