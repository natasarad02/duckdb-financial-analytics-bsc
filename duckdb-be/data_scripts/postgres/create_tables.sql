DROP TABLE IF EXISTS "Account";
DROP TABLE IF EXISTS "Address";
DROP TABLE IF EXISTS "User";

-- User table
CREATE TABLE IF NOT EXISTS "User" (
    user_id SERIAL PRIMARY KEY,
    current_age INT,
    retirement_age INT,
    birth_year INT,
    birth_month INT,
    gender VARCHAR(10)
);


-- Address table
CREATE TABLE IF NOT EXISTS "Address" (
    address_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES "User"(user_id),
    address VARCHAR(255),
    latitude NUMERIC,
    longitude NUMERIC,
    per_capita_income NUMERIC
);


-- Account table
CREATE TABLE IF NOT EXISTS "Account" (
    account_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES "User"(user_id),
    yearly_income NUMERIC,
    total_debt NUMERIC,
    credit_score INT,
    num_credit_cards INT
);