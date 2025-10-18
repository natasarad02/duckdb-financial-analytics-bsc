SELECT
    CASE
        WHEN (u.retirement_age - u.current_age) < 10 THEN '0-10'
        WHEN (u.retirement_age - u.current_age) BETWEEN 10 AND 19 THEN '10-19'
        WHEN (u.retirement_age - u.current_age) BETWEEN 20 AND 29 THEN '20-29'
        WHEN (u.retirement_age - u.current_age) BETWEEN 30 AND 39 THEN '30-39'
        ELSE '40+'
    END AS retirement_groups,
    AVG(a.total_debt) AS avg_total_debt,
    STDDEV(a.total_debt) AS stddev_total_debt,
    AVG(a.total_debt) + STDDEV(a.total_debt) AS upper_bound,
     GREATEST(AVG(a.total_debt) - STDDEV(a.total_debt), 0) AS lower_bound
FROM User u
JOIN Account a ON u.user_id = a.user_id
WHERE a.total_debt > 0
GROUP BY retirement_groups
ORDER BY retirement_groups DESC;