USE currencies;

CREATE TABLE IF NOT EXISTS currency (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    abbreviation VARCHAR(3) NOT NULL,
    value_in_bgn DECIMAL(10, 2) NOT NULL
);

INSERT INTO currency (name, abbreviation, value_in_bgn) VALUES
    ('Euro', 'EUR', 1.96),
    ('US Dollar', 'USD', 1.83),
    ('British Pound', 'GBP', 2.28);

