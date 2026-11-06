-- Analytisches Datenmodell (für Diskussion/Anpassung, kein fertiger Migrationsskript)
CREATE TABLE dim_customer (customer_key INTEGER PRIMARY KEY, customer_id VARCHAR(30) UNIQUE, company_name VARCHAR(200), country CHAR(2));
CREATE TABLE dim_product (product_key INTEGER PRIMARY KEY, product_id VARCHAR(30) UNIQUE, product_name VARCHAR(200));
CREATE TABLE dim_date (date_key INTEGER PRIMARY KEY, calendar_date DATE UNIQUE, year_num INTEGER, month_num INTEGER);
CREATE TABLE fact_order (order_id VARCHAR(30) PRIMARY KEY, customer_key INTEGER REFERENCES dim_customer(customer_key), product_key INTEGER REFERENCES dim_product(product_key), date_key INTEGER REFERENCES dim_date(date_key), quantity INTEGER);
-- Aufgaben: Welche Grain? Wie historisierte Preise und Slowly Changing Dimensions abbilden?
