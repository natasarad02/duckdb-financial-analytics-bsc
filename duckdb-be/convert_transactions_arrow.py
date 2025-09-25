import pandas as pd

parquet_path = "data/raw/transactions_data.parquet"
df = pd.read_parquet(parquet_path)

arrow_path = "data/raw/transactions_data.arrow"
df.to_feather(arrow_path)