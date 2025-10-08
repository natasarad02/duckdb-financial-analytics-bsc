SELECT
    a.user_id, a.credit_score, a.total_debt,
    AVG(CAST(REPLACE(t.amount, '$', '') AS DOUBLE)) AS avg_spent,
    c.num_cards_issued AS num_credit_cards
FROM Account a
LEFT JOIN cards c ON a.user_id = c.user_id
LEFT JOIN transactions_arrow t ON a.user_id = t.user_id
GROUP BY a.user_id, a.credit_score, a.total_debt, c.num_cards_issued
HAVING a.credit_score < 650 AND a.total_debt > 10000
ORDER BY a.total_debt DESC, a.credit_score ASC;