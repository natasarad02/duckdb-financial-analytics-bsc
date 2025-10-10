WITH transactions_clean AS (
    SELECT
        user_id,
        CAST(REPLACE(CAST(amount AS VARCHAR), '$', '') AS DOUBLE) AS amount_clean
    FROM transactions_arrow
),
user_avg_spent AS (
    SELECT
        user_id,
        AVG(amount_clean) AS avg_spent
    FROM transactions_clean
    GROUP BY user_id
)
SELECT
    a.user_id,
    a.credit_score,
    a.total_debt,
    u.avg_spent,
    c.num_cards_issued AS num_credit_cards
FROM Account a
LEFT JOIN cards c ON a.user_id = c.user_id
LEFT JOIN user_avg_spent u ON a.user_id = u.user_id
WHERE a.credit_score < 650 AND a.total_debt > 10000
ORDER BY a.total_debt DESC, a.credit_score ASC;
