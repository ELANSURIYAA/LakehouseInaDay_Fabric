_____________________________________________
## *Author*: AAVA
## *Created on*:   
## *Description*:   PySpark pipeline to transform raw credit card acquisition data into the Bronze layer in Microsoft Fabric Lakehouse with audit logging, deduplication, and metadata tracking.
## *Version*: 1 
## *Updated on*: 
_____________________________________________

"""
Fabric Bronze Pipeline for Credit Card Acquisition
Transforms raw data into Bronze layer tables with audit logging, deduplication, and Microsoft Fabric best practices.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, current_timestamp
from pyspark.sql.types import IntegerType, StringType, TimestampType
import time
import sys

# ------------------
# 1. Spark Session Initialization
# ------------------
spark = SparkSession.builder.appName("Fabric Bronze Pipeline").getOrCreate()

# ------------------
# 2. Credential Management
# ------------------
try:
    from notebookutils import mssparkutils
    source_username = mssparkutils.credentials.getSecret("fabric-keyvault", "source-username")
    source_password = mssparkutils.credentials.getSecret("fabric-keyvault", "source-password")
    source_url = mssparkutils.credentials.getSecret("fabric-keyvault", "source-url")
    database_name = mssparkutils.credentials.getSecret("fabric-keyvault", "database-name")
    source_system = mssparkutils.credentials.getSecret("fabric-keyvault", "source-system")
    bronze_path = mssparkutils.credentials.getSecret("fabric-keyvault", "bronze-path")
except Exception as e:
    # Fallback: hardcoded or input-based (for demo)
    source_username = "<source_username>"
    source_password = "<source_password>"
    source_url = "<source_url>"
    database_name = "credit_card"
    source_system = "CreditCardSystem"
    bronze_path = "/lakehouse/default/bronze"

# ------------------
# 3. User Identity Capture
# ------------------
try:
    current_user = mssparkutils.env.getUserName()
except:
    try:
        current_user = spark.sparkContext.sparkUser()
    except:
        current_user = "Unknown User"

# ------------------
# 4. Audit Table Schema
# ------------------
from pyspark.sql.types import StructType, StructField

audit_schema = StructType([
    StructField("Record_ID", IntegerType(), False),
    StructField("Source_Table", StringType(), False),
    StructField("Load_Timestamp", TimestampType(), False),
    StructField("Processed_By", StringType(), False),
    StructField("Processing_Time", IntegerType(), False),
    StructField("Status", StringType(), False),
    StructField("Row_Count", IntegerType(), False)
])

audit_table = f"{bronze_path}/bz_audit"

# ------------------
# 5. Audit Logging Function
# ------------------
def log_audit(record_id, source_table, processing_time, status, row_count):
    from pyspark.sql import Row
    audit_row = [Row(
        Record_ID=record_id,
        Source_Table=source_table,
        Load_Timestamp=current_timestamp(),
        Processed_By=current_user,
        Processing_Time=processing_time,
        Status=status,
        Row_Count=row_count
    )]
    audit_df = spark.createDataFrame(audit_row, audit_schema)
    audit_df.write.format("delta").mode("append").option("mergeSchema", "true").save(audit_table)

# ------------------
# 6. Table List and Primary Keys (from DDL)
# ------------------
table_primary_keys = {
    "applicants": ["applicant_id"],
    "applications": ["application_id"],
    "card_products": ["card_product_id"],
    "credit_scores": ["credit_score_id"],
    "document_submissions": ["document_id"],
    "verification_results": ["verification_id"],
    "underwriting_decisions": ["decision_id"],
    "campaigns": ["campaign_id"],
    "application_campaigns": ["app_campaign_id"],
    "activations": ["activation_id"],
    "fraud_checks": ["fraud_check_id"],
    "offers": ["offer_id"],
    "offer_performance": ["offer_analytics_id"],
    "address_history": ["address_id"],
    "employment_info": ["employment_id"]
}

# Table mapping for raw to bronze
raw_to_bronze = {
    "applicants": "raw_applicants",
    "applications": "raw_applications",
    "card_products": "raw_card_products",
    "credit_scores": "raw_credit_scores",
    "document_submissions": "raw_document_submissions",
    "verification_results": "raw_verification_results",
    "underwriting_decisions": "raw_underwriting_decisions",
    "campaigns": "raw_campaigns",
    "application_campaigns": "raw_application_campaigns",
    "activations": "raw_activations",
    "fraud_checks": "raw_fraud_checks",
    "offers": "raw_offers",
    "offer_performance": "raw_offer_performance",
    "address_history": "raw_address_history",
    "employment_info": "raw_employment_info"
}

# ------------------
# 7. Bronze Data Loading Function
# ------------------
def load_to_bronze(table_name, record_id):
    start_time = time.time()
    bronze_tbl = f"bz_{table_name.lower()}"
    raw_tbl = raw_to_bronze[table_name]
    try:
        # Read from RAW (delta table)
        df = spark.read.format("delta").load(f"/lakehouse/default/raw/{raw_tbl}")
        # Filter NULLs for primary keys
        for pk in table_primary_keys[table_name]:
            df = df.filter(col(pk).isNotNull())
        # Deduplicate
        df = df.dropDuplicates(table_primary_keys[table_name])
        # Overwrite Load_Date and Update_Date
        df = df.withColumn("Load_Date", current_timestamp()) \
               .withColumn("Update_Date", current_timestamp()) \
               .withColumn("Source_System", lit(source_system))
        # Write to Bronze
        df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(f"{bronze_path}/{bronze_tbl}")
        row_count = df.count()
        processing_time = int(time.time() - start_time)
        log_audit(record_id, bronze_tbl, processing_time, "Success", row_count)
        print(f"Table {bronze_tbl} processed successfully. Rows: {row_count}")
    except Exception as e:
        processing_time = int(time.time() - start_time)
        log_audit(record_id, bronze_tbl, processing_time, f"Failure: {str(e)}", 0)
        print(f"Error processing {bronze_tbl}: {e}", file=sys.stderr)

# ------------------
# 8. Main Execution Logic
# ------------------
tables = list(table_primary_keys.keys())
record_id = 1
try:
    # Ensure audit table exists
    spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {audit_table} (
        Record_ID INT,
        Source_Table STRING,
        Load_Timestamp TIMESTAMP,
        Processed_By STRING,
        Processing_Time INT,
        Status STRING,
        Row_Count INT
    )
    USING DELTA
    """)
    for tbl in tables:
        load_to_bronze(tbl, record_id)
        record_id += 1
except Exception as main_e:
    print(f"Pipeline failed: {main_e}", file=sys.stderr)
finally:
    spark.stop()

# ------------------
# 9. Cost Reporting
# ------------------
api_cost_usd = 0.0004321  # Example cost, replace with actual API cost if available
print(f"API Cost (USD): {api_cost_usd}")
