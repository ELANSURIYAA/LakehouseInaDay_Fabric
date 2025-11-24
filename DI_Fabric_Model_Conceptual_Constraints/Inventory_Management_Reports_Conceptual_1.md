_____________________________________________
## *Author*: AAVA
## *Created on*: 2024-12-19
## *Description*: Conceptual data model for Inventory Management Reports
## *Version*: 1
## *Updated on*: 2024-12-19
_____________________________________________

# Conceptual Data Model for Inventory Management Reports

## 1. Domain Overview

The Inventory Management domain encompasses comprehensive tracking and analysis of inventory operations across multiple warehouses. This domain covers stock level monitoring, supplier performance evaluation, sales-inventory correlation analysis, warehouse utilization optimization, and demand forecasting to support strategic inventory management decisions.

## 2. List of Entity Names with Descriptions

1. **Product**: Represents individual items or goods managed within the inventory system
2. **Warehouse**: Physical storage facilities where inventory is maintained
3. **Supplier**: External vendors who provide products to the organization
4. **Purchase Order**: Formal requests for products from suppliers
5. **Sales Transaction**: Records of product sales activities
6. **Inventory Level**: Current stock quantities for products in warehouses
7. **Stock Adjustment**: Records of inventory changes and modifications
8. **Shipment**: Delivery records from suppliers to warehouses
9. **Product Category**: Classification groups for organizing products
10. **Region**: Geographic areas where warehouses are located

## 3. List of Attributes for Each Entity

### Product
1. **Product Name**: Unique identifier name for each product
2. **Category**: Classification group the product belongs to
3. **Minimum Threshold Level**: Lowest acceptable stock level before reordering
4. **Maximum Threshold Level**: Highest recommended stock level
5. **Average Daily Sales**: Historical average of daily sales quantity
6. **Cost of Goods Sold**: Cost associated with producing or purchasing the product
7. **Historical Sales Data**: Past sales performance data
8. **Lead Time**: Time required for supplier to deliver the product

### Warehouse
1. **Warehouse Name**: Unique identifier for each warehouse facility
2. **Location**: Physical address or geographic location
3. **Total Capacity**: Maximum storage capacity in square feet or cubic meters
4. **Utilized Space**: Currently occupied storage space
5. **Underutilized Space**: Available unused storage space
6. **Region**: Geographic region where warehouse is located

### Supplier
1. **Supplier Name**: Unique identifier for each supplier
2. **Average Delivery Time**: Typical time taken for order delivery
3. **Order Fulfillment Rate**: Percentage of orders successfully fulfilled
4. **Rejected Items Percentage**: Percentage of delivered items that were rejected
5. **Delayed Delivery Percentage**: Percentage of orders delivered late
6. **Total Purchase Order Value**: Cumulative value of orders placed

### Purchase Order
1. **Purchase Order Value**: Monetary value of the order
2. **Order Date**: Date when order was placed
3. **Expected Delivery Date**: Planned delivery date
4. **Actual Delivery Date**: Actual date of delivery
5. **Order Status**: Current status of the purchase order
6. **Total Items Ordered**: Quantity of items in the order
7. **Defective Items**: Number of items received in defective condition

### Sales Transaction
1. **Sales Quantity**: Number of units sold
2. **Sales Date**: Date of the sales transaction
3. **Sales Value**: Monetary value of the sale
4. **Sales Trends**: Historical sales pattern data

### Inventory Level
1. **Current Stock Level**: Present quantity of product in warehouse
2. **Stock Replenishment Status**: Current status (Below, Optimal, Overstocked)
3. **Reorder Point**: Stock level that triggers reordering
4. **Average Inventory**: Mean inventory level over a period

### Stock Adjustment
1. **Adjustment Date**: Date when stock adjustment was made
2. **Adjustment Type**: Type of adjustment (increase, decrease, correction)
3. **Adjustment Quantity**: Amount of stock adjusted
4. **Adjustment Reason**: Reason for the stock adjustment

### Shipment
1. **Shipment Date**: Date when shipment was sent
2. **Delivery Date**: Date when shipment was received
3. **Shipment Status**: Current status of the shipment
4. **Items Delivered**: Quantity of items in the shipment

### Product Category
1. **Category Name**: Name of the product category
2. **Category Description**: Description of the category

### Region
1. **Region Name**: Name of the geographic region
2. **Region Description**: Description of the region

## 4. KPI List

1. **Days of Inventory Remaining**: Number of days current stock will last based on sales velocity
2. **Stockout Percentage**: Percentage of products or warehouses experiencing stockouts
3. **Overstock Percentage**: Percentage of products exceeding maximum threshold levels
4. **On-Time Delivery Rate**: Percentage of supplier deliveries made on time
5. **Average Lead Time**: Average time taken by suppliers for order delivery
6. **Defective Items Percentage**: Percentage of items received in defective condition
7. **Supplier Fulfillment Rate**: Percentage of orders successfully fulfilled by suppliers
8. **Inventory Turnover Ratio**: Rate at which inventory is sold and replaced
9. **Fast-Moving vs. Slow-Moving Product Ratio**: Comparison of product movement rates
10. **Average Days to Sell Inventory**: Average time taken to sell inventory
11. **Warehouse Utilization Rate**: Percentage of warehouse capacity being utilized
12. **Underutilized Space**: Amount of unused warehouse space
13. **Overstocked vs. Understocked Percentage**: Comparison of stock level statuses
14. **Forecast Accuracy**: Accuracy of demand predictions compared to actual demand
15. **Predicted vs. Actual Demand**: Comparison between forecasted and actual demand
16. **Seasonal Demand Trends**: Patterns in demand based on seasonal factors

## 5. Conceptual Data Model Diagram

| Source Entity | Relationship Key Field | Target Entity | Relationship Type |
|---------------|------------------------|---------------|-------------------|
| Product | product_name | Inventory Level | One-to-Many |
| Warehouse | warehouse_name | Inventory Level | One-to-Many |
| Product | product_name | Sales Transaction | One-to-Many |
| Warehouse | warehouse_name | Sales Transaction | One-to-Many |
| Supplier | supplier_name | Purchase Order | One-to-Many |
| Product | product_name | Purchase Order | Many-to-Many |
| Purchase Order | order_id | Shipment | One-to-Many |
| Product | product_name | Stock Adjustment | One-to-Many |
| Warehouse | warehouse_name | Stock Adjustment | One-to-Many |
| Product Category | category_name | Product | One-to-Many |
| Region | region_name | Warehouse | One-to-Many |
| Supplier | supplier_name | Shipment | One-to-Many |
| Warehouse | warehouse_name | Shipment | One-to-Many |

## 6. Common Data Elements in Report Requirements

1. **Product Name**: Referenced across all five reports for product identification
2. **Warehouse Name**: Used in inventory, correlation, and utilization reports
3. **Stock Level**: Common element in inventory and correlation reports
4. **Category**: Referenced in inventory, correlation, and forecast reports
5. **Sales Quantity**: Used in correlation and forecast reports
6. **Region**: Referenced in multiple reports for geographic analysis
7. **Supplier Name**: Common element in supplier performance reporting
8. **Delivery Time**: Referenced in supplier and inventory reports
9. **Historical Sales Data**: Used in correlation and forecast reports
10. **Inventory Levels**: Referenced across inventory, correlation, and utilization reports
11. **Capacity and Utilization**: Common elements in warehouse utilization reporting
12. **Threshold Levels**: Referenced in inventory management reports
13. **Order Fulfillment Data**: Common in supplier and inventory reports
14. **Seasonal Factors**: Referenced in demand forecasting reports
15. **Trend Data**: Common element across correlation and forecast reports