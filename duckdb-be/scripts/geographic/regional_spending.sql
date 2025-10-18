WITH user_avg_transactions AS (
    SELECT
        ad.state AS region,
        t.user_id,
        AVG(CAST(REPLACE(t.amount, '$', '') AS DOUBLE)) AS avg_transaction_per_user
    FROM Address ad
    JOIN transactions_parquet t ON ad.user_id = t.user_id
    GROUP BY ad.state, t.user_id
),
region_avg_transactions AS (
    SELECT
        region,
        AVG(avg_transaction_per_user) AS avg_transaction_per_region
    FROM user_avg_transactions
    GROUP BY region
)
SELECT
    region,
    avg_transaction_per_region
FROM region_avg_transactions
ORDER BY avg_transaction_per_region DESC;