-- Logische Datenqualitätsprüfungen – Tabellen vorher selbst in deiner SQL-Umgebung anlegen.
SELECT o.order_id FROM erp_orders o LEFT JOIN crm_customers c ON o.customer_id=c.customer_id WHERE c.customer_id IS NULL;
SELECT product_id FROM price_list WHERE unit_price IS NULL OR unit_price <= 0;
SELECT batch_id FROM production_quality WHERE units_defective IS NULL OR units_defective < 0 OR units_defective > units_produced;
