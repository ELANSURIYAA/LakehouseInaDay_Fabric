_____________________________________________
## *Author*: AAVA
## *Created on*:   
## *Description*:   Bronze layer data mapping for Credit Card Acquisition Reporting (raw-to-bronze ingestion, delta tables)
## *Version*: 1 
## *Updated on*: 
_____________________________________________

### Data Mapping for Bronze Layer

| Target Layer | Target Table                | Target Field            | Source Layer | Source Table                | Source Field            | Transformation Rule |
| ------------ | -------------------------- | ----------------------- | ------------ | -------------------------- | ----------------------- | ------------------- |
| Bronze       | bronze_applicants          | applicant_id            | Raw          | raw_applicants             | applicant_id            | 1-1 Mapping         |
| Bronze       | bronze_applicants          | full_name               | Raw          | raw_applicants             | full_name               | 1-1 Mapping         |
| Bronze       | bronze_applicants          | email                   | Raw          | raw_applicants             | email                   | 1-1 Mapping         |
| Bronze       | bronze_applicants          | phone_number            | Raw          | raw_applicants             | phone_number            | 1-1 Mapping         |
| Bronze       | bronze_applicants          | dob                     | Raw          | raw_applicants             | dob                     | 1-1 Mapping         |
| Bronze       | bronze_applicants          | ssn                     | Raw          | raw_applicants             | ssn                     | 1-1 Mapping         |
| Bronze       | bronze_applicants          | channel                 | Raw          | raw_applicants             | channel                 | 1-1 Mapping         |
| Bronze       | bronze_applicants          | load_timestamp          | Raw          | raw_applicants             | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_applicants          | update_timestamp        | Raw          | raw_applicants             | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_applicants          | source_system           | Raw          | raw_applicants             | source_system           | 1-1 Mapping         |
| Bronze       | bronze_applications        | application_id          | Raw          | raw_applications           | application_id          | 1-1 Mapping         |
| Bronze       | bronze_applications        | applicant_id            | Raw          | raw_applications           | applicant_id            | 1-1 Mapping         |
| Bronze       | bronze_applications        | card_product_id         | Raw          | raw_applications           | card_product_id         | 1-1 Mapping         |
| Bronze       | bronze_applications        | application_date        | Raw          | raw_applications           | application_date        | 1-1 Mapping         |
| Bronze       | bronze_applications        | status                  | Raw          | raw_applications           | status                  | 1-1 Mapping         |
| Bronze       | bronze_applications        | approval_date           | Raw          | raw_applications           | approval_date           | 1-1 Mapping         |
| Bronze       | bronze_applications        | rejection_reason        | Raw          | raw_applications           | rejection_reason        | 1-1 Mapping         |
| Bronze       | bronze_applications        | load_timestamp          | Raw          | raw_applications           | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_applications        | update_timestamp        | Raw          | raw_applications           | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_applications        | source_system           | Raw          | raw_applications           | source_system           | 1-1 Mapping         |
| Bronze       | bronze_card_products       | card_product_id         | Raw          | raw_card_products          | card_product_id         | 1-1 Mapping         |
| Bronze       | bronze_card_products       | card_name               | Raw          | raw_card_products          | card_name               | 1-1 Mapping         |
| Bronze       | bronze_card_products       | category                | Raw          | raw_card_products          | category                | 1-1 Mapping         |
| Bronze       | bronze_card_products       | interest_rate           | Raw          | raw_card_products          | interest_rate           | 1-1 Mapping         |
| Bronze       | bronze_card_products       | annual_fee              | Raw          | raw_card_products          | annual_fee              | 1-1 Mapping         |
| Bronze       | bronze_card_products       | load_timestamp          | Raw          | raw_card_products          | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_card_products       | update_timestamp        | Raw          | raw_card_products          | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_card_products       | source_system           | Raw          | raw_card_products          | source_system           | 1-1 Mapping         |
| Bronze       | bronze_credit_scores       | credit_score_id         | Raw          | raw_credit_scores          | credit_score_id         | 1-1 Mapping         |
| Bronze       | bronze_credit_scores       | applicant_id            | Raw          | raw_credit_scores          | applicant_id            | 1-1 Mapping         |
| Bronze       | bronze_credit_scores       | score                   | Raw          | raw_credit_scores          | score                   | 1-1 Mapping         |
| Bronze       | bronze_credit_scores       | score_date              | Raw          | raw_credit_scores          | score_date              | 1-1 Mapping         |
| Bronze       | bronze_credit_scores       | load_timestamp          | Raw          | raw_credit_scores          | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_credit_scores       | update_timestamp        | Raw          | raw_credit_scores          | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_credit_scores       | source_system           | Raw          | raw_credit_scores          | source_system           | 1-1 Mapping         |
| Bronze       | bronze_document_submissions| document_id             | Raw          | raw_document_submissions   | document_id             | 1-1 Mapping         |
| Bronze       | bronze_document_submissions| application_id          | Raw          | raw_document_submissions   | application_id          | 1-1 Mapping         |
| Bronze       | bronze_document_submissions| document_type           | Raw          | raw_document_submissions   | document_type           | 1-1 Mapping         |
| Bronze       | bronze_document_submissions| upload_date             | Raw          | raw_document_submissions   | upload_date             | 1-1 Mapping         |
| Bronze       | bronze_document_submissions| verified_flag           | Raw          | raw_document_submissions   | verified_flag           | 1-1 Mapping         |
| Bronze       | bronze_document_submissions| load_timestamp          | Raw          | raw_document_submissions   | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_document_submissions| update_timestamp        | Raw          | raw_document_submissions   | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_document_submissions| source_system           | Raw          | raw_document_submissions   | source_system           | 1-1 Mapping         |
| Bronze       | bronze_verification_results| verification_id         | Raw          | raw_verification_results   | verification_id         | 1-1 Mapping         |
| Bronze       | bronze_verification_results| application_id          | Raw          | raw_verification_results   | application_id          | 1-1 Mapping         |
| Bronze       | bronze_verification_results| verification_type       | Raw          | raw_verification_results   | verification_type       | 1-1 Mapping         |
| Bronze       | bronze_verification_results| result                  | Raw          | raw_verification_results   | result                  | 1-1 Mapping         |
| Bronze       | bronze_verification_results| verified_on             | Raw          | raw_verification_results   | verified_on             | 1-1 Mapping         |
| Bronze       | bronze_verification_results| load_timestamp          | Raw          | raw_verification_results   | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_verification_results| update_timestamp        | Raw          | raw_verification_results   | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_verification_results| source_system           | Raw          | raw_verification_results   | source_system           | 1-1 Mapping         |
| Bronze       | bronze_underwriting_decisions| decision_id           | Raw          | raw_underwriting_decisions | decision_id             | 1-1 Mapping         |
| Bronze       | bronze_underwriting_decisions| application_id        | Raw          | raw_underwriting_decisions | application_id          | 1-1 Mapping         |
| Bronze       | bronze_underwriting_decisions| decision              | Raw          | raw_underwriting_decisions | decision                | 1-1 Mapping         |
| Bronze       | bronze_underwriting_decisions| decision_reason       | Raw          | raw_underwriting_decisions | decision_reason         | 1-1 Mapping         |
| Bronze       | bronze_underwriting_decisions| decision_date         | Raw          | raw_underwriting_decisions | decision_date           | 1-1 Mapping         |
| Bronze       | bronze_underwriting_decisions| load_timestamp        | Raw          | raw_underwriting_decisions | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_underwriting_decisions| update_timestamp      | Raw          | raw_underwriting_decisions | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_underwriting_decisions| source_system         | Raw          | raw_underwriting_decisions | source_system           | 1-1 Mapping         |
| Bronze       | bronze_campaigns            | campaign_id           | Raw          | raw_campaigns              | campaign_id             | 1-1 Mapping         |
| Bronze       | bronze_campaigns            | campaign_name         | Raw          | raw_campaigns              | campaign_name           | 1-1 Mapping         |
| Bronze       | bronze_campaigns            | channel               | Raw          | raw_campaigns              | channel                 | 1-1 Mapping         |
| Bronze       | bronze_campaigns            | start_date            | Raw          | raw_campaigns              | start_date              | 1-1 Mapping         |
| Bronze       | bronze_campaigns            | end_date              | Raw          | raw_campaigns              | end_date                | 1-1 Mapping         |
| Bronze       | bronze_campaigns            | load_timestamp        | Raw          | raw_campaigns              | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_campaigns            | update_timestamp      | Raw          | raw_campaigns              | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_campaigns            | source_system         | Raw          | raw_campaigns              | source_system           | 1-1 Mapping         |
| Bronze       | bronze_application_campaigns| app_campaign_id       | Raw          | raw_application_campaigns  | app_campaign_id         | 1-1 Mapping         |
| Bronze       | bronze_application_campaigns| application_id        | Raw          | raw_application_campaigns  | application_id          | 1-1 Mapping         |
| Bronze       | bronze_application_campaigns| campaign_id           | Raw          | raw_application_campaigns  | campaign_id             | 1-1 Mapping         |
| Bronze       | bronze_application_campaigns| load_timestamp        | Raw          | raw_application_campaigns  | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_application_campaigns| update_timestamp      | Raw          | raw_application_campaigns  | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_application_campaigns| source_system         | Raw          | raw_application_campaigns  | source_system           | 1-1 Mapping         |
| Bronze       | bronze_activations          | activation_id         | Raw          | raw_activations             | activation_id           | 1-1 Mapping         |
| Bronze       | bronze_activations          | application_id        | Raw          | raw_activations             | application_id          | 1-1 Mapping         |
| Bronze       | bronze_activations          | activation_date       | Raw          | raw_activations             | activation_date         | 1-1 Mapping         |
| Bronze       | bronze_activations          | first_transaction_amount | Raw        | raw_activations             | first_transaction_amount | 1-1 Mapping         |
| Bronze       | bronze_activations          | load_timestamp        | Raw          | raw_activations             | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_activations          | update_timestamp      | Raw          | raw_activations             | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_activations          | source_system         | Raw          | raw_activations             | source_system           | 1-1 Mapping         |
| Bronze       | bronze_fraud_checks         | fraud_check_id        | Raw          | raw_fraud_checks            | fraud_check_id          | 1-1 Mapping         |
| Bronze       | bronze_fraud_checks         | application_id        | Raw          | raw_fraud_checks            | application_id          | 1-1 Mapping         |
| Bronze       | bronze_fraud_checks         | check_type            | Raw          | raw_fraud_checks            | check_type              | 1-1 Mapping         |
| Bronze       | bronze_fraud_checks         | check_result          | Raw          | raw_fraud_checks            | check_result            | 1-1 Mapping         |
| Bronze       | bronze_fraud_checks         | check_date            | Raw          | raw_fraud_checks            | check_date              | 1-1 Mapping         |
| Bronze       | bronze_fraud_checks         | load_timestamp        | Raw          | raw_fraud_checks            | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_fraud_checks         | update_timestamp      | Raw          | raw_fraud_checks            | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_fraud_checks         | source_system         | Raw          | raw_fraud_checks            | source_system           | 1-1 Mapping         |
| Bronze       | bronze_offers               | offer_id              | Raw          | raw_offers                  | offer_id                | 1-1 Mapping         |
| Bronze       | bronze_offers               | card_product_id       | Raw          | raw_offers                  | card_product_id         | 1-1 Mapping         |
| Bronze       | bronze_offers               | offer_detail          | Raw          | raw_offers                  | offer_detail            | 1-1 Mapping         |
| Bronze       | bronze_offers               | valid_from            | Raw          | raw_offers                  | valid_from              | 1-1 Mapping         |
| Bronze       | bronze_offers               | valid_to              | Raw          | raw_offers                  | valid_to                | 1-1 Mapping         |
| Bronze       | bronze_offers               | load_timestamp        | Raw          | raw_offers                  | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_offers               | update_timestamp      | Raw          | raw_offers                  | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_offers               | source_system         | Raw          | raw_offers                  | source_system           | 1-1 Mapping         |
| Bronze       | bronze_offer_performance    | offer_analytics_id    | Raw          | raw_offer_performance       | offer_analytics_id      | 1-1 Mapping         |
| Bronze       | bronze_offer_performance    | offer_id              | Raw          | raw_offer_performance       | offer_id                | 1-1 Mapping         |
| Bronze       | bronze_offer_performance    | applications_count    | Raw          | raw_offer_performance       | applications_count      | 1-1 Mapping         |
| Bronze       | bronze_offer_performance    | activations_count     | Raw          | raw_offer_performance       | activations_count       | 1-1 Mapping         |
| Bronze       | bronze_offer_performance    | load_timestamp        | Raw          | raw_offer_performance       | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_offer_performance    | update_timestamp      | Raw          | raw_offer_performance       | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_offer_performance    | source_system         | Raw          | raw_offer_performance       | source_system           | 1-1 Mapping         |
| Bronze       | bronze_address_history      | address_id            | Raw          | raw_address_history         | address_id              | 1-1 Mapping         |
| Bronze       | bronze_address_history      | applicant_id          | Raw          | raw_address_history         | applicant_id            | 1-1 Mapping         |
| Bronze       | bronze_address_history      | address_type          | Raw          | raw_address_history         | address_type            | 1-1 Mapping         |
| Bronze       | bronze_address_history      | street                | Raw          | raw_address_history         | street                  | 1-1 Mapping         |
| Bronze       | bronze_address_history      | city                  | Raw          | raw_address_history         | city                    | 1-1 Mapping         |
| Bronze       | bronze_address_history      | state                 | Raw          | raw_address_history         | state                   | 1-1 Mapping         |
| Bronze       | bronze_address_history      | zip                   | Raw          | raw_address_history         | zip                     | 1-1 Mapping         |
| Bronze       | bronze_address_history      | load_timestamp        | Raw          | raw_address_history         | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_address_history      | update_timestamp      | Raw          | raw_address_history         | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_address_history      | source_system         | Raw          | raw_address_history         | source_system           | 1-1 Mapping         |
| Bronze       | bronze_employment_info      | employment_id         | Raw          | raw_employment_info         | employment_id           | 1-1 Mapping         |
| Bronze       | bronze_employment_info      | applicant_id          | Raw          | raw_employment_info         | applicant_id            | 1-1 Mapping         |
| Bronze       | bronze_employment_info      | employer_name         | Raw          | raw_employment_info         | employer_name           | 1-1 Mapping         |
| Bronze       | bronze_employment_info      | job_title             | Raw          | raw_employment_info         | job_title               | 1-1 Mapping         |
| Bronze       | bronze_employment_info      | income                | Raw          | raw_employment_info         | income                  | 1-1 Mapping         |
| Bronze       | bronze_employment_info      | employment_type       | Raw          | raw_employment_info         | employment_type         | 1-1 Mapping         |
| Bronze       | bronze_employment_info      | load_timestamp        | Raw          | raw_employment_info         | load_timestamp          | 1-1 Mapping         |
| Bronze       | bronze_employment_info      | update_timestamp      | Raw          | raw_employment_info         | update_timestamp        | 1-1 Mapping         |
| Bronze       | bronze_employment_info      | source_system         | Raw          | raw_employment_info         | source_system           | 1-1 Mapping         |
