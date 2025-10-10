SELECT 
    c.card_brand,
    COUNT(t.id) AS num_transactions,
    ROUND(100.0 * COUNT(t.id) / SUM(COUNT(t.id)) OVER (), 2) AS pct_transactions
FROM transactions_parquet t
JOIN cards c ON t.card_id = c.card_id
GROUP BY c.card_brand
ORDER BY pct_transactions DESC;