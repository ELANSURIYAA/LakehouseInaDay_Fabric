_____________________________________________
## *Author*: AAVA
## *Created on*:   
## *Description*: Bronze layer data mapping for Inventory Management system in Medallion architecture
## *Version*: 1 
## *Updated on*: 
_____________________________________________

# Bronze Layer Data Mapping for Inventory Management System

## Overview
This document defines the data mapping between the source system and the Bronze layer in the Medallion architecture implementation for the Inventory Management system. The Bronze layer maintains raw data with minimal transformation, preserving the original structure and metadata for downstream processing.

## Data Mapping Tables

### Products Table Mapping
| Target Layer | Target Table      | Target Field     | Source Layer | Source Table | Source Field     | Transformation Rule |
| ------------ | ----------------- | ---------------- | ------------ | ------------ | ---------------- | ------------------- |
| Bronze       | bronze_Products   | Product_ID       | Raw          | Products     | Product_ID       | 1-1 Mapping         |
| Bronze       | bronze_Products   | Product_Name     | Raw          | Products     | Product_Name     | 1-1 Mapping         |
| Bronze       | bronze_Products   | Category         | Raw          | Products     | Category         | 1-1 Mapping         |

### Suppliers Table Mapping
| Target Layer | Target Table      | Target Field     | Source Layer | Source Table | Source Field     | Transformation Rule |
| ------------ | ----------------- | ---------------- | ------------ | ------------ | ---------------- | ------------------- |
| Bronze       | bronze_Suppliers  | Supplier_ID      | Raw          | Suppliers    | Supplier_ID      | 1-1 Mapping         |
| Bronze       | bronze_Suppliers  | Supplier_Name    | Raw          | Suppliers    | Supplier_Name    | 1-1 Mapping         |
| Bronze       | bronze_Suppliers  | Contact_Number   | Raw          | Suppliers    | Contact_Number   | 1-1 Mapping         |
| Bronze       | bronze_Suppliers  | Product_ID       | Raw          | Suppliers    | Product_ID       | 1-1 Mapping         |

### Warehouses Table Mapping
| Target Layer | Target Table       | Target Field     | Source Layer | Source Table | Source Field     | Transformation Rule |
| ------------ | ------------------ | ---------------- | ------------ | ------------ | ---------------- | ------------------- |
| Bronze       | bronze_Warehouses  | Warehouse_ID     | Raw          | Warehouses   | Warehouse_ID     | 1-1 Mapping         |
| Bronze       | bronze_Warehouses  | Location         | Raw          | Warehouses   | Location         | 1-1 Mapping         |
| Bronze       | bronze_Warehouses  | Capacity         | Raw          | Warehouses   | Capacity         | 1-1 Mapping         |

### Inventory Table Mapping
| Target Layer | Target Table      | Target Field        | Source Layer | Source Table | Source Field        | Transformation Rule |
| ------------ | ----------------- | ------------------- | ------------ | ------------ | ------------------- | ------------------- |
| Bronze       | bronze_Inventory  | Inventory_ID        | Raw          | Inventory    | Inventory_ID        | 1-1 Mapping         |
| Bronze       | bronze_Inventory  | Product_ID          | Raw          | Inventory    | Product_ID          | 1-1 Mapping         |
| Bronze       | bronze_Inventory  | Quantity_Available  | Raw          | Inventory    | Quantity_Available  | 1-1 Mapping         |
| Bronze       | bronze_Inventory  | Warehouse_ID        | Raw          | Inventory    | Warehouse_ID        | 1-1 Mapping         |

### Orders Table Mapping
| Target Layer | Target Table    | Target Field | Source Layer | Source Table | Source Field | Transformation Rule |
| ------------ | --------------- | ------------ | ------------ | ------------ | ------------ | ------------------- |
| Bronze       | bronze_Orders   | Order_ID     | Raw          | Orders       | Order_ID     | 1-1 Mapping         |
| Bronze       | bronze_Orders   | Customer_ID  | Raw          | Orders       | Customer_ID  | 1-1 Mapping         |
| Bronze       | bronze_Orders   | Order_Date   | Raw          | Orders       | Order_Date   | 1-1 Mapping         |

### Order_Details Table Mapping
| Target Layer | Target Table          | Target Field        | Source Layer | Source Table  | Source Field        | Transformation Rule |
| ------------ | --------------------- | ------------------- | ------------ | ------------- | ------------------- | ------------------- |
| Bronze       | bronze_Order_Details  | Order_Detail_ID     | Raw          | Order_Details | Order_Detail_ID     | 1-1 Mapping         |
| Bronze       | bronze_Order_Details  | Order_ID            | Raw          | Order_Details | Order_ID            | 1-1 Mapping         |
| Bronze       | bronze_Order_Details  | Product_ID          | Raw          | Order_Details | Product_ID          | 1-1 Mapping         |
| Bronze       | bronze_Order_Details  | Quantity_Ordered    | Raw          | Order_Details | Quantity_Ordered    | 1-1 Mapping         |

### Shipments Table Mapping
| Target Layer | Target Table       | Target Field     | Source Layer | Source Table | Source Field     | Transformation Rule |
| ------------ | ------------------ | ---------------- | ------------ | ------------ | ---------------- | ------------------- |
| Bronze       | bronze_Shipments   | Shipment_ID      | Raw          | Shipments    | Shipment_ID      | 1-1 Mapping         |
| Bronze       | bronze_Shipments   | Order_ID         | Raw          | Shipments    | Order_ID         | 1-1 Mapping         |
| Bronze       | bronze_Shipments   | Shipment_Date    | Raw          | Shipments    | Shipment_Date    | 1-1 Mapping         |

### Returns Table Mapping
| Target Layer | Target Table     | Target Field     | Source Layer | Source Table | Source Field     | Transformation Rule |
| ------------ | ---------------- | ---------------- | ------------ | ------------ | ---------------- | ------------------- |
| Bronze       | bronze_Returns   | Return_ID        | Raw          | Returns      | Return_ID        | 1-1 Mapping         |
| Bronze       | bronze_Returns   | Order_ID         | Raw          | Returns      | Order_ID         | 1-1 Mapping         |
| Bronze       | bronze_Returns   | Return_Reason    | Raw          | Returns      | Return_Reason    | 1-1 Mapping         |

### Stock_Levels Table Mapping
| Target Layer | Target Table         | Target Field        | Source Layer | Source Table  | Source Field        | Transformation Rule |
| ------------ | -------------------- | ------------------- | ------------ | ------------- | ------------------- | ------------------- |
| Bronze       | bronze_Stock_Levels  | Stock_Level_ID      | Raw          | Stock_Levels  | Stock_Level_ID      | 1-1 Mapping         |
| Bronze       | bronze_Stock_Levels  | Warehouse_ID        | Raw          | Stock_Levels  | Warehouse_ID        | 1-1 Mapping         |
| Bronze       | bronze_Stock_Levels  | Product_ID          | Raw          | Stock_Levels  | Product_ID          | 1-1 Mapping         |
| Bronze       | bronze_Stock_Levels  | Reorder_Threshold   | Raw          | Stock_Levels  | Reorder_Threshold   | 1-1 Mapping         |

### Customers Table Mapping
| Target Layer | Target Table      | Target Field     | Source Layer | Source Table | Source Field     | Transformation Rule |
| ------------ | ----------------- | ---------------- | ------------ | ------------ | ---------------- | ------------------- |
| Bronze       | bronze_Customers  | Customer_ID      | Raw          | Customers    | Customer_ID      | 1-1 Mapping         |
| Bronze       | bronze_Customers  | Customer_Name    | Raw          | Customers    | Customer_Name    | 1-1 Mapping         |
| Bronze       | bronze_Customers  | Email            | Raw          | Customers    | Email            | 1-1 Mapping         |

## Data Type Compatibility

All data types are preserved from source to Bronze layer to maintain compatibility with Microsoft Fabric Lakehouse as Delta tables:

- **INT**: Mapped to INT in Delta tables
- **VARCHAR(n)**: Mapped to STRING in Delta tables
- **DATE**: Mapped to DATE in Delta tables

## Ingestion Details

### Data Ingestion Strategy
- **Ingestion Type**: Full load and incremental load support
- **File Format**: Delta table format for optimal performance
- **Compression**: Snappy compression for storage efficiency
- **Partitioning**: Date-based partitioning where applicable

### Metadata Management
- **Source System**: Inventory Management System
- **Target Platform**: Microsoft Fabric Lakehouse
- **Storage Format**: Delta Lake
- **Schema Evolution**: Supported through Delta Lake schema evolution

### Data Quality Considerations
- No data transformations applied at Bronze layer
- Original data structure and values preserved
- Data validation and cleansing deferred to Silver layer
- Audit columns to be added for lineage tracking

## Assumptions
1. Source system provides data in structured format
2. All source tables are available for ingestion
3. Primary key and foreign key relationships are maintained
4. Data types are compatible with Delta Lake format
5. No real-time streaming requirements for initial implementation

## Notes
- This mapping ensures complete preservation of source data structure
- All transformations, validations, and business rules will be applied in Silver layer
- Bronze layer serves as the single source of truth for raw data
- Delta Lake format provides ACID transactions and time travel capabilities