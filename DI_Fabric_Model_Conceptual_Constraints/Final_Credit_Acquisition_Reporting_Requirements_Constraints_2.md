____________________________________________
## *Author*: AAVA
## *Created on*: 2024-06-12
## *Description*: Model data constraints and business rules for Final Credit Acquisition Reporting Requirements
## *Version*: 2
## *Updated on*: 2024-06-12
## *Changes*: Incorporated additional constraints and business rules from DDL and requirements; clarified mandatory fields, uniqueness, dependencies, and referential integrity.
## *Reason*: Update to ensure constraints and business rules reflect expanded data model and business requirements.
____________________________________________

## 1. Data Expectations

### 1.1 Data Completeness
1. All applications must have application timestamps, approval dates, and activation dates recorded.
2. Demographic information (geography, age group, income level, employment type) should be available for each applicant.
3. Campaign and acquisition channel details must be present for every application.
4. Fraud check results should be available for all applications.
5. Credit score and employment info must be present for risk segmentation.
6. Offer details must be linked to card products and transactions where applicable.

### 1.2 Data Accuracy
1. Approval and activation dates must accurately reflect the actual process events.
2. Credit scores must be sourced from validated credit bureaus.
3. Transaction amounts and dates must match actual cardholder activity.
4. Campaign costs must be accurately attributed to each campaign.
5. Employment income must be validated against supporting documents.

### 1.3 Data Format
1. Dates must follow a consistent format (e.g., YYYY-MM-DD).
2. Income levels should be categorized into predefined ranges.
3. Credit scores must be numeric and within valid ranges.
4. Application outcomes must use standardized status values (approved, declined, activated).
5. Offer details must be text and within defined length constraints.

### 1.4 Data Consistency
1. Applicant demographic data must be consistent across all reports.
2. Application outcomes should align with activation and transaction records.
3. Campaign and channel names must be consistent across applications.
4. Fraud check types and results must be standardized.
5. Employment info and credit score must be consistent for each applicant.

## 2. Constraints

### 2.1 Mandatory Fields
1. Application Timestamp: Required for every application.
2. Approval Date: Required for approved applications.
3. Activation Date: Required for activated cards.
4. Applicant Demographics: Geography, age group, income level, employment type must be provided.
5. Credit Score: Required for risk segmentation.
6. Offer Detail: Required for promotional offers linked to transactions.
7. Employment Info: Required for applicants.

### 2.2 Uniqueness Requirements
1. Application Timestamp + Applicant: Must be unique for each application.
2. Campaign Name + Start Date: Must be unique for each campaign instance.
3. Offer Detail + Valid From: Must be unique for each offer.

### 2.3 Data Type Limitations
1. Credit Score: Numeric, within valid credit score range.
2. Transaction Amount: Numeric, positive values only.
3. Marketing Cost: Numeric, positive values only.
4. Income: Numeric, positive values only.
5. Offer Detail: Text, max 255 characters.

### 2.4 Dependencies
1. Activation Date depends on Approval Date; only approved applications can be activated.
2. First Transaction Date depends on Activation Date; only activated cards can have transactions.
3. Fraud Check must be performed before approval.
4. Employment Info must be linked to applicant before application submission.
5. Offer must be linked to card product before activation.

### 2.5 Referential Integrity
1. Application must reference valid Card Product, Acquisition Channel, Campaign, Demographic Segment, and Applicant.
2. Transaction must reference valid Application and Offer.
3. Employment Info must reference valid Applicant.
4. Credit Score must reference valid Applicant.
5. Verification Result must reference valid Application.
6. Underwriting Decision must reference valid Application.

## 3. Business Rules

### 3.1 Data Processing Rules
1. Applications must be processed in chronological order based on timestamps.
2. Only applications with complete demographic, credit score, and employment info are considered for risk segmentation.
3. Offers must be validated for eligibility before linking to transactions.

### 3.2 Reporting Logic Rules
1. Approval Rate is calculated as (Approved ÷ Total Applications) × 100.
2. Activation Rate is calculated as (Activated ÷ Approved) × 100.
3. Drop-off Rate is calculated as (Applications – Activations) ÷ Applications × 100.
4. Cost per Acquisition is calculated as Campaign Cost ÷ Activations.
5. Campaign ROI is calculated as (Revenue from Activations – Campaign Cost) ÷ Campaign Cost.
6. Conversion Rate is calculated as Activations ÷ Applications × 100.
7. Decline Rate is calculated as Rejections ÷ Total Applications × 100.
8. Fraud Detection Rate is calculated as Confirmed Fraud ÷ Total Applications × 100.
9. False Positive Rate is calculated as Cleared Fraud Flags ÷ Total Fraud Flags × 100.
10. Escalation Rate is calculated as Manually Reviewed Applications ÷ Total Flags × 100.
11. Time to First Transaction is calculated as First Transaction Date – Activation Date.
12. Inactive Rate is calculated as (No Transactions within 30 Days ÷ Activated Cards) × 100.
13. Average First Transaction Amount is calculated as Total First Transaction Value ÷ Users Who Transacted.

### 3.3 Transformation Guidelines
1. Applicant demographic attributes should be mapped to standardized segment categories.
2. Campaign costs and revenues should be aggregated by campaign type and quarter for ROI analysis.
3. Credit score values should be grouped into risk tiers (<580, 580–699, ≥700) for segmentation.
4. Transaction data should be anonymized for downstream reporting where required.
5. Employment info should be categorized for segment analysis.
6. Offer performance should be aggregated by product and quarter.