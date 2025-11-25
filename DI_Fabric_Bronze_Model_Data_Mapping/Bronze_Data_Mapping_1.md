_____________________________________________
## *Author*: AAVA
## *Created on*: 
## *Description*: Bronze layer data mapping for Inventory Management system in Medallion architecture
## *Version*: 1 
## *Updated on*: 
_____________________________________________

# Bronze Layer Data Mapping for Inventory Management System

## Overview
This document defines the data mapping between source systems and the Bronze layer in the Medallion architecture implementation for the Inventory Management system. The Bronze layer preserves raw data structure with minimal transformation, ensuring data lineage and auditability.

## Data Mapping Tables

### Products Table Mapping
| Target Layer | Target Table      | Target Field    | Source Layer | Source Table | Source Field    | Transformation Rule |
|--------------|-------------------|-----------------|--------------|--------------|-----------------|--------------------|
| Bronze       | bronze_Products   | Product_ID      | Raw          | Products     | Product_ID      | 1-1 Mapping        |
| Bronze       | bronze_Products   | Product_Name    | Raw          | Products     | Product_Name    | 1-1 Mapping        |
| Bronze       | bronze_Products   | Category        | Raw          | Products     | Category        | 1-1 Mapping        |

### Suppliers Table Mapping
| Target Layer | Target Table      | Target Field      | Source Layer | Source Table | Source Field      | Transformation Rule |
|--------------|-------------------|-------------------|--------------|--------------|-------------------|--------------------|
| Bronze       | bronze_Suppliers  | Supplier_ID       | Raw          | Suppliers    | Supplier_ID       | 1-1 Mapping        |
| Bronze       | bronze_Suppliers  | Supplier_Name     | Raw          | Suppliers    | Supplier_Name     | 1-1 Mapping        |
| Bronze       | bronze_Suppliers  | Contact_Number    | Raw          | Suppliers    | Contact_Number    | 1-1 Mapping        |
| Bronze       | bronze_Suppliers  | Product_ID        | Raw          | Suppliers    | Product_ID        | 1-1 Mapping        |

### Warehouses Table Mapping
| Target Layer | Target Table        | Target Field    | Source Layer | Source Table | Source Field    | Transformation Rule |
|--------------|---------------------|-----------------|--------------|--------------|-----------------|--------------------|
| Bronze       | bronze_Warehouses   | Warehouse_ID    | Raw          | Warehouses   | Warehouse_ID    | 1-1 Mapping        |
| Bronze       | bronze_Warehouses   | Location        | Raw          | Warehouses   | Location        | 1-1 Mapping        |
| Bronze       | bronze_Warehouses   | Capacity        | Raw          | Warehouses   | Capacity        | 1-1 Mapping        |

### Inventory Table Mapping
| Target Layer | Target Table      | Target Field         | Source Layer | Source Table | Source Field         | Transformation Rule |
|--------------|-------------------|----------------------|--------------|--------------|----------------------|--------------------|
| Bronze       | bronze_Inventory  | Inventory_ID         | Raw          | Inventory    | Inventory_ID         | 1-1 Mapping        |
| Bronze       | bronze_Inventory  | Product_ID           | Raw          | Inventory    | Product_ID           | 1-1 Mapping        |
| Bronze       | bronze_Inventory  | Quantity_Available   | Raw          | Inventory    | Quantity_Available   | 1-1 Mapping        |
| Bronze       | bronze_Inventory  | Warehouse_ID         | Raw          | Inventory    | Warehouse_ID         | 1-1 Mapping        |

### Orders Table Mapping
| Target Layer | Target Table    | Target Field  | Source Layer | Source Table | Source Field  | Transformation Rule |
|--------------|-----------------|---------------|--------------|--------------|---------------|--------------------|
| Bronze       | bronze_Orders   | Order_ID      | Raw          | Orders       | Order_ID      | 1-1 Mapping        |
| Bronze       | bronze_Orders   | Customer_ID   | Raw          | Orders       | Customer_ID   | 1-1 Mapping        |
| Bronze       | bronze_Orders   | Order_Date    | Raw          | Orders       | Order_Date    | 1-1 Mapping        |

### Order_Details Table Mapping
| Target Layer | Target Table           | Target Field        | Source Layer | Source Table  | Source Field        | Transformation Rule |
|--------------|------------------------|---------------------|--------------|---------------|---------------------|--------------------|
| Bronze       | bronze_Order_Details   | Order_Detail_ID     | Raw          | Order_Details | Order_Detail_ID     | 1-1 Mapping        |
| Bronze       | bronze_Order_Details   | Order_ID            | Raw          | Order_Details | Order_ID            | 1-1 Mapping        |
| Bronze       | bronze_Order_Details   | Product_ID          | Raw          | Order_Details | Product_ID          | 1-1 Mapping        |
| Bronze       | bronze_Order_Details   | Quantity_Ordered    | Raw          | Order_Details | Quantity_Ordered    | 1-1 Mapping        |

### Shipments Table Mapping
| Target Layer | Target Table       | Target Field    | Source Layer | Source Table | Source Field    | Transformation Rule |
|--------------|--------------------|-----------------|--------------|--------------|-----------------|--------------------||
| Bronze       | bronze_Shipments   | Shipment_ID     | Raw          | Shipments    | Shipment_ID     | 1-1 Mapping        |
| Bronze       | bronze_Shipments   | Order_ID        | Raw          | Shipments    | Order_ID        | 1-1 Mapping        |
| Bronze       | bronze_Shipments   | Shipment_Date   | Raw          | Shipments    | Shipment_Date   | 1-1 Mapping        |

### Returns Table Mapping
| Target Layer | Target Table     | Target Field     | Source Layer | Source Table | Source Field     | Transformation Rule |
|--------------|------------------|------------------|--------------|--------------|------------------|--------------------|
| Bronze       | bronze_Returns   | Return_ID        | Raw          | Returns      | Return_ID        | 1-1 Mapping        |
| Bronze       | bronze_Returns   | Order_ID         | Raw          | Returns      | Order_ID         | 1-1 Mapping        |
| Bronze       | bronze_Returns   | Return_Reason    | Raw          | Returns      | Return_Reason    | 1-1 Mapping        |

### Stock_Levels Table Mapping
| Target Layer | Target Table         | Target Field        | Source Layer | Source Table | Source Field        | Transformation Rule |
|--------------|----------------------|---------------------|--------------|--------------|---------------------|--------------------|
| Bronze       | bronze_Stock_Levels  | Stock_Level_ID      | Raw          | Stock_Levels | Stock_Level_ID      | 1-1 Mapping        |
| Bronze       | bronze_Stock_Levels  | Warehouse_ID        | Raw          | Stock_Levels | Warehouse_ID        | 1-1 Mapping        |
| Bronze       | bronze_Stock_Levels  | Product_ID          | Raw          | Stock_Levels | Product_ID          | 1-1 Mapping        |
| Bronze       | bronze_Stock_Levels  | Reorder_Threshold   | Raw          | Stock_Levels | Reorder_Threshold   | 1-1 Mapping        |

### Customers Table Mapping
| Target Layer | Target Table      | Target Field     | Source Layer | Source Table | Source Field     | Transformation Rule |
|--------------|-------------------|------------------|--------------|--------------|------------------|--------------------|
| Bronze       | bronze_Customers  | Customer_ID      | Raw          | Customers    | Customer_ID      | 1-1 Mapping        |
| Bronze       | bronze_Customers  | Customer_Name    | Raw          | Customers    | Customer_Name    | 1-1 Mapping        |
| Bronze       | bronze_Customers  | Email            | Raw          | Customers    | Email            | 1-1 Mapping        |

## Data Type Compatibility for Fabric Lakehouse Delta Tables

### Data Type Mapping Guidelines
- **INT**: Maps to `INT` in Delta tables
- **VARCHAR(n)**: Maps to `STRING` in Delta tables
- **DATE**: Maps to `DATE` in Delta tables

## Ingestion Metadata Requirements

### Standard Metadata Columns
Each Bronze layer table should include the following metadata columns:
- `_ingestion_timestamp`: TIMESTAMP - When the record was ingested
- `_source_file_name`: STRING - Name of the source file
- `_source_system`: STRING - Source system identifier
- `_record_hash`: STRING - Hash of the record for change detection

## Data Ingestion Details

### Ingestion Approach
- **Method**: Batch ingestion using Azure Data Factory or Fabric Data Pipelines
- **Format**: Delta Lake format for ACID transactions and time travel
- **Partitioning**: Consider partitioning by date for time-based queries
- **Schema Evolution**: Enable schema evolution for handling source schema changes

### Data Quality Checks
- Null value validation for primary key fields
- Data type validation
- Record count validation
- Duplicate detection based on primary keys

## Assumptions and Notes

1. **Source Data Format**: Assuming source data is in structured format (CSV, JSON, or database tables)
2. **Data Freshness**: Bronze layer will be updated based on source system availability
3. **Historical Data**: Bronze layer will maintain historical versions using Delta Lake time travel
4. **Error Handling**: Failed records will be logged and stored in separate error tables
5. **Compression**: Delta tables will use Snappy compression for optimal storage

## Next Steps

1. Implement Bronze layer tables in Fabric Lakehouse
2. Create data ingestion pipelines
3. Set up monitoring and alerting for data quality
4. Establish data retention policies
5. Prepare for Silver layer transformations