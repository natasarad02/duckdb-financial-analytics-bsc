SELECT
    c.card_brand,
    AVG(CAST(REPLACE(t.amount, '$', '') AS DOUBLE)) AS avg_transaction_amount,
    COUNT(t.amount) AS num_transactions
FROM cards AS c
JOIN transactions_arrow AS t
    ON c.user_id = t.user_id
GROUP BY c.card_brand
ORDER BY avg_transaction_amount DESC;
