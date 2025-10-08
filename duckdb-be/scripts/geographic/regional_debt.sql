SELECT
    ad.address AS region,
    AVG(a.total_debt) AS avg_total_debt,
    AVG(a.yearly_income) AS avg_yearly_income
FROM Address ad
JOIN Account a ON ad.user_id = a.user_id
GROUP BY ad.address
ORDER BY avg_total_debt DESC