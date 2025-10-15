WITH active_cards_count AS (
    SELECT 
        c.card_id,
        1 AS is_active
    FROM cards c
    JOIN transactions_parquet t USING(user_id)
    GROUP BY c.card_id
)
SELECT 
    c.card_brand,
    SUM(c.num_cards_issued) AS total_cards_issued,
    COUNT(ac.card_id) AS total_cards_active
FROM cards c
LEFT JOIN active_cards_count ac USING(card_id)
GROUP BY c.card_brand
ORDER BY c.card_brand;