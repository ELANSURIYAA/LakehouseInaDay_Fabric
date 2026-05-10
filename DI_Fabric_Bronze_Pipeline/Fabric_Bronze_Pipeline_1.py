_____________________________________________
\
## *Author*: AAVA
\
## *Created on*:   
\
## *Description*:   PySpark pipeline for ingesting raw credit card business data into the Bronze layer (Delta tables) in Microsoft Fabric Lakehouse, with audit logging and metadata tracking.
\
## *Version*: 1 
\
## *Updated on*: 
\
_____________________________________________
\

\
import sys
\
import time
\
from datetime import datetime
\
from pyspark.sql import SparkSession
\
from pyspark.sql.functions import col, current_timestamp, lit
\
from pyspark.sql.types import *
\

\
# Initialize Spark session for Microsoft Fabric
\
spark = SparkSession.builder.appName('Fabric Bronze Pipeline').getOrCreate()
\

\
# Secure credential loading (replace with mssparkutils.credentials.getSecret in Fabric)
\
try:
\
    from notebookutils import mssparkutils
\
    db_username = mssparkutils.credentials.getSecret('fabric-kv', 'db-username')
\
    db_password = mssparkutils.credentials.getSecret('fabric-kv', 'db-password')
\
except Exception:
\
    db_username = '<db_username>'
\
    db_password = '<db_password>'
\

\
# Metadata
\
source_system = 'CreditCardBusiness'  # update as needed
\
bronze_path = '/lakehouse/default/Files/bronze/'  # update as needed
\
audit_table = 'bz_audit'
\

\
# Capture current user identity
\
try:
\
    current_user = mssparkutils.env.getUserName()
\
except Exception:
\
    try:
\
        current_user = spark.sparkContext.sparkUser()
\
    except Exception:
\
        current_user = 'Unknown User'
\

\
# Audit table schema
\
audit_schema = StructType([
\
    StructField('Record_ID', IntegerType(), False),
\
    StructField('Source_Table', StringType(), False),
\
    StructField('Load_Timestamp', TimestampType(), False),
\
    StructField('Processed_By', StringType(), False),
\
    StructField('Processing_Time', IntegerType(), False),
\
    StructField('Status', StringType(), False),
\
    StructField('Row_Count', IntegerType(), False)
\
])
\

\
# Helper: Get next audit record_id
\
def get_next_record_id():
\
    try:
\
        df = spark.read.format('delta').load(f'{bronze_path}{audit_table}')
\
        max_id = df.agg({'Record_ID': 'max'}).collect()[0][0]
\
        return int(max_id) + 1 if max_id is not None else 1
\
    except Exception:
\
        return 1
\

\
# Audit logging function
\
def log_audit(source_table, processing_time, status, row_count):
\
    record_id = get_next_record_id()
\
    audit_df = spark.createDataFrame([
\
        (record_id, source_table, datetime.now(), current_user, processing_time, status, row_count)
\
    ], audit_schema)
\
    audit_df.write.format('delta').mode('append').save(f'{bronze_path}{audit_table}')
\

\
# Table definitions (from mapping)
\
table_mappings = {
\
    'bz_applicants': {
\
        'raw_table': 'raw_applicants',
\
        'primary_keys': ['applicant_id'],
\
        'columns': ['applicant_id', 'full_name', 'email', 'phone_number', 'dob', 'ssn', 'channel']
\
    },
\
    'bz_applications': {
\
        'raw_table': 'raw_applications',
\
        'primary_keys': ['application_id'],
\
        'columns': ['application_id', 'applicant_id', 'card_product_id', 'application_date', 'status', 'approval_date', 'rejection_reason']
\
    },
\
    'bz_card_products': {
\
        'raw_table': 'raw_card_products',
\
        'primary_keys': ['card_product_id'],
\
        'columns': ['card_product_id', 'card_name', 'category', 'interest_rate', 'annual_fee']
\
    },
\
    'bz_credit_scores': {
\
        'raw_table': 'raw_credit_scores',
\
        'primary_keys': ['credit_score_id'],
\
        'columns': ['credit_score_id', 'applicant_id', 'score', 'score_date']
\
    },
\
    'bz_document_submissions': {
\
        'raw_table': 'raw_document_submissions',
\
        'primary_keys': ['document_id'],
\
        'columns': ['document_id', 'application_id', 'document_type', 'upload_date', 'verified_flag']
\
    },
\
    'bz_verification_results': {
\
        'raw_table': 'raw_verification_results',
\
        'primary_keys': ['verification_id'],
\
        'columns': ['verification_id', 'application_id', 'verification_type', 'result', 'verified_on']
\
    },
\
    'bz_underwriting_decisions': {
\
        'raw_table': 'raw_underwriting_decisions',
\
        'primary_keys': ['decision_id'],
\
        'columns': ['decision_id', 'application_id', 'decision', 'decision_reason', 'decision_date']
\
    },
\
    'bz_campaigns': {
\
        'raw_table': 'raw_campaigns',
\
        'primary_keys': ['campaign_id'],
\
        'columns': ['campaign_id', 'campaign_name', 'channel', 'start_date', 'end_date']
\
    },
\
    'bz_application_campaigns': {
\
        'raw_table': 'raw_application_campaigns',
\
        'primary_keys': ['app_campaign_id'],
\
        'columns': ['app_campaign_id', 'application_id', 'campaign_id']
\
    },
\
    'bz_activations': {
\
        'raw_table': 'raw_activations',
\
        'primary_keys': ['activation_id'],
\
        'columns': ['activation_id', 'application_id', 'activation_date', 'first_transaction_amount']
\
    },
\
    'bz_fraud_checks': {
\
        'raw_table': 'raw_fraud_checks',
\
        'primary_keys': ['fraud_check_id'],
\
        'columns': ['fraud_check_id', 'application_id', 'check_type', 'check_result', 'check_date']
\
    },
\
    'bz_offers': {
\
        'raw_table': 'raw_offers',
\
        'primary_keys': ['offer_id'],
\
        'columns': ['offer_id', 'card_product_id', 'offer_detail', 'valid_from', 'valid_to']
\
    },
\
    'bz_offer_performance': {
\
        'raw_table': 'raw_offer_performance',
\
        'primary_keys': ['offer_analytics_id'],
\
        'columns': ['offer_analytics_id', 'offer_id', 'applications_count', 'activations_count']
\
    },
\
    'bz_address_history': {
\
        'raw_table': 'raw_address_history',
\
        'primary_keys': ['address_id'],
\
        'columns': ['address_id', 'applicant_id', 'address_type', 'street', 'city', 'state', 'zip']
\
    },
\
    'bz_employment_info': {
\
        'raw_table': 'raw_employment_info',
\
        'primary_keys': ['employment_id'],
\
        'columns': ['employment_id', 'applicant_id', 'employer_name', 'job_title', 'income', 'employment_type']
\
    }
\
}
\

\
# Bronze table loader
\
def load_to_bronze(table_name, mapping):
\
    start_time = time.time()
\
    status = 'Success'
\
    row_count = 0
\
    try:
\
        raw_df = spark.read.format('delta').load(f'{bronze_path}{mapping["raw_table"]}')
\
        # Filter NOT NULL for primary keys
\
        for pk in mapping['primary_keys']:
\
            raw_df = raw_df.filter(col(pk).isNotNull())
\
        # Deduplicate
\
        dedup_df = raw_df.dropDuplicates(mapping['primary_keys'])
\
        # Select columns and add metadata (overwrite Load_Date/Update_Date)
\
        bronze_df = dedup_df.select(*mapping['columns']) \n\
            .withColumn('Load_Date', current_timestamp()) \n\
            .withColumn('Update_Date', current_timestamp()) \n\
            .withColumn('Source_System', lit(source_system))
\
        # Write to bronze table
\
        bronze_df.write.format('delta').mode('overwrite').save(f'{bronze_path}{table_name}')
\
        row_count = bronze_df.count()
\
    except Exception as e:
\
        status = f'Failure: {str(e)}'
\
    finally:
\
        processing_time = int(time.time() - start_time)
\
        log_audit(table_name, processing_time, status, row_count)
\

\
# Main execution
\
if __name__ == '__main__':
\
    # Create audit table if not exists
\
    try:
\
        spark.sql(f"""
\
        CREATE TABLE IF NOT EXISTS {audit_table} (
\
            Record_ID INT,
\
            Source_Table STRING,
\
            Load_Timestamp TIMESTAMP,
\
            Processed_By STRING,
\
            Processing_Time INT,
\
            Status STRING,
\
            Row_Count INT
\
        ) USING DELTA LOCATION '{bronze_path}{audit_table}'
\
        """)
\
    except Exception:
\
        pass
\
    # Process each table
\
    for table_name, mapping in table_mappings.items():
\
        print(f'Processing {table_name}...')
\
        load_to_bronze(table_name, mapping)
\
    spark.stop()
\

\
# API Cost Reporting
\
api_cost_usd = 0.0001  # Example: update with real API cost if available
\
print(f'API call cost (USD): {api_cost_usd}')
\