-- Q10
SELECT 
    u.current_age,
    SUM(CAST(REPLACE(t.amount, '$','') AS DOUBLE)) AS total_spending
FROM User u
JOIN Account a ON u.user_id = a.user_id
JOIN transactions_parquet t ON u.user_id = t.user_id
GROUP BY u.current_age
ORDER BY u.current_age;