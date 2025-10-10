-- Q6
SELECT
    ad.latitude,
    ad.longitude,
    COUNT(t.id) AS total_transactions
FROM Address ad
LEFT JOIN transactions_parquet t ON ad.user_id = t.user_id
GROUP BY ad.latitude, ad.longitude;