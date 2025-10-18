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