-- Q2
WITH spending AS (
    SELECT
        user_id,  
        AVG(CAST(REPLACE(CAST(amount AS VARCHAR), '$', '') AS DOUBLE)) AS avg_spent
    FROM transactions_arrow
    GROUP BY user_id
),
credit_info AS (
    SELECT 
        c.user_id, 
        c.num_cards_issued,  
        AVG(CAST(REPLACE(CAST(c.credit_limit AS VARCHAR), '$', '') AS DOUBLE)) AS avg_credit_limit
    FROM cards c
    GROUP BY c.user_id, c.num_cards_issued
)
SELECT
    ci.num_cards_issued, 
    AVG(ci.avg_credit_limit) AS avg_credit_limit,
    AVG(s.avg_spent) AS avg_spent
FROM credit_info ci
LEFT JOIN spending s ON ci.user_id = s.user_id
GROUP BY ci.num_cards_issued
ORDER BY ci.num_cards_issued;