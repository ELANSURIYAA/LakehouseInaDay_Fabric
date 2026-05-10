_____________________________________________
## *Author*: AAVA
## *Created on*:   
## *Description*:   Bronze layer physical data model for Credit Card Acquisition Reporting (raw ingestion tables for lakehouse delta tables)
## *Version*: 1 
## *Updated on*: 
_____________________________________________

1. Bronze Layer DDL Script

-- 1. bronze_applicants
CREATE TABLE IF NOT EXISTS bronze_applicants (
    applicant_id NUMBER,
    full_name STRING,
    email STRING,
    phone_number STRING,
    dob DATE,
    ssn STRING,
    channel STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 2. bronze_applications
CREATE TABLE IF NOT EXISTS bronze_applications (
    application_id NUMBER,
    applicant_id NUMBER,
    card_product_id NUMBER,
    application_date DATE,
    status STRING,
    approval_date DATE,
    rejection_reason STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 3. bronze_card_products
CREATE TABLE IF NOT EXISTS bronze_card_products (
    card_product_id NUMBER,
    card_name STRING,
    category STRING,
    interest_rate FLOAT,
    annual_fee FLOAT,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 4. bronze_credit_scores
CREATE TABLE IF NOT EXISTS bronze_credit_scores (
    credit_score_id NUMBER,
    applicant_id NUMBER,
    score NUMBER,
    score_date DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 5. bronze_document_submissions
CREATE TABLE IF NOT EXISTS bronze_document_submissions (
    document_id NUMBER,
    application_id NUMBER,
    document_type STRING,
    upload_date DATE,
    verified_flag BOOLEAN,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 6. bronze_verification_results
CREATE TABLE IF NOT EXISTS bronze_verification_results (
    verification_id NUMBER,
    application_id NUMBER,
    verification_type STRING,
    result STRING,
    verified_on DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 7. bronze_underwriting_decisions
CREATE TABLE IF NOT EXISTS bronze_underwriting_decisions (
    decision_id NUMBER,
    application_id NUMBER,
    decision STRING,
    decision_reason STRING,
    decision_date DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 8. bronze_campaigns
CREATE TABLE IF NOT EXISTS bronze_campaigns (
    campaign_id NUMBER,
    campaign_name STRING,
    channel STRING,
    start_date DATE,
    end_date DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 9. bronze_application_campaigns
CREATE TABLE IF NOT EXISTS bronze_application_campaigns (
    app_campaign_id NUMBER,
    application_id NUMBER,
    campaign_id NUMBER,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 10. bronze_activations
CREATE TABLE IF NOT EXISTS bronze_activations (
    activation_id NUMBER,
    application_id NUMBER,
    activation_date DATE,
    first_transaction_amount FLOAT,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 11. bronze_fraud_checks
CREATE TABLE IF NOT EXISTS bronze_fraud_checks (
    fraud_check_id NUMBER,
    application_id NUMBER,
    check_type STRING,
    check_result STRING,
    check_date DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 12. bronze_offers
CREATE TABLE IF NOT EXISTS bronze_offers (
    offer_id NUMBER,
    card_product_id NUMBER,
    offer_detail STRING,
    valid_from DATE,
    valid_to DATE,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 13. bronze_offer_performance
CREATE TABLE IF NOT EXISTS bronze_offer_performance (
    offer_analytics_id NUMBER,
    offer_id NUMBER,
    applications_count NUMBER,
    activations_count NUMBER,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 14. bronze_address_history
CREATE TABLE IF NOT EXISTS bronze_address_history (
    address_id NUMBER,
    applicant_id NUMBER,
    address_type STRING,
    street STRING,
    city STRING,
    state STRING,
    zip STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 15. bronze_employment_info
CREATE TABLE IF NOT EXISTS bronze_employment_info (
    employment_id NUMBER,
    applicant_id NUMBER,
    employer_name STRING,
    job_title STRING,
    income FLOAT,
    employment_type STRING,
    load_timestamp TIMESTAMP_NTZ,
    update_timestamp TIMESTAMP_NTZ,
    source_system STRING
)
USING DELTA;

-- 16. bronze_audit
CREATE TABLE IF NOT EXISTS bronze_audit (
    record_id NUMBER AUTOINCREMENT,
    source_table STRING,
    load_timestamp TIMESTAMP_NTZ,
    processed_by STRING,
    processing_time NUMBER,
    status STRING
)
USING DELTA;
