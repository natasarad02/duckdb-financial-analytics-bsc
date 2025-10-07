import duckdb
import pandas as pd
import pymongo
from flask import Flask, request, jsonify

app = Flask(__name__)

connection = duckdb.connect(database='analytics.duckdb', read_only=False)

connection.execute("DROP TABLE IF EXISTS user;")
connection.execute("DROP TABLE IF EXISTS address;")
connection.execute("DROP TABLE IF EXISTS account;")
connection.execute("DROP TABLE IF EXISTS transactions_arrow;")
connection.execute("DROP TABLE IF EXISTS transactions_parquet;")
connection.execute("DROP TABLE IF EXISTS cards;")

connection.execute("""
INSTALL postgres_scanner;
LOAD postgres_scanner;
""")
connection.execute("""
CREATE TABLE user AS 
SELECT * FROM postgres_scan('postgresql://postgres:super@postgres:5432/users_data', 'public', 'User');
""")

connection.execute("""
CREATE TABLE account AS 
SELECT * FROM postgres_scan('postgresql://postgres:super@postgres:5432/users_data', 'public', 'Account');
""")

connection.execute("""
CREATE TABLE address AS 
SELECT * FROM postgres_scan('postgresql://postgres:super@postgres:5432/users_data', 'public', 'Address');
""")

transactions_parquet = pd.read_parquet('data/raw/transactions_data.parquet')
connection.register('transactions_parquet', transactions_parquet)

connection.execute("""
CREATE TABLE IF NOT EXISTS transactions_parquet AS
SELECT * FROM transactions_parquet
""")

transactions_arrow = pd.read_feather('data/raw/transactions_data.arrow')
connection.register('transactions_arrow', transactions_arrow)

connection.execute("""
CREATE TABLE IF NOT EXISTS transactions_arrow AS
SELECT * FROM transactions_arrow
""")

client = pymongo.MongoClient("mongodb://mongo:super@mongodb:27017/")
db = client['card_data']
cards_df = pd.DataFrame(list(db.Card.find()))
connection.register('cards', cards_df)

connection.execute("""
CREATE TABLE IF NOT EXISTS cards AS
SELECT * FROM cards
""")

'''
@app.route("/query", methods=["POST"])
def execute_query():
    data = request.json
    sql = data.get("sql")
    if not sql:
        return jsonify({"error": "No SQL query provided"}), 400
    
    try:
        result = connection.execute(sql).fetchall()
        columns = [desc[0] for desc in connection.description]
        return jsonify({"columns": columns, "rows": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)   



## Transactions amount by user and account
with open("scripts/transaction_amount.sql", "r") as f:
    query = f.read()

result_df = connection.execute(query).fetchdf()

print(result_df)

## Users with cards
with open("scripts/users_cards.sql", "r") as f:
    query = f.read()

result_df = connection.execute(query).fetchdf()

print(result_df)

## Average transaction per card brand
with open("scripts/average_transaction.sql", "r") as f:
    query = f.read()

result_df = connection.execute(query).fetchdf()

print(result_df)
'''