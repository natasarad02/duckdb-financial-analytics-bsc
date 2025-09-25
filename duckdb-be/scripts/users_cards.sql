SELECT
    u.user_id,
    c.card_id,
    c.card_brand,
    c.card_type,
    c.credit_limit,
    c.features['num_cards_issued'] AS num_cards_issued,
    c.features['year_pin_last_changed'] AS pin_changed,
    c.features['card_on_dark_web'] AS dark_web_flag
FROM user AS u
LEFT JOIN cards AS c
    ON u.user_id = c.user_id
WHERE c.card_brand IS NOT NULL;