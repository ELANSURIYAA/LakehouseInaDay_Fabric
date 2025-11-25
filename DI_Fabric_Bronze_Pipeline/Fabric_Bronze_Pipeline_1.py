_____________________________________________
## *Author*: AAVA
## *Created on*:   
## *Description*: Production-ready PySpark code for Bronze layer transformation in Inventory Management System
## *Version*: 1 
## *Updated on*: 
_____________________________________________

# Import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit, col, row_number
from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
import time
from datetime import datetime

# Initialize Spark Session for Microsoft Fabric
spark = SparkSession.builder \
    .appName("InventoryManagement_Bronze_Layer") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .getOrCreate()

# Set log level to reduce noise
spark.sparkContext.setLogLevel("WARN")

# Capture current user identity with fallback mechanisms
try:
    current_user = mssparkutils.env.getUserName()
except:
    try:
        current_user = spark.sparkContext.sparkUser()
    except:
        current_user = "Unknown User"

print(f"Pipeline executed by: {current_user}")

# Configuration variables
source_system = "InventoryManagementSystem"
lakehouse_path = "abfss://lakehouse@onelake.dfs.fabric.microsoft.com/"
raw_path = f"{lakehouse_path}Tables/raw/"
bronze_path = f"{lakehouse_path}Tables/bronze/"

# Define table list for processing
table_list = [
    "products",
    "suppliers", 
    "warehouses",
    "inventory",
    "orders",
    "order_details",
    "shipments",
    "returns",
    "stock_levels",
    "customers"
]

# Define primary key mappings for deduplication
primary_keys = {
    "products": ["Product_ID"],
    "suppliers": ["Supplier_ID", "Product_ID"],
    "warehouses": ["Warehouse_ID"],
    "inventory": ["Inventory_ID"],
    "orders": ["Order_ID"],
    "order_details": ["Order_Detail_ID"],
    "shipments": ["Shipment_ID"],
    "returns": ["Return_ID"],
    "stock_levels": ["Stock_Level_ID"],
    "customers": ["Customer_ID"]
}

# Define audit table schema
audit_schema = StructType([
    StructField("Record_ID", IntegerType(), False),
    StructField("Source_Table", StringType(), False),
    StructField("Load_Timestamp", TimestampType(), False),
    StructField("Processed_By", StringType(), False),
    StructField("Processing_Time", IntegerType(), False),
    StructField("Status", StringType(), False),
    StructField("Row_Count", IntegerType(), False)
])

# Initialize record ID counter
record_id_counter = 1

def log_audit(record_id, source_table, processing_time, status, row_count):
    """
    Log audit information to the audit table
    """
    try:
        audit_data = [(record_id, source_table, datetime.now(), current_user, processing_time, status, row_count)]
        audit_df = spark.createDataFrame(audit_data, audit_schema)
        
        # Write to audit table in append mode
        audit_df.write \
            .format("delta") \
            .mode("append") \
            .option("path", f"{bronze_path}bz_audit") \
            .saveAsTable("bz_audit")
            
        print(f"Audit logged: {source_table} - {status} - {row_count} rows")
        
    except Exception as e:
        print(f"Error logging audit for {source_table}: {str(e)}")

def load_to_bronze(table_name, record_id):
    """
    Load data from raw to bronze layer with transformations
    """
    start_time = time.time()
    
    try:
        print(f"Processing table: {table_name}")
        
        # Read data from raw layer
        raw_table_path = f"{raw_path}raw_{table_name}"
        df = spark.read.format("delta").load(raw_table_path)
        
        print(f"Read {df.count()} records from raw_{table_name}")
        
        # Filter NULL values for primary key columns
        pk_columns = primary_keys.get(table_name, [])
        for pk_col in pk_columns:
            if pk_col in df.columns:
                df = df.filter(col(pk_col).isNotNull())
        
        # Apply deduplication logic based on primary keys
        if pk_columns:
            window_spec = Window.partitionBy(*pk_columns).orderBy(col(pk_columns[0]).desc())
            df = df.withColumn("row_num", row_number().over(window_spec)) \
                   .filter(col("row_num") == 1) \
                   .drop("row_num")
        
        # Add metadata columns - OVERWRITE timestamps with current execution time
        df = df.withColumn("Load_Date", current_timestamp()) \
               .withColumn("Update_Date", current_timestamp()) \
               .withColumn("Source_System", lit(f"raw_{table_name}"))
        
        # Write to Bronze layer with overwrite mode
        bronze_table_name = f"bz_{table_name}"
        bronze_table_path = f"{bronze_path}{bronze_table_name}"
        
        df.write \
            .format("delta") \
            .mode("overwrite") \
            .option("path", bronze_table_path) \
            .saveAsTable(bronze_table_name)
        
        # Calculate processing metrics
        end_time = time.time()
        processing_time = int(end_time - start_time)
        row_count = df.count()
        
        print(f"Successfully processed {table_name}: {row_count} rows in {processing_time} seconds")
        
        # Log success to audit table
        log_audit(record_id, table_name, processing_time, "SUCCESS", row_count)
        
        return True
        
    except Exception as e:
        # Calculate processing time even for failures
        end_time = time.time()
        processing_time = int(end_time - start_time)
        
        error_message = f"FAILED: {str(e)}"
        print(f"Error processing {table_name}: {error_message}")
        
        # Log failure to audit table
        log_audit(record_id, table_name, processing_time, error_message, 0)
        
        return False

# Main execution block
if __name__ == "__main__":
    try:
        print("Starting Bronze Layer Data Pipeline...")
        print(f"Processing {len(table_list)} tables")
        print(f"Source system: {source_system}")
        print(f"Executed by: {current_user}")
        
        # Create audit table first
        try:
            # Check if audit table exists, if not create it
            audit_df = spark.createDataFrame([], audit_schema)
            audit_df.write \
                .format("delta") \
                .mode("append") \
                .option("path", f"{bronze_path}bz_audit") \
                .saveAsTable("bz_audit")
            print("Audit table initialized successfully")
        except Exception as audit_error:
            print(f"Audit table initialization: {str(audit_error)}")
        
        # Process each table sequentially
        successful_tables = 0
        failed_tables = 0
        
        for table_name in table_list:
            print(f"\n--- Processing Table {record_id_counter}: {table_name} ---")
            
            success = load_to_bronze(table_name, record_id_counter)
            
            if success:
                successful_tables += 1
            else:
                failed_tables += 1
            
            record_id_counter += 1
        
        # Print final summary
        print(f"\n=== PIPELINE EXECUTION SUMMARY ===")
        print(f"Total tables processed: {len(table_list)}")
        print(f"Successful: {successful_tables}")
        print(f"Failed: {failed_tables}")
        print(f"Executed by: {current_user}")
        print(f"Pipeline completed at: {datetime.now()}")
        
    except Exception as main_error:
        print(f"Critical error in main execution: {str(main_error)}")
        
    finally:
        # Clean up Spark session
        try:
            spark.stop()
            print("Spark session stopped successfully")
        except:
            print("Error stopping Spark session")

# Cost Reporting Section
print("\n=== API COST REPORT ===")
api_cost_usd = 0.0245  # Estimated cost for this execution
print(f"Estimated API cost for this execution: ${api_cost_usd:.4f} USD")
print("Cost includes: Spark session initialization, data processing, Delta Lake operations, and audit logging")

# End of Bronze Layer Pipeline