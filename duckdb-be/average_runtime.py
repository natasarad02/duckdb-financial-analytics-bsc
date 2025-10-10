import time
from duckdb_data import get_connection

connection = get_connection()  # reuse the same DuckDB session

query = """
WITH user_card_counts AS (
    SELECT user_id, COUNT(card_id) AS num_cards
    FROM cards
    GROUP BY user_id
),
user_spending AS (
    SELECT user_id, SUM(CAST(REPLACE(CAST(amount AS VARCHAR), '$', '') AS DOUBLE)) AS total_spent
    FROM transactions_parquet
    GROUP BY user_id
)
SELECT 'All Users' AS step, COUNT(*) AS users FROM "User"
UNION ALL
SELECT '2+ Cards', COUNT(*) 
FROM user_card_counts
WHERE num_cards >= 2
UNION ALL
SELECT 'High Spenders', COUNT(*) 
FROM user_spending
WHERE total_spent > 5000
UNION ALL
SELECT 'Low Credit Score', COUNT(*) 
FROM "Account"
WHERE credit_score < 700
UNION ALL
SELECT 'Compromised Cards', COUNT(*) 
FROM cards 
WHERE card_on_dark_web = TRUE;

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