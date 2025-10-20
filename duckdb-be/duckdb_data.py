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
connection.execute("DROP INDEX IF EXISTS idx_account_total_debt;")
connection.execute("DROP INDEX IF EXISTS idx_account_yearly_income;")


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
CREATE INDEX idx_account_total_debt
ON account(total_debt);
""")

connection.execute("""
CREATE INDEX idx_account_yearly_income
ON account(yearly_income);
""")

connection.execute("""
CREATE TABLE address AS 
SELECT * FROM postgres_scan('postgresql://postgres:super@postgres:5432/users_data', 'public', 'Address');
""")

connection.execute("""
CREATE TABLE transactions_parquet AS
SELECT * FROM read_parquet('data/raw/transactions_data.parquet');
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


def get_connection():
    return connection