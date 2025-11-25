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
CREATE TABLE IF NOT EXISTS bz_products (
    Product_ID STRING,
    Product_Name STRING,
    Category STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 2. SUPPLIERS TABLE
CREATE TABLE IF NOT EXISTS bz_suppliers (
    Supplier_ID STRING,
    Supplier_Name STRING,
    Contact_Number STRING,
    Product_ID STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 3. WAREHOUSES TABLE
CREATE TABLE IF NOT EXISTS bz_warehouses (
    Warehouse_ID STRING,
    Location STRING,
    Capacity NUMBER,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 4. INVENTORY TABLE
CREATE TABLE IF NOT EXISTS bz_inventory (
    Inventory_ID STRING,
    Product_ID STRING,
    Quantity_Available NUMBER,
    Warehouse_ID STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 5. ORDERS TABLE
CREATE TABLE IF NOT EXISTS bz_orders (
    Order_ID STRING,
    Customer_ID STRING,
    Order_Date DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 6. ORDER_DETAILS TABLE
CREATE TABLE IF NOT EXISTS bz_order_details (
    Order_Detail_ID STRING,
    Order_ID STRING,
    Product_ID STRING,
    Quantity_Ordered NUMBER,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 7. SHIPMENTS TABLE
CREATE TABLE IF NOT EXISTS bz_shipments (
    Shipment_ID STRING,
    Order_ID STRING,
    Shipment_Date DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 8. RETURNS TABLE
CREATE TABLE IF NOT EXISTS bz_returns (
    Return_ID STRING,
    Order_ID STRING,
    Return_Reason STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 9. STOCK_LEVELS TABLE
CREATE TABLE IF NOT EXISTS bz_stock_levels (
    Stock_Level_ID STRING,
    Warehouse_ID STRING,
    Product_ID STRING,
    Reorder_Threshold NUMBER,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 10. CUSTOMERS TABLE
CREATE TABLE IF NOT EXISTS bz_customers (
    Customer_ID STRING,
    Customer_Name STRING,
    Email STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 11. AUDIT TABLE
CREATE TABLE IF NOT EXISTS bz_audit_table (
    record_id NUMBER AUTOINCREMENT,
    source_table STRING,
    load_timestamp TIMESTAMP_NTZ,
    processed_by STRING,
    processing_time NUMBER,
    status STRING
)
USING DELTA;

-- =====================================================
-- END OF BRONZE LAYER PHYSICAL DATA MODEL
-- =====================================================