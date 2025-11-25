_____________________________________________
## *Author*: AAVA
## *Created on*: 2024-12-19
## *Description*: Conceptual data model for Inventory Management Reports
## *Version*: 1
## *Updated on*: 2024-12-19
_____________________________________________

# Conceptual Data Model for Inventory Management Reports

## 1. Domain Overview

This conceptual data model covers the Inventory Management domain, focusing on analytical reporting requirements for inventory stock levels, supplier performance, sales and inventory correlation, warehouse utilization, and product demand forecasting. The model supports decision-making processes for inventory managers, warehouse managers, procurement teams, and executives in optimizing inventory levels, supplier relationships, and warehouse operations.

## 2. List of Entity Names with Descriptions

1. **Product**: Represents items managed in the inventory system with their categorization and identification details
2. **Warehouse**: Physical storage locations where inventory is maintained with capacity and location information
3. **Supplier**: External vendors who provide products to the organization with performance tracking capabilities
4. **Inventory**: Current stock levels and status of products across different warehouses
5. **Sales**: Historical and current sales transactions and quantities for products
6. **Purchase Order**: Orders placed with suppliers for product procurement
7. **Delivery**: Shipment and delivery information for orders from suppliers
8. **Forecast**: Predictive demand data for products based on historical trends and seasonal factors

## 3. List of Attributes for Each Entity

### Product
1. **Product Name**: Unique identifier name for each product in the system
2. **Category**: Classification grouping for products for reporting and analysis purposes
3. **Cost of Goods Sold**: Financial value used for inventory turnover calculations

### Warehouse
1. **Warehouse Name**: Unique identifier for each warehouse location
2. **Location**: Geographic or address information for the warehouse
3. **Capacity**: Total storage capacity of the warehouse in square feet or cubic meters
4. **Utilized Space**: Currently occupied storage space in the warehouse
5. **Region**: Geographic region where the warehouse is located

### Supplier
1. **Supplier Name**: Unique identifier for each supplier in the system
2. **Average Delivery Time**: Typical time taken by supplier to deliver orders in days
3. **Order Fulfillment Rate**: Percentage of orders successfully fulfilled by the supplier
4. **Total Purchase Order Value**: Cumulative value of orders placed with the supplier
5. **Rejected Items Percentage**: Percentage of items rejected due to quality or other issues
6. **Delayed Delivery Percentage**: Percentage of orders delivered after the promised date

### Inventory
1. **Stock Level**: Current quantity of product available in warehouse
2. **Minimum Threshold Level**: Minimum stock level before reorder is required
3. **Maximum Threshold Level**: Maximum stock level to avoid overstocking
4. **Stock Replenishment Status**: Current status indicating below, optimal, or overstocked levels
5. **Average Daily Sales**: Historical average of daily sales for reorder calculations
6. **Lead Time**: Time required for supplier to deliver after order placement

### Sales
1. **Sales Quantity**: Number of units sold for a specific product
2. **Sales Trends**: Historical pattern of sales over time periods
3. **Average Inventory**: Average stock level maintained over a period

### Purchase Order
1. **Orders Delivered on Time**: Count of orders delivered within promised timeframe
2. **Total Orders**: Total number of orders placed with supplier
3. **Defective Items**: Count of items received with quality issues
4. **Total Items Ordered**: Total quantity of items ordered from supplier

### Delivery
1. **Delivery Time**: Actual time taken for order delivery
2. **Delivery Status**: On-time or delayed status of delivery

### Forecast
1. **Historical Sales Data**: Past sales information used for demand prediction
2. **Predicted Demand**: Forecasted demand for future periods
3. **Seasonal Factors**: Seasonal adjustments applied to demand forecasting
4. **Trend Factors**: Growth or decline trends applied to forecasting
5. **Forecast Accuracy**: Measure of how accurate previous forecasts were

## 4. KPI List

1. **Days of Inventory Remaining**: Number of days current stock will last based on sales velocity
2. **Stockout Percentage**: Percentage of products or warehouses experiencing stockouts
3. **Overstock Percentage**: Percentage of products exceeding maximum threshold levels
4. **On-Time Delivery Rate**: Percentage of supplier deliveries made on schedule
5. **Average Lead Time**: Average time suppliers take to deliver orders
6. **Defective Items Percentage**: Percentage of items received with quality issues
7. **Supplier Fulfillment Rate**: Percentage of orders successfully fulfilled by suppliers
8. **Inventory Turnover Ratio**: Rate at which inventory is sold and replaced over a period
9. **Fast-Moving vs Slow-Moving Product Ratio**: Comparison of product movement rates
10. **Average Days to Sell Inventory**: Average time taken to sell inventory
11. **Warehouse Utilization Rate**: Percentage of warehouse capacity being utilized
12. **Underutilized Space**: Amount of unused warehouse space
13. **Overstocked vs Understocked Percentage**: Comparison of stocking levels across warehouses
14. **Forecast Accuracy**: Accuracy percentage of demand predictions
15. **Predicted vs Actual Demand**: Comparison between forecasted and actual demand
16. **Seasonal Demand Trends**: Patterns of demand variation across seasons

## 5. Conceptual Data Model Diagram

| Source Entity | Relationship Key Field | Target Entity | Relationship Type |
|---------------|------------------------|---------------|-------------------|
| Product | Product Name | Inventory | One-to-Many |
| Warehouse | Warehouse Name | Inventory | One-to-Many |
| Product | Product Name | Sales | One-to-Many |
| Warehouse | Warehouse Name | Sales | One-to-Many |
| Supplier | Supplier Name | Purchase Order | One-to-Many |
| Product | Product Name | Purchase Order | One-to-Many |
| Purchase Order | Order Reference | Delivery | One-to-One |
| Product | Product Name | Forecast | One-to-Many |
| Warehouse | Warehouse Name | Forecast | One-to-Many |
| Inventory | Product Name | Sales | Many-to-Many |

## 6. Common Data Elements in Report Requirements

1. **Product Name**: Referenced across all five reports for product identification and analysis
2. **Warehouse Name**: Used in inventory stock levels, sales correlation, and warehouse utilization reports
3. **Category**: Product categorization used in multiple reports for grouping and analysis
4. **Stock Level**: Core inventory data used in stock levels and correlation reports
5. **Sales Quantity**: Sales data referenced in correlation and forecast reports
6. **Region**: Geographic grouping used across warehouse and sales analysis
7. **Supplier Name**: Referenced in supplier performance and procurement-related calculations
8. **Delivery Time**: Used in supplier performance and lead time calculations
9. **Historical Sales Data**: Foundation for forecasting and trend analysis across reports
10. **Threshold Levels**: Minimum and maximum levels used in inventory and warehouse reports