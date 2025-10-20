import time
from duckdb_data import get_connection

connection = get_connection()  

query = """
WITH brand_counts AS (
    SELECT
        c.card_brand,
        COUNT(*) AS num_transactions
    FROM transactions_parquet t
    JOIN cards c ON t.card_id = c.card_id
    GROUP BY c.card_brand
)
SELECT
    card_brand,
    num_transactions,
    ROUND(100.0 * num_transactions / SUM(num_transactions) OVER (), 2) AS pct_transactions
FROM brand_counts
ORDER BY pct_transactions DESC;
"""

n_runs = 10
times = []

for _ in range(n_runs):
    start = time.time()
    connection.execute(query).fetchall()
    end = time.time()
    times.append(end - start)

avg_runtime = sum(times) / n_runs
print(f"Average runtime over {n_runs} runs: {avg_runtime:.4f} seconds")