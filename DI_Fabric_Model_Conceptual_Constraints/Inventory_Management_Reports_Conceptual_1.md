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

1. **Product**: Represents items managed within the inventory system, including their categorization and identification
2. **Warehouse**: Physical storage locations where inventory is maintained, including capacity and location information
3. **Supplier**: External entities that provide products to the organization, including performance metrics
4. **Purchase Order**: Formal requests for products from suppliers, including delivery and fulfillment details
5. **Sales Transaction**: Records of product sales, including quantities and timing
6. **Inventory Level**: Current stock quantities and status for products across warehouses
7. **Threshold Configuration**: Minimum and maximum stock level settings for inventory management
8. **Demand Forecast**: Predictive data for future product demand based on historical trends

## 3. List of Attributes for Each Entity

### Product
1. **Product Name**: Unique identifier name for the product
2. **Category**: Classification grouping for the product
3. **Cost of Goods Sold**: Financial cost associated with the product

### Warehouse
1. **Warehouse Name**: Unique identifier for the warehouse facility
2. **Location**: Geographic location of the warehouse
3. **Total Capacity**: Maximum storage capacity in square feet or cubic meters
4. **Utilized Space**: Currently occupied storage space
5. **Region**: Geographic region where the warehouse is located

### Supplier
1. **Supplier Name**: Unique identifier for the supplier organization
2. **Average Delivery Time**: Typical time taken for order delivery in days
3. **Order Fulfillment Rate**: Percentage of orders successfully fulfilled
4. **Rejected Items Percentage**: Percentage of items rejected due to quality issues
5. **Delayed Delivery Percentage**: Percentage of orders delivered late

### Purchase Order
1. **Total Purchase Order Value**: Financial value of the purchase order
2. **Orders Delivered on Time**: Count of orders delivered within expected timeframe
3. **Total Orders**: Total number of orders placed
4. **Defective Items**: Count of items received with defects
5. **Total Items Ordered**: Total quantity of items in the order

### Sales Transaction
1. **Sales Quantity**: Number of units sold
2. **Sales Trends**: Historical sales patterns over time
3. **Average Daily Sales**: Average number of units sold per day

### Inventory Level
1. **Stock Level**: Current quantity of product in stock
2. **Stock Replenishment Status**: Current status (Below, Optimal, Overstocked)
3. **Average Inventory**: Average stock level over a period

### Threshold Configuration
1. **Minimum Threshold Level**: Minimum acceptable stock level
2. **Maximum Threshold Level**: Maximum desired stock level
3. **Lead Time**: Time required for stock replenishment

### Demand Forecast
1. **Predicted Demand**: Forecasted demand for next period
2. **Historical Sales Data**: Past sales data used for forecasting
3. **Seasonal Factors**: Seasonal adjustments for demand prediction
4. **Trend Factors**: Trend-based adjustments for demand prediction
5. **Actual Demand**: Realized demand for comparison with predictions

## 4. KPI List

1. **Days of Inventory Remaining**: Based on current stock and sales velocity
2. **Stockout Percentage**: Percentage of products or warehouses experiencing stockouts
3. **Overstock Percentage**: Percentage of inventory exceeding maximum thresholds
4. **On-Time Delivery Rate**: Percentage of supplier deliveries made on time
5. **Average Lead Time**: Average time for supplier deliveries in days
6. **Defective Items Percentage**: Percentage of items received with defects
7. **Supplier Fulfillment Rate**: Percentage of orders successfully fulfilled by suppliers
8. **Inventory Turnover Ratio**: Rate at which inventory is sold and replaced
9. **Fast-Moving vs. Slow-Moving Product Ratio**: Comparison of product movement rates
10. **Average Days to Sell Inventory**: Average time to sell current inventory
11. **Warehouse Utilization Rate**: Percentage of warehouse capacity being used
12. **Underutilized Space**: Amount of unused warehouse space
13. **Overstocked vs. Understocked Percentage**: Comparison of stock level distributions
14. **Forecast Accuracy**: Accuracy percentage of demand predictions
15. **Predicted vs. Actual Demand**: Comparison between forecasted and actual demand
16. **Seasonal Demand Trends**: Patterns in demand based on seasonal factors

## 5. Conceptual Data Model Diagram

| Source Entity | Relationship Key Field | Target Entity | Relationship Type |
|---------------|------------------------|---------------|-------------------|
| Product | product_name | Inventory Level | One-to-Many |
| Warehouse | warehouse_name | Inventory Level | One-to-Many |
| Product | product_name | Threshold Configuration | One-to-Many |
| Warehouse | warehouse_name | Threshold Configuration | One-to-Many |
| Supplier | supplier_name | Purchase Order | One-to-Many |
| Product | product_name | Purchase Order | Many-to-Many |
| Product | product_name | Sales Transaction | One-to-Many |
| Warehouse | warehouse_name | Sales Transaction | One-to-Many |
| Product | product_name | Demand Forecast | One-to-Many |
| Warehouse | warehouse_name | Demand Forecast | One-to-Many |

## 6. Common Data Elements in Report Requirements

1. **Product Name**: Referenced across all five reports for inventory tracking, sales analysis, and forecasting
2. **Warehouse Name**: Used in inventory stock levels, sales correlation, and warehouse utilization reports
3. **Category**: Product categorization used for grouping and analysis across multiple reports
4. **Stock Level**: Current inventory quantities referenced in stock levels and correlation reports
5. **Location/Region**: Geographic identifiers used for warehouse and supplier performance analysis
6. **Sales Quantity**: Sales data used in correlation and demand forecast reports
7. **Inventory Levels**: Stock quantities referenced in multiple reports for analysis and optimization
8. **Historical Sales Data**: Past sales information used for trend analysis and demand forecasting
9. **Delivery Time**: Supplier performance metric used for procurement decisions
10. **Utilization Metrics**: Capacity and space utilization data for warehouse optimization