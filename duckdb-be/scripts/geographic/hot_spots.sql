SELECT
    ad.latitude,
    ad.longitude,
    COUNT(t.id) AS total_transactions
FROM Address ad
JOIN User u ON ad.user_id = u.user_id
LEFT JOIN transactions_parquet t ON u.user_id = t.user_id
GROUP BY ad.latitude, ad.longitude
HAVING count(t.id) > 0;