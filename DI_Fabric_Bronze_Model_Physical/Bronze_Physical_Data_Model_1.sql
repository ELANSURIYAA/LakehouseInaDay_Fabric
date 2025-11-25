_____________________________________________
## *Author*: AAVA
## *Created on*: 
## *Description*: Bronze Layer Physical Data Model for Inventory Management System
## *Version*: 1 
## *Updated on*: 
_____________________________________________

-- =====================================================
-- BRONZE LAYER DDL SCRIPT
-- Inventory Management System - Bronze Layer Tables
-- =====================================================

-- 1. Bronze Products Table
CREATE TABLE IF NOT EXISTS bronze_products (
    Product_ID STRING,
    Product_Name STRING,
    Category STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 2. Bronze Suppliers Table
CREATE TABLE IF NOT EXISTS bronze_suppliers (
    Supplier_ID STRING,
    Supplier_Name STRING,
    Contact_Number STRING,
    Product_ID STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 3. Bronze Warehouses Table
CREATE TABLE IF NOT EXISTS bronze_warehouses (
    Warehouse_ID STRING,
    Location STRING,
    Capacity NUMBER,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 4. Bronze Inventory Table
CREATE TABLE IF NOT EXISTS bronze_inventory (
    Inventory_ID STRING,
    Product_ID STRING,
    Quantity_Available NUMBER,
    Warehouse_ID STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 5. Bronze Orders Table
CREATE TABLE IF NOT EXISTS bronze_orders (
    Order_ID STRING,
    Customer_ID STRING,
    Order_Date DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 6. Bronze Order Details Table
CREATE TABLE IF NOT EXISTS bronze_order_details (
    Order_Detail_ID STRING,
    Order_ID STRING,
    Product_ID STRING,
    Quantity_Ordered NUMBER,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 7. Bronze Shipments Table
CREATE TABLE IF NOT EXISTS bronze_shipments (
    Shipment_ID STRING,
    Order_ID STRING,
    Shipment_Date DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 8. Bronze Returns Table
CREATE TABLE IF NOT EXISTS bronze_returns (
    Return_ID STRING,
    Order_ID STRING,
    Return_Reason STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 9. Bronze Stock Levels Table
CREATE TABLE IF NOT EXISTS bronze_stock_levels (
    Stock_Level_ID STRING,
    Warehouse_ID STRING,
    Product_ID STRING,
    Reorder_Threshold NUMBER,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 10. Bronze Customers Table
CREATE TABLE IF NOT EXISTS bronze_customers (
    Customer_ID STRING,
    Customer_Name STRING,
    Email STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 11. Bronze Audit Table
CREATE TABLE IF NOT EXISTS bronze_audit (
    record_id NUMBER AUTOINCREMENT,
    source_table STRING,
    load_timestamp TIMESTAMP_NTZ,
    processed_by STRING,
    processing_time NUMBER,
    status STRING
)
USING DELTA;

-- =====================================================
-- END OF BRONZE LAYER DDL SCRIPT
-- =====================================================