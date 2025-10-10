WITH user_spending AS (
    SELECT
        user_id,
        SUM(CAST(REPLACE(amount, '$','') AS DOUBLE)) AS total_spent
    FROM transactions_parquet
    GROUP BY user_id
)
SELECT
    u.current_age,
    SUM(us.total_spent) AS total_spending
FROM User u
JOIN Account a USING(user_id)
JOIN user_spending us USING(user_id)
GROUP BY u.current_age
ORDER BY u.current_age;