import pandas as pd

csv_path = "data/raw/transactions_data.csv"

parquet_path = "data/raw/transactions_data.parquet"

ROW_NUM = 10000

df = pd.read_csv(csv_path, nrows = ROW_NUM)
df = df.rename(columns={"client_id": "user_id"})

df.to_parquet(parquet_path, index=False)