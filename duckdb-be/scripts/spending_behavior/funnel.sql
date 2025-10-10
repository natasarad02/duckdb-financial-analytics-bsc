WITH funnel AS (
    SELECT COUNT(*) AS all_users
    FROM "User"
), step1 AS (
    SELECT COUNT(*) AS users_with_2plus_cards
    FROM (
        SELECT u.user_id
        FROM "User" u
        JOIN cards c ON u.user_id = c.user_id
        GROUP BY u.user_id
        HAVING COUNT(c.card_id) >= 2
    ) t
), step2 AS (
    SELECT COUNT(*) AS high_spenders
    FROM (
        SELECT u.user_id
        FROM "User" u
        JOIN transactions_parquet t ON u.user_id = t.user_id
        GROUP BY u.user_id
        HAVING SUM(CAST(REPLACE(t.amount,'$','') AS DOUBLE)) > 5000
    ) t
), step3 AS (
  	SELECT COUNT(*) AS low_credit_score
    FROM "Account"
    WHERE credit_score < 700
  
), step4 AS (
  	SELECT COUNT(*) AS compromised_cards
    FROM cards
    WHERE card_on_dark_web = true
	
  
)
SELECT *
FROM funnel, step1, step2, step3, step4;



SELECT 'All Users' AS step, COUNT(*) AS users 
FROM "User"

UNION ALL
SELECT '2+ Cards', COUNT(DISTINCT u.user_id)
FROM "User" u
JOIN cards c ON u.user_id = c.user_id
GROUP BY u.user_id
HAVING COUNT(c.card_id) >= 2

UNION ALL
SELECT 'High Spenders', COUNT(DISTINCT u.user_id)
FROM "User" u
JOIN transactions_parquet t ON u.user_id = t.user_id
GROUP BY u.user_id
HAVING SUM(CAST(REPLACE(t.amount,'$','') AS DOUBLE)) > 5000

UNION ALL
SELECT 'Low Credit Score', COUNT(*) 
FROM "Account"
WHERE credit_score < 700

UNION ALL
SELECT 'Compromised Cards', COUNT(*) 
FROM cards 
WHERE card_on_dark_web = TRUE;