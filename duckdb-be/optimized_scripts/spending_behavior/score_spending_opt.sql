WITH transactions_clean AS (
    SELECT
        id,
        user_id,
        CAST(REPLACE(amount, '$', '') AS DOUBLE) AS amount_double
    FROM transactions_parquet
)
SELECT
    a.user_id,
    a.credit_score,
    c.num_cards_issued,
    AVG(t.amount_double) AS avg_transaction_amount,
    COUNT(t.id) AS total_transactions
FROM Account a
LEFT JOIN cards c ON a.user_id = c.user_id
JOIN transactions_clean t ON a.user_id = t.user_id  
GROUP BY a.user_id, a.credit_score, c.num_cards_issued
ORDER BY a.credit_score;