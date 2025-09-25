SELECT
    u.user_id,
    u.current_age,
    u.retirement_age,
    SUM(CAST(REPLACE(t.amount, '$', '') AS DOUBLE)) as total_amount,
    COUNT(t.amount) AS num_transactions
FROM user AS u
LEFT JOIN transactions_parquet AS t
    ON u.user_id = t.user_id
LEFT JOIN account as a
    ON u.user_id = a.user_id
GROUP BY u.user_id, u.current_age, u.retirement_age
ORDER BY total_amount DESC;