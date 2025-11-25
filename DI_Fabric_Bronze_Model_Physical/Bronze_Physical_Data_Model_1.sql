_____________________________________________
## *Author*: AAVA
## *Created on*: 
## *Description*: Bronze Layer Physical Data Model for Inventory Management System
## *Version*: 1 
## *Updated on*: 
_____________________________________________

-- =====================================================
-- BRONZE LAYER PHYSICAL DATA MODEL
-- INVENTORY MANAGEMENT SYSTEM
-- =====================================================

-- 1. PRODUCTS TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_products (
    product_id NUMBER,
    product_name STRING,
    category STRING,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 2. SUPPLIERS TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_suppliers (
    supplier_id NUMBER,
    supplier_name STRING,
    contact_number STRING,
    product_id NUMBER,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 3. WAREHOUSES TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_warehouses (
    warehouse_id NUMBER,
    location STRING,
    capacity NUMBER,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 4. INVENTORY TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_inventory (
    inventory_id NUMBER,
    product_id NUMBER,
    quantity_available NUMBER,
    warehouse_id NUMBER,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 5. ORDERS TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_orders (
    order_id NUMBER,
    customer_id NUMBER,
    order_date DATE,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 6. ORDER_DETAILS TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_order_details (
    order_detail_id NUMBER,
    order_id NUMBER,
    product_id NUMBER,
    quantity_ordered NUMBER,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 7. SHIPMENTS TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_shipments (
    shipment_id NUMBER,
    order_id NUMBER,
    shipment_date DATE,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 8. RETURNS TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_returns (
    return_id NUMBER,
    order_id NUMBER,
    return_reason STRING,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 9. STOCK_LEVELS TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_stock_levels (
    stock_level_id NUMBER,
    warehouse_id NUMBER,
    product_id NUMBER,
    reorder_threshold NUMBER,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 10. CUSTOMERS TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_customers (
    customer_id NUMBER,
    customer_name STRING,
    email STRING,
    -- Metadata columns
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
);

-- 11. AUDIT TABLE
CREATE TABLE IF NOT EXISTS Bronze.bz_audit (
    record_id NUMBER AUTOINCREMENT,
    source_table STRING,
    load_timestamp TIMESTAMP_NTZ,
    processed_by STRING,
    processing_time NUMBER,
    status STRING
);

-- =====================================================
-- END OF BRONZE LAYER PHYSICAL DATA MODEL
-- =====================================================

/*
NOTES:
1. All tables use Snowflake's default micro-partitioned storage format
2. No primary keys, foreign keys, or constraints are defined as per Bronze layer requirements
3. All data types are compatible with Snowflake SQL (STRING, NUMBER, DATE, TIMESTAMP_NTZ)
4. Metadata columns (load_timestamp, update_timestamp, source_system) are included for data lineage
5. Table names follow the Bronze layer naming convention with 'bz_' prefix
6. Audit table includes AUTOINCREMENT for record_id to track processing history
7. All tables use 'CREATE TABLE IF NOT EXISTS' syntax for safe deployment
*/