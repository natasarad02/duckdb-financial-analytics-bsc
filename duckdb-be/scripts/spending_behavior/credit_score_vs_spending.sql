-- Q1
SELECT
    a.user_id, a.credit_score, c.num_cards_issued, avg(CAST(REPLACE(t.amount, '$', '') AS DOUBLE)) as avg_transaction_amount,
    count(t.id) as total_transactions
FROM Account a
LEFT JOIN cards c ON a.user_id = c.user_id
LEFT JOIN transactions_parquet t ON a.user_id = t.user_id
GROUP BY a.user_id, a.credit_score, c.num_cards_issued
HAVING count(t.id) > 0
ORDER BY a.credit_score;