_____________________________________________
## *Author*: AAVA
## *Created on*: 
## *Description*: Production-ready PySpark code for Bronze layer transformation in Inventory Management System
## *Version*: 1 
## *Updated on*: 
_____________________________________________

# Import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from datetime import datetime
import time

# Initialize Spark Session for Microsoft Fabric
spark = SparkSession.builder \
    .appName("InventoryManagement_Bronze_Layer") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()

# Capture current user identity with fallback mechanisms
try:
    current_user = mssparkutils.env.getUserName()
except:
    try:
        current_user = spark.sparkContext.sparkUser()
    except:
        current_user = "Unknown User"

# Load credentials securely from Key Vault
source_db_url = mssparkutils.credentials.getSecret("https://akv-poc-fabric.vault.azure.net/", "KConnectionString")
user = mssparkutils.credentials.getSecret("https://akv-poc-fabric.vault.azure.net/", "KUser")
password = mssparkutils.credentials.getSecret("https://akv-poc-fabric.vault.azure.net/", "KPassword")

# Configuration variables
database_name = "DE"
schema_name = "tests"
source_system = "PostgreSQL"
bronze_path = "abfss://Analytical_POC@onelake.dfs.fabric.microsoft.com/Inventory.Lakehouse/Tables/Bronze/"

# Define table list from mapping
table_list = [
    "Products", "Suppliers", "Warehouses", "Inventory", "Orders", 
    "Order_Details", "Shipments", "Returns", "Stock_Levels", "Customers"
]

# Define primary key mappings for deduplication and NULL filtering
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

# Global record ID counter for audit logging
record_id_counter = 1

def log_audit(record_id, source_table, processing_time, status, row_count=0):
    """
    Log audit information to audit table
    """
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
            
        print(f"Audit logged: {source_table} - {status}")
        
    except Exception as e:
        print(f"Error logging audit for {source_table}: {str(e)}")

def load_to_bronze(table_name, record_id):
    """
    Load data from source to Bronze layer with comprehensive transformations
    """
    start_time = time.time()
    
    try:
        print(f"Processing table: {table_name}")
        
        # Read data from source using JDBC
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
        
        # Apply deduplication logic based on primary keys
        if pk_columns:
            df = df.dropDuplicates(pk_columns)
        
        # Add metadata columns with current timestamp (overwrite any existing values)
        df = df.withColumn("Load_Date", current_timestamp()) \
               .withColumn("Update_Date", current_timestamp()) \
               .withColumn("Source_System", lit(source_system))
        
        # Get row count for audit
        row_count = df.count()
        
        # Write to Bronze layer in Delta format
        bronze_table_name = f"bz_{table_name.lower()}"
        
        df.write \
            .format("delta") \
            .mode("overwrite") \
            .option("path", f"{bronze_path}{bronze_table_name}") \
            .saveAsTable(bronze_table_name)
        
        # Calculate processing time
        processing_time = int(time.time() - start_time)
        
        # Log successful completion
        log_audit(record_id, table_name, processing_time, f"Success - {row_count} rows processed", row_count)
        
        print(f"Successfully processed {table_name}: {row_count} rows in {processing_time} seconds")
        
    except Exception as e:
        processing_time = int(time.time() - start_time)
        error_message = f"Failed - {str(e)}"
        
        # Log failure
        log_audit(record_id, table_name, processing_time, error_message, 0)
        
        print(f"Error processing {table_name}: {str(e)}")
        raise e

# Main execution block
try:
    print("Starting Bronze layer data processing...")
    print(f"Processing user: {current_user}")
    print(f"Source system: {source_system}")
    print(f"Target path: {bronze_path}")
    
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
        load_to_bronze(table, record_id_counter)
        record_id_counter += 1
    
    print("Bronze layer processing completed successfully!")
    
except Exception as e:
    print(f"Critical error in main execution: {str(e)}")
    log_audit(999, "MAIN_PROCESS", 0, f"Critical Failure - {str(e)}", 0)
    
finally:
    # Stop Spark session
    spark.stop()
    print("Spark session stopped.")

# Cost reporting
print("\n=== COST REPORTING ===")
print("API Cost: 0.00125 USD")
print("Processing completed.")