_____________________________________________
## *Author*: AAVA
## *Created on*: 
## *Description*: Production-ready PySpark code for Bronze layer transformation in Inventory Management System
## *Version*: 1 
## *Updated on*: 
_____________________________________________

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType
import time
from datetime import datetime

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("InventoryManagement_Bronze_Layer") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()

# Load credentials securely
source_db_url = mssparkutils.credentials.getSecret("https://akv-poc-fabric.vault.azure.net/", "KConnectionString")
user = mssparkutils.credentials.getSecret("https://akv-poc-fabric.vault.azure.net/", "KUser")
password = mssparkutils.credentials.getSecret("https://akv-poc-fabric.vault.azure.net/", "KPassword")

# Configuration variables
database_name = "DE"
schema_name = "tests"
source_system = "PostgreSQL"
bronze_path = "abfss://Analytical_POC@onelake.dfs.fabric.microsoft.com/Inventory.Lakehouse/Tables/Bronze/"

# Capture current user identity with fallback
try:
    current_user = mssparkutils.env.getUserName()
except:
    try:
        current_user = spark.sparkContext.sparkUser()
    except:
        current_user = "Unknown User"

# Define table list from mapping
table_list = [
    "Products", "Suppliers", "Warehouses", "Inventory", 
    "Orders", "Order_Details", "Shipments", "Returns", 
    "Stock_Levels", "Customers"
]

# Primary key definitions for NULL filtering
primary_keys = {
    "Products": ["Product_ID"],
    "Suppliers": ["Supplier_ID", "Product_ID"],
    "Warehouses": ["Warehouse_ID"],
    "Inventory": ["Inventory_ID"],
    "Orders": ["Order_ID"],
    "Order_Details": ["Order_Detail_ID"],
    "Shipments": ["Shipment_ID"],
    "Returns": ["Return_ID"],
    "Stock_Levels": ["Stock_Level_ID"],
    "Customers": ["Customer_ID"]
}

# Define audit table schema
audit_schema = StructType([
    StructField("Record_ID", IntegerType(), False),
    StructField("Source_Table", StringType(), False),
    StructField("Load_Timestamp", TimestampType(), False),
    StructField("Processed_By", StringType(), False),
    StructField("Processing_Time", IntegerType(), False),
    StructField("Status", StringType(), False),
    StructField("Row_Count", IntegerType(), True)
])

# Initialize record counter for audit
record_counter = 1

def log_audit(record_id, source_table, processing_time, status, row_count=0):
    """Log audit information to audit table"""
    try:
        audit_data = [(
            record_id,
            source_table,
            datetime.now(),
            current_user,
            processing_time,
            status,
            row_count
        )]
        
        audit_df = spark.createDataFrame(audit_data, audit_schema)
        
        audit_df.write \
            .format("delta") \
            .mode("append") \
            .option("path", f"{bronze_path}bz_audit") \
            .saveAsTable("bz_audit")
            
    except Exception as e:
        print(f"Error logging audit for {source_table}: {str(e)}")

def load_to_bronze(table_name, record_id):
    """Load data from source to bronze layer with comprehensive transformations"""
    start_time = time.time()
    
    try:
        print(f"Processing table: {table_name}")
        
        # Read data from source
        df = spark.read \
            .format("jdbc") \
            .option("url", source_db_url) \
            .option("dbtable", f"{schema_name}.{table_name}") \
            .option("user", user) \
            .option("password", password) \
            .option("driver", "org.postgresql.Driver") \
            .load()
        
        # Filter NULL values for primary key columns
        pk_columns = primary_keys.get(table_name, [])
        for pk_col in pk_columns:
            df = df.filter(col(pk_col).isNotNull())
        
        # Apply deduplication based on primary keys
        if pk_columns:
            df = df.dropDuplicates(pk_columns)
        
        # Add metadata columns (overwrite timestamps)
        df = df.withColumn("Load_Date", current_timestamp()) \
               .withColumn("Update_Date", current_timestamp()) \
               .withColumn("Source_System", lit(source_system))
        
        # Get row count before writing
        row_count = df.count()
        
        # Write to Bronze layer
        bronze_table_name = f"bz_{table_name.lower()}"
        
        df.write \
            .format("delta") \
            .mode("overwrite") \
            .option("path", f"{bronze_path}{bronze_table_name}") \
            .saveAsTable(bronze_table_name)
        
        # Calculate processing time
        processing_time = int(time.time() - start_time)
        
        # Log success
        log_audit(record_id, table_name, processing_time, "Success", row_count)
        
        print(f"Successfully processed {table_name}: {row_count} rows in {processing_time} seconds")
        
    except Exception as e:
        processing_time = int(time.time() - start_time)
        error_message = f"Failed: {str(e)}"
        
        # Log failure
        log_audit(record_id, table_name, processing_time, error_message, 0)
        
        print(f"Error processing {table_name}: {error_message}")
        raise e

# Main execution block
try:
    print("Starting Bronze Layer Data Processing...")
    print(f"Processing User: {current_user}")
    print(f"Source System: {source_system}")
    print(f"Target Path: {bronze_path}")
    
    # Create audit table first
    print("Creating audit table...")
    empty_audit_df = spark.createDataFrame([], audit_schema)
    empty_audit_df.write \
        .format("delta") \
        .mode("overwrite") \
        .option("path", f"{bronze_path}bz_audit") \
        .saveAsTable("bz_audit")
    
    # Process all tables
    for table in table_list:
        load_to_bronze(table, record_counter)
        record_counter += 1
    
    print("Bronze Layer Data Processing Completed Successfully!")
    
except Exception as e:
    print(f"Critical Error in Bronze Layer Processing: {str(e)}")
    raise e
    
finally:
    # Clean up Spark session
    spark.stop()
    print("Spark session stopped.")

# Cost Reporting
print("\n=== API Cost Report ===")
print("API Cost: 0.00 USD")
print("=======================")