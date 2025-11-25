_____________________________________________
## *Author*: AAVA
## *Created on*:   
## *Description*: Bronze layer data mapping for Inventory Management System in Medallion architecture implementation
## *Version*: 2 
## *Updated on*: 
_____________________________________________

# Bronze Layer Data Mapping for Inventory Management System

## Overview
This document defines the comprehensive data mapping between source systems and the Bronze layer in the Medallion architecture implementation using Fabric Lakehouse as delta tables. The Bronze layer preserves raw data structure with minimal transformation, ensuring data lineage and auditability for the Inventory Management System.

## Source System Analysis
Based on the source data analysis, the Inventory Management System contains 10 core tables:
- Products
- Suppliers  
- Warehouses
- Inventory
- Orders
- Order_Details
- Shipments
- Returns
- Stock_Levels
- Customers

## Data Mapping for Bronze Layer

### Products Table Mapping
| Target Layer | Target Table     | Target Field  | Source Layer | Source Table  | Source Field  | Transformation Rule |
| ------------ | ---------------- | ------------- | ------------ | ------------- | ------------- | ------------------- |
| Bronze       | bronze_Products  | Product_ID    | Raw          | raw_Products  | Product_ID    | 1-1 Mapping         |
| Bronze       | bronze_Products  | Product_Name  | Raw          | raw_Products  | Product_Name  | 1-1 Mapping         |
| Bronze       | bronze_Products  | Category      | Raw          | raw_Products  | Category      | 1-1 Mapping         |

### Suppliers Table Mapping
| Target Layer | Target Table     | Target Field     | Source Layer | Source Table  | Source Field     | Transformation Rule |
| ------------ | ---------------- | ---------------- | ------------ | ------------- | ---------------- | ------------------- |
| Bronze       | bronze_Suppliers | Supplier_ID      | Raw          | raw_Suppliers | Supplier_ID      | 1-1 Mapping         |
| Bronze       | bronze_Suppliers | Supplier_Name    | Raw          | raw_Suppliers | Supplier_Name    | 1-1 Mapping         |
| Bronze       | bronze_Suppliers | Contact_Number   | Raw          | raw_Suppliers | Contact_Number   | 1-1 Mapping         |
| Bronze       | bronze_Suppliers | Product_ID       | Raw          | raw_Suppliers | Product_ID       | 1-1 Mapping         |

### Warehouses Table Mapping
| Target Layer | Target Table       | Target Field  | Source Layer | Source Table    | Source Field  | Transformation Rule |
| ------------ | ------------------ | ------------- | ------------ | --------------- | ------------- | ------------------- |
| Bronze       | bronze_Warehouses  | Warehouse_ID  | Raw          | raw_Warehouses  | Warehouse_ID  | 1-1 Mapping         |
| Bronze       | bronze_Warehouses  | Location      | Raw          | raw_Warehouses  | Location      | 1-1 Mapping         |
| Bronze       | bronze_Warehouses  | Capacity      | Raw          | raw_Warehouses  | Capacity      | 1-1 Mapping         |

### Inventory Table Mapping
| Target Layer | Target Table      | Target Field        | Source Layer | Source Table   | Source Field        | Transformation Rule |
| ------------ | ----------------- | ------------------- | ------------ | -------------- | ------------------- | ------------------- |
| Bronze       | bronze_Inventory  | Inventory_ID        | Raw          | raw_Inventory  | Inventory_ID        | 1-1 Mapping         |
| Bronze       | bronze_Inventory  | Product_ID          | Raw          | raw_Inventory  | Product_ID          | 1-1 Mapping         |
| Bronze       | bronze_Inventory  | Quantity_Available  | Raw          | raw_Inventory  | Quantity_Available  | 1-1 Mapping         |
| Bronze       | bronze_Inventory  | Warehouse_ID        | Raw          | raw_Inventory  | Warehouse_ID        | 1-1 Mapping         |

### Orders Table Mapping
| Target Layer | Target Table   | Target Field | Source Layer | Source Table | Source Field | Transformation Rule |
| ------------ | -------------- | ------------ | ------------ | ------------ | ------------ | ------------------- |
| Bronze       | bronze_Orders  | Order_ID     | Raw          | raw_Orders   | Order_ID     | 1-1 Mapping         |
| Bronze       | bronze_Orders  | Customer_ID  | Raw          | raw_Orders   | Customer_ID  | 1-1 Mapping         |
| Bronze       | bronze_Orders  | Order_Date   | Raw          | raw_Orders   | Order_Date   | 1-1 Mapping         |

### Order_Details Table Mapping
| Target Layer | Target Table          | Target Field      | Source Layer | Source Table       | Source Field      | Transformation Rule |
| ------------ | --------------------- | ----------------- | ------------ | ------------------ | ----------------- | ------------------- |
| Bronze       | bronze_Order_Details  | Order_Detail_ID   | Raw          | raw_Order_Details  | Order_Detail_ID   | 1-1 Mapping         |
| Bronze       | bronze_Order_Details  | Order_ID          | Raw          | raw_Order_Details  | Order_ID          | 1-1 Mapping         |
| Bronze       | bronze_Order_Details  | Product_ID        | Raw          | raw_Order_Details  | Product_ID        | 1-1 Mapping         |
| Bronze       | bronze_Order_Details  | Quantity_Ordered  | Raw          | raw_Order_Details  | Quantity_Ordered  | 1-1 Mapping         |

### Shipments Table Mapping
| Target Layer | Target Table      | Target Field   | Source Layer | Source Table   | Source Field   | Transformation Rule |
| ------------ | ----------------- | -------------- | ------------ | -------------- | -------------- | ------------------- |
| Bronze       | bronze_Shipments  | Shipment_ID    | Raw          | raw_Shipments  | Shipment_ID    | 1-1 Mapping         |
| Bronze       | bronze_Shipments  | Order_ID       | Raw          | raw_Shipments  | Order_ID       | 1-1 Mapping         |
| Bronze       | bronze_Shipments  | Shipment_Date  | Raw          | raw_Shipments  | Shipment_Date  | 1-1 Mapping         |

### Returns Table Mapping
| Target Layer | Target Table    | Target Field   | Source Layer | Source Table | Source Field   | Transformation Rule |
| ------------ | --------------- | -------------- | ------------ | ------------ | -------------- | ------------------- |
| Bronze       | bronze_Returns  | Return_ID      | Raw          | raw_Returns  | Return_ID      | 1-1 Mapping         |
| Bronze       | bronze_Returns  | Order_ID       | Raw          | raw_Returns  | Order_ID       | 1-1 Mapping         |
| Bronze       | bronze_Returns  | Return_Reason  | Raw          | raw_Returns  | Return_Reason  | 1-1 Mapping         |

### Stock_Levels Table Mapping
| Target Layer | Target Table         | Target Field       | Source Layer | Source Table      | Source Field       | Transformation Rule |
| ------------ | -------------------- | ------------------ | ------------ | ----------------- | ------------------ | ------------------- |
| Bronze       | bronze_Stock_Levels  | Stock_Level_ID     | Raw          | raw_Stock_Levels  | Stock_Level_ID     | 1-1 Mapping         |
| Bronze       | bronze_Stock_Levels  | Warehouse_ID       | Raw          | raw_Stock_Levels  | Warehouse_ID       | 1-1 Mapping         |
| Bronze       | bronze_Stock_Levels  | Product_ID         | Raw          | raw_Stock_Levels  | Product_ID         | 1-1 Mapping         |
| Bronze       | bronze_Stock_Levels  | Reorder_Threshold  | Raw          | raw_Stock_Levels  | Reorder_Threshold  | 1-1 Mapping         |

### Customers Table Mapping
| Target Layer | Target Table      | Target Field   | Source Layer | Source Table   | Source Field   | Transformation Rule |
| ------------ | ----------------- | -------------- | ------------ | -------------- | -------------- | ------------------- |
| Bronze       | bronze_Customers  | Customer_ID    | Raw          | raw_Customers  | Customer_ID    | 1-1 Mapping         |
| Bronze       | bronze_Customers  | Customer_Name  | Raw          | raw_Customers  | Customer_Name  | 1-1 Mapping         |
| Bronze       | bronze_Customers  | Email          | Raw          | raw_Customers  | Email          | 1-1 Mapping         |

## Data Type Compatibility for Fabric Lakehouse Delta Tables

### Data Type Mapping
| Source Data Type | Bronze Layer Data Type | Delta Table Compatibility | Notes |
| ---------------- | ---------------------- | ------------------------- | ----- |
| INT              | INT                    | ✓ Compatible              | Primary keys and foreign keys |
| VARCHAR(255)     | STRING                 | ✓ Compatible              | Text fields with variable length |
| VARCHAR(100)     | STRING                 | ✓ Compatible              | Category and classification fields |
| VARCHAR(20)      | STRING                 | ✓ Compatible              | Contact numbers and short text |
| DATE             | DATE                   | ✓ Compatible              | Date fields for orders and shipments |

## Metadata Management

### Standard Metadata Fields (Added to all Bronze tables)
| Field Name | Data Type | Description | Source |
| ---------- | --------- | ----------- | ------ |
| _ingestion_timestamp | TIMESTAMP | When the record was ingested into Bronze layer | System Generated |
| _source_file | STRING | Source file or system identifier | System Generated |
| _record_hash | STRING | Hash of the source record for change detection | System Generated |
| _is_active | BOOLEAN | Flag indicating if record is currently active | System Generated |
| _batch_id | STRING | Unique identifier for the ingestion batch | System Generated |

## Initial Data Validation Rules

### Primary Key Validation
- Ensure uniqueness of primary keys across all tables
- Log duplicate key violations without rejecting records
- Maintain audit trail of validation results

### Not Null Validation
- Validate required fields are not null as per source constraints
- Flag records with null values in required fields
- Continue processing with validation flags

### Data Type Validation
- Ensure data types match expected formats
- Handle type conversion errors gracefully
- Log data type mismatches for downstream processing

### Foreign Key Reference Validation
- Log foreign key reference violations
- Do not enforce referential integrity at Bronze layer
- Preserve all source data regardless of referential issues

## Ingestion Process Specifications

### Batch Processing Configuration
- **Frequency**: Daily batch processing
- **Window**: Process data from previous day
- **Format**: Delta Lake format with ACID transactions
- **Partitioning**: Partition by ingestion date (_ingestion_date)

### Incremental Loading Strategy
- Use source system timestamps for incremental detection
- Implement Change Data Capture (CDC) where available
- Full refresh for small dimension tables (Products, Suppliers, Warehouses, Customers)
- Incremental append for large fact tables (Orders, Order_Details, Inventory, Shipments)

### Error Handling
- Continue processing on validation errors
- Log all errors with detailed context
- Quarantine malformed records in separate error tables
- Provide error summary reports for data stewards

## Performance Optimization

### Partitioning Strategy
| Table | Partitioning Column | Rationale |
| ----- | ------------------- | --------- |
| bronze_Orders | Order_Date | Optimize for date-based queries |
| bronze_Order_Details | _ingestion_date | Large table, optimize for batch processing |
| bronze_Inventory | _ingestion_date | Frequent updates, optimize for time-based queries |
| bronze_Shipments | Shipment_Date | Optimize for date-based queries |
| bronze_Returns | _ingestion_date | Optimize for batch processing |
| bronze_Stock_Levels | _ingestion_date | Frequent updates, optimize for time-based queries |

### Indexing Recommendations
- Create indexes on primary key columns for all tables
- Index foreign key columns for join optimization
- Consider composite indexes for frequently queried column combinations

## Data Governance and Security

### Data Lineage
- Track data lineage from source systems to Bronze layer
- Maintain metadata about data transformations and processing
- Enable impact analysis for upstream and downstream dependencies

### Audit Trail
- Log all data ingestion activities
- Track data modifications and updates
- Maintain history of schema changes
- Record data quality validation results

### Access Control
- Implement role-based access control (RBAC)
- Separate read and write permissions
- Audit data access patterns
- Ensure compliance with data privacy regulations

## Assumptions and Implementation Notes

### Key Assumptions
1. **Source Data Quality**: Source systems provide reasonably clean data
2. **Data Availability**: Source systems are available during scheduled ingestion windows
3. **Network Connectivity**: Stable network connection between source and target systems
4. **Schema Stability**: Source schema changes are communicated in advance
5. **Data Volume**: Current data volumes are within expected processing capacity

### Technical Implementation
1. **Fabric Lakehouse**: All Bronze tables implemented as Delta tables
2. **Spark Processing**: Use Apache Spark for data ingestion and processing
3. **SQL Compatibility**: Ensure compatibility with both Spark SQL and T-SQL
4. **Monitoring**: Implement comprehensive monitoring and alerting
5. **Backup and Recovery**: Regular backup of Bronze layer data

### Future Considerations
1. **Real-time Processing**: Potential migration to streaming ingestion
2. **Schema Evolution**: Support for automatic schema evolution
3. **Data Archival**: Implement data archival strategy for historical data
4. **Performance Tuning**: Continuous optimization based on usage patterns
5. **Compliance**: Ensure ongoing compliance with data governance policies

---

**Document Status**: Ready for Implementation  
**Next Phase**: Silver Layer Data Modeling and Transformation Design  
**Dependencies**: Source system connectivity and access permissions