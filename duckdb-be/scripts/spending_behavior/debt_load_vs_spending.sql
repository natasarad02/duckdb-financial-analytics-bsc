-- Q3
SELECT
    a.user_id, a.total_debt,
    SUM(CAST(REPLACE(t.amount, '$', '') AS DOUBLE)) AS total_spending,
	a.per_capita_income,
	CASE
        WHEN a.per_capita_income < 20000 THEN 'Low Income'
        WHEN a.per_capita_income < 50000 THEN 'Medium Income'
        ELSE 'High Income'
    END AS income_category
	 
FROM Account a
LEFT JOIN transactions_parquet t ON a.user_id = t.user_id
GROUP BY a.user_id, a.total_debt, a.per_capita_income
HAVING COUNT(t.id) > 0
ORDER BY a.total_debt;