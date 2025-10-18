import time
from duckdb_data import get_connection

connection = get_connection()  

query = """
WITH active_cards AS (
    SELECT DISTINCT c.card_id
    FROM cards c
    JOIN transactions_parquet t ON c.user_id = t.user_id
)
SELECT 
    c.card_brand AS card_brand,
    SUM(c.num_cards_issued) AS total_cards_issued,
    COUNT(ac.card_id) AS total_cards_active
FROM cards c
LEFT JOIN active_cards ac ON c.card_id = ac.card_id
GROUP BY c.card_brand
ORDER BY c.card_brand;
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