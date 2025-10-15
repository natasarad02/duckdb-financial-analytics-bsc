WITH transactions_clean AS (
    SELECT
        user_id,
        CAST(REPLACE(CAST(amount AS VARCHAR), '$', '') AS DOUBLE) AS amount_clean
    FROM transactions_parquet
),
user_spending AS (
    SELECT
        user_id,
        SUM(amount_clean) AS total_spending,
        COUNT(*) AS transaction_count
    FROM transactions_clean
    GROUP BY user_id
)
SELECT
    a.user_id,
    a.total_debt,
    us.total_spending,
    a.yearly_income,
    CASE
        WHEN a.yearly_income < 20000 THEN 'Low Income'
        WHEN a.yearly_income < 50000 THEN 'Medium Income'
        ELSE 'High Income'
    END AS income_category
FROM Account a
JOIN user_spending us ON a.user_id = us.user_id
ORDER BY a.total_debt;