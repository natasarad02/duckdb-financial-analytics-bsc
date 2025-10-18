import psycopg2
import pandas as pd

connection = psycopg2.connect(
    host="postgres",
    port=5432,
    database="users_data",
    user="postgres",
    password="super"
)

cursor = connection.cursor()

def create_tables(cursor, filepath):
    with open(filepath, 'r') as f:
        sql = f.read()
    cursor.execute(sql)


def insert_data(df, table_name):
    cols = ', '.join(df.columns)
    placeholders = ', '.join(['%s'] * len(df.columns))
    query = f'INSERT INTO "{table_name}" ({cols}) VALUES ({placeholders})'
    
    for row in df.itertuples(index=False):
        cursor.execute(query, row)


# Creating tables
create_tables(cursor, 'data_scripts/postgres/create_tables.sql')


# Reading data
user_df = pd.read_csv("data/raw/user.csv")

address_df = pd.read_csv("data/raw/address.csv")
account_df = pd.read_csv("data/raw/account.csv")

# Removing dollar signs
address_df["per_capita_income"] = address_df["per_capita_income"].replace('[\$,]', '', regex=True).astype(float)
account_df["yearly_income"] = account_df["yearly_income"].replace('[\$,]', '', regex=True).astype(float)
account_df["total_debt"] = account_df["total_debt"].replace('[\$,]', '', regex=True).astype(float)
account_df["credit_score"] = account_df["credit_score"].astype(float)
insert_data(user_df, "User")      
insert_data(address_df, "Address")
insert_data(account_df, "Account")


connection.commit()
cursor.close()
connection.close()