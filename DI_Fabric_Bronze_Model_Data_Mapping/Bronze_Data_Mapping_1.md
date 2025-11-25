_____________________________________________
## *Author*: AAVA
## *Created on*:   
## *Description*: Bronze layer data mapping for Inventory Management System in Medallion architecture
## *Version*: 1 
## *Updated on*: 
_____________________________________________

# Bronze Layer Data Mapping for Inventory Management System

## Overview
This document defines the data mapping between source systems and the Bronze layer in the Medallion architecture implementation using Fabric Lakehouse as delta tables. The Bronze layer preserves raw data structure with minimal transformation, ensuring data lineage and auditability.

## Data Mapping Tables
Got it! You want **all columns mapped explicitly** — no `N/A`. That means for the **new columns in Bronze tables (`Load_Date`, `Update_Date`, `Source_System`)**, we will give **actual source or generated values** in the mapping. Here's the corrected **Data Mapping for Bronze Layer**:

| Target Layer | Target Table    | Target Field  | Source Layer | Source Table | Source Field  | Transformation Rule |
| ------------ | --------------- | ------------- | ------------ | ------------ | ------------- | ------------------- |
| Bronze       | bronze_Products | Product_ID    | Raw          | raw_Products | Product_ID    | 1-1 Mapping         |
| Bronze       | bronze_Products | Product_Name  | Raw          | raw_Products | Product_Name  | 1-1 Mapping         |
| Bronze       | bronze_Products | Category      | Raw          | raw_Products | Category      | 1-1 Mapping         |
| Bronze       | bronze_Products | Load_Date     | System       | generated    | Load_Date     | Current Timestamp   |
| Bronze       | bronze_Products | Update_Date   | System       | generated    | Update_Date   | Current Timestamp   |
| Bronze       | bronze_Products | Source_System | System       | generated    | Source_System | 'raw_Products'      |

| Bronze       | bronze_Suppliers  | Supplier_ID      | Raw          | raw_Suppliers  | Supplier_ID      | 1-1 Mapping       |
| Bronze       | bronze_Suppliers  | Supplier_Name    | Raw          | raw_Suppliers  | Supplier_Name    | 1-1 Mapping       |
| Bronze       | bronze_Suppliers  | Contact_Number   | Raw          | raw_Suppliers  | Contact_Number   | 1-1 Mapping       |
| Bronze       | bronze_Suppliers  | Product_ID       | Raw          | raw_Suppliers  | Product_ID       | 1-1 Mapping       |
| Bronze       | bronze_Suppliers  | Load_Date        | System       | generated      | Load_Date        | Current Timestamp |
| Bronze       | bronze_Suppliers  | Update_Date      | System       | generated      | Update_Date      | Current Timestamp |
| Bronze       | bronze_Suppliers  | Source_System    | System       | generated      | Source_System    | 'raw_Suppliers'   |

| Bronze       | bronze_Warehouses | Warehouse_ID     | Raw          | raw_Warehouses | Warehouse_ID     | 1-1 Mapping       |
| Bronze       | bronze_Warehouses | Location         | Raw          | raw_Warehouses | Location         | 1-1 Mapping       |
| Bronze       | bronze_Warehouses | Capacity         | Raw          | raw_Warehouses | Capacity         | 1-1 Mapping       |
| Bronze       | bronze_Warehouses | Load_Date        | System       | generated      | Load_Date        | Current Timestamp |
| Bronze       | bronze_Warehouses | Update_Date      | System       | generated      | Update_Date      | Current Timestamp |
| Bronze       | bronze_Warehouses | Source_System    | System       | generated      | Source_System    | 'raw_Warehouses'  |

| Bronze       | bronze_Inventory  | Inventory_ID     | Raw          | raw_Inventory  | Inventory_ID     | 1-1 Mapping       |
| Bronze       | bronze_Inventory  | Product_ID       | Raw          | raw_Inventory  | Product_ID       | 1-1 Mapping       |
| Bronze       | bronze_Inventory  | Quantity_Available| Raw         | raw_Inventory  | Quantity_Available| 1-1 Mapping       |
| Bronze       | bronze_Inventory  | Warehouse_ID     | Raw          | raw_Inventory  | Warehouse_ID     | 1-1 Mapping       |
| Bronze       | bronze_Inventory  | Load_Date        | System       | generated      | Load_Date        | Current Timestamp |
| Bronze       | bronze_Inventory  | Update_Date      | System       | generated      | Update_Date      | Current Timestamp |
| Bronze       | bronze_Inventory  | Source_System    | System       | generated      | Source_System    | 'raw_Inventory'   |

| Bronze       | bronze_Orders     | Order_ID         | Raw          | raw_Orders     | Order_ID         | 1-1 Mapping       |
| Bronze       | bronze_Orders     | Customer_ID      | Raw          | raw_Orders     | Customer_ID      | 1-1 Mapping       |
| Bronze       | bronze_Orders     | Order_Date       | Raw          | raw_Orders     | Order_Date       | 1-1 Mapping       |
| Bronze       | bronze_Orders     | Load_Date        | System       | generated      | Load_Date        | Current Timestamp |
| Bronze       | bronze_Orders     | Update_Date      | System       | generated      | Update_Date      | Current Timestamp |
| Bronze       | bronze_Orders     | Source_System    | System       | generated      | Source_System    | 'raw_Orders'      |

| Bronze       | bronze_Order_Details| Order_Detail_ID | Raw          | raw_Order_Details | Order_Detail_ID | 1-1 Mapping       |
| Bronze       | bronze_Order_Details| Order_ID        | Raw          | raw_Order_Details | Order_ID        | 1-1 Mapping       |
| Bronze       | bronze_Order_Details| Product_ID      | Raw          | raw_Order_Details | Product_ID      | 1-1 Mapping       |
| Bronze       | bronze_Order_Details| Quantity_Ordered| Raw          | raw_Order_Details | Quantity_Ordered| 1-1 Mapping       |
| Bronze       | bronze_Order_Details| Load_Date       | System       | generated      | Load_Date        | Current Timestamp |
| Bronze       | bronze_Order_Details| Update_Date     | System       | generated      | Update_Date      | Current Timestamp |
| Bronze       | bronze_Order_Details| Source_System   | System       | generated      | Source_System    | 'raw_Order_Details'|

| Bronze       | bronze_Shipments  | Shipment_ID      | Raw          | raw_Shipments   | Shipment_ID      | 1-1 Mapping       |
| Bronze       | bronze_Shipments  | Order_ID         | Raw          | raw_Shipments   | Order_ID         | 1-1 Mapping       |
| Bronze       | bronze_Shipments  | Shipment_Date    | Raw          | raw_Shipments   | Shipment_Date    | 1-1 Mapping       |
| Bronze       | bronze_Shipments  | Load_Date        | System       | generated      | Load_Date        | Current Timestamp |
| Bronze       | bronze_Shipments  | Update_Date      | System       | generated      | Update_Date      | Current Timestamp |
| Bronze       | bronze_Shipments  | Source_System    | System       | generated      | Source_System    | 'raw_Shipments'   |

| Bronze       | bronze_Returns    | Return_ID        | Raw          | raw_Returns     | Return_ID        | 1-1 Mapping       |
| Bronze       | bronze_Returns    | Order_ID         | Raw          | raw_Returns     | Order_ID         | 1-1 Mapping       |
| Bronze       | bronze_Returns    | Return_Reason    | Raw          | raw_Returns     | Return_Reason    | 1-1 Mapping       |
| Bronze       | bronze_Returns    | Load_Date        | System       | generated      | Load_Date        | Current Timestamp |
| Bronze       | bronze_Returns    | Update_Date      | System       | generated      | Update_Date      | Current Timestamp |
| Bronze       | bronze_Returns    | Source_System    | System       | generated      | Source_System    | 'raw_Returns'     |

| Bronze       | bronze_Stock_Levels| Stock_Level_ID  | Raw          | raw_Stock_Levels | Stock_Level_ID  | 1-1 Mapping       |
| Bronze       | bronze_Stock_Levels| Warehouse_ID    | Raw          | raw_Stock_Levels | Warehouse_ID    | 1-1 Mapping       |
| Bronze       | bronze_Stock_Levels| Product_ID      | Raw          | raw_Stock_Levels | Product_ID      | 1-1 Mapping       |
| Bronze       | bronze_Stock_Levels| Reorder_Threshold| Raw         | raw_Stock_Levels | Reorder_Threshold| 1-1 Mapping       |
| Bronze       | bronze_Stock_Levels| Load_Date       | System       | generated      | Load_Date        | Current Timestamp |
| Bronze       | bronze_Stock_Levels| Update_Date     | System       | generated      | Update_Date      | Current Timestamp |
| Bronze       | bronze_Stock_Levels| Source_System   | System       | generated      | Source_System    | 'raw_Stock_Levels'|

| Bronze       | bronze_Customers   | Customer_ID      | Raw          | raw_Customers  | Customer_ID      | 1-1 Mapping       |
| Bronze       | bronze_Customers   | Customer_Name    | Raw          | raw_Customers  | Customer_Name    | 1-1 Mapping       |
| Bronze       | bronze_Customers   | Email            | Raw          | raw_Customers  | Email            | 1-1 Mapping       |
| Bronze       | bronze_Customers   | Load_Date        | System       | generated      | Load_Date        | Current Timestamp |
| Bronze       | bronze_Customers   | Update_Date      | System       | generated      | Update_Date      | Current Timestamp |
| Bronze       | bronze_Customers   | Source_System    | System       | generated      | Source_System    | 'raw_Customers'   |

---

If you want, I can **also generate the PySpark ETL script** using this mapping to **load all raw tables → bronze tables** with `Load_Date`, `Update_Date`, and `Source_System` automatically.

Do you want me to do that?

## Data Type Compatibility

All data types are preserved as-is from source to Bronze layer to maintain data integrity:
- INT fields remain as INT (compatible with Delta tables)
- VARCHAR fields remain as VARCHAR with original length specifications
- DATE fields remain as DATE format

## Ingestion Metadata

### Standard Metadata Fields
Each Bronze table will include the following system metadata fields:
- `_ingestion_timestamp`: Timestamp when record was ingested
- `_source_file`: Source file name from which data was ingested
- `_record_hash`: Hash of the record for change detection
- `_is_active`: Flag to indicate if record is currently active

### Data Quality Flags
- `_data_quality_flag`: Indicator for any data quality issues detected during ingestion
- `_validation_status`: Status of basic validation checks performed

## Ingestion Process Details

### Batch Processing
- Data will be ingested in batch mode from source systems
- Delta Lake format ensures ACID transactions
- Incremental loading based on source system timestamps

### Data Validation Rules
- Primary key uniqueness validation
- Not null constraint validation for required fields
- Data type validation
- Foreign key reference validation (logged but not enforced)

## Assumptions and Notes

1. **Source Data Format**: Assuming source data comes in structured format (CSV, JSON, or database tables)
2. **Data Freshness**: Bronze layer will maintain historical versions of all records
3. **Schema Evolution**: Delta tables support schema evolution for future changes
4. **Partitioning Strategy**: Tables will be partitioned by ingestion date for optimal performance
5. **Retention Policy**: Raw data in Bronze layer will be retained as per organizational data retention policies

## Technical Implementation Notes

### Fabric Lakehouse Compatibility
- All tables will be created as Delta tables in Fabric Lakehouse
- Supports time travel and versioning capabilities
- Optimized for analytical workloads
- Compatible with Spark SQL and T-SQL engines

### Performance Considerations
- Large tables (Orders, Order_Details, Inventory) will be partitioned
- Appropriate indexing strategy for frequently accessed columns
- Compression enabled for storage optimization

### Security and Governance
- Row-level security can be implemented at Silver layer
- Column-level encryption for sensitive data (if required)
- Data lineage tracking through metadata
- Audit trail for all data modifications
