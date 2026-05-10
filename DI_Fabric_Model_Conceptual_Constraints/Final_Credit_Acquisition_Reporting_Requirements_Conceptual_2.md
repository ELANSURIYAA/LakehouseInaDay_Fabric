_____________________________________________
## *Author*: AAVA
## *Created on*: 2024-06-12
## *Description*: Conceptual data model for Final Credit Acquisition Reporting Requirements
## *Version*: 2
## *Updated on*: 2024-06-12
## *Changes*: Enhanced entity and attribute coverage using DDL and requirements; clarified relationships and KPIs; added business context from DDL.
## *Reason*: Update to align conceptual model with expanded business requirements and DDL structure.
_____________________________________________

## 1. Domain Overview
The business domain is Credit Card Acquisition, covering the end-to-end process from applicant onboarding, application processing, campaign performance, credit risk segmentation, fraud screening, and first transaction behavior. The model now incorporates detailed business entities and relationships as reflected in the DDL and reporting requirements, supporting marketing, product, risk, operations, fraud management, and customer engagement teams.

## 2. List of Entity Names with Descriptions
1. **Applicant**: Individual applying for a credit card.
2. **Application**: Record of a credit card application process.
3. **Card Product**: The specific credit card product offered.
4. **Acquisition Channel**: The channel through which the application was submitted (e.g., online, branch, campaign).
5. **Campaign**: Marketing initiative aimed at acquiring new customers.
6. **Fraud Check**: Screening process to detect fraudulent applications.
7. **Transaction**: First transaction activity post card activation.
8. **Demographic Segment**: Grouping of applicants by geography, age, income, etc.
9. **Credit Score**: Creditworthiness indicator for applicants.
10. **Employment Info**: Employment and income details for applicants.
11. **Offer**: Promotional offer linked to card product and activation.
12. **Verification Result**: Outcome of document and application verification.
13. **Underwriting Decision**: Decision and reasoning for application approval/decline.

## 3. List of Attributes for Each Entity
### Applicant
1. **Full Name**: Applicant's legal name.
2. **Email**: Contact email address.
3. **Phone Number**: Contact phone number.
4. **Date of Birth**: Applicant's birth date.
5. **Channel**: Acquisition channel for applicant.
6. **Geography**: Location of applicant.
7. **Age Group**: Age category of applicant.
8. **Income Level**: Income range of applicant.
9. **Employment Type**: Employment status of applicant.

### Application
1. **Application Timestamp**: Date and time of application submission.
2. **Approval Date**: Date application was approved.
3. **Activation Date**: Date card was activated.
4. **Application Outcome**: Status of application (approved, declined, activated).
5. **Rejection Reason**: Reason for application rejection.

### Card Product
1. **Product Name**: Name of credit card product.
2. **Product Type**: Category/type of card.
3. **Interest Rate**: Interest rate for product.
4. **Annual Fee**: Annual fee for product.

### Acquisition Channel
1. **Channel Name**: Name of acquisition channel.
2. **Channel Type**: Type of channel (digital, branch, campaign).

### Campaign
1. **Campaign Name**: Name of campaign.
2. **Campaign Type**: Type of campaign.
3. **Start Date**: Campaign start date.
4. **End Date**: Campaign end date.
5. **Marketing Cost**: Cost incurred for campaign.

### Fraud Check
1. **Fraud Check Type**: Type of fraud check performed.
2. **Screening Result**: Outcome of fraud check.
3. **Check Execution Date**: Date fraud check was executed.

### Transaction
1. **Activation Date**: Date card was activated.
2. **First Transaction Date**: Date of first transaction.
3. **Transaction Amount**: Value of first transaction.
4. **Promotional Offer**: Offer linked to transaction.

### Demographic Segment
1. **Geography**: Applicant location.
2. **Age Group**: Applicant age category.
3. **Income Level**: Applicant income range.

### Credit Score
1. **Score**: Numeric credit score value.
2. **Score Date**: Date score was assessed.

### Employment Info
1. **Employer Name**: Name of employer.
2. **Job Title**: Applicant's job title.
3. **Income**: Applicant's income.
4. **Employment Type**: Type of employment.

### Offer
1. **Offer Detail**: Description of promotional offer.
2. **Valid From**: Offer start date.
3. **Valid To**: Offer end date.

### Verification Result
1. **Verification Type**: Type of verification performed.
2. **Result**: Outcome of verification.
3. **Verified On**: Date verification completed.

### Underwriting Decision
1. **Decision**: Approval or decline decision.
2. **Decision Reason**: Reason for decision.
3. **Decision Date**: Date of decision.

## 4. KPI List
1. **Approval Rate**: Percentage of applications approved.
2. **Activation Rate**: Percentage of approved applications activated.
3. **Average Time to Approval**: Average duration from application to approval.
4. **Drop-off Rate**: Percentage of applicants not progressing through funnel stages.
5. **Cost per Acquisition**: Marketing cost per activated card.
6. **Campaign ROI**: Return on investment for campaigns.
7. **Conversion Rate**: Percentage of applications resulting in activations.
8. **Average Credit Score**: Mean credit score of applicants.
9. **Decline Rate**: Percentage of applications declined.
10. **Fraud Detection Rate**: Percentage of applications flagged as fraud.
11. **False Positive Rate**: Percentage of cleared fraud flags.
12. **Escalation Rate**: Percentage of applications manually reviewed for fraud.
13. **Time to First Transaction**: Time from activation to first transaction.
14. **Inactive Rate**: Percentage of activated cards with no transactions in first 30 days.
15. **Average First Transaction Amount**: Mean value of first transaction.

## 5. Conceptual Data Model Diagram
| Source Entity      | Relationship Key Field     | Target Entity      | Relationship Type |
|-------------------|---------------------------|--------------------|-------------------|
| Applicant         | Application Timestamp      | Application        | One-to-Many       |
| Applicant         | applicant_id              | Employment Info    | One-to-One        |
| Applicant         | applicant_id              | Credit Score       | One-to-Many       |
| Applicant         | applicant_id              | Address History    | One-to-Many       |
| Application       | Card Product              | Card Product       | Many-to-One       |
| Application       | Acquisition Channel       | Acquisition Channel| Many-to-One       |
| Application       | Campaign                  | Campaign           | Many-to-One       |
| Application       | Fraud Check               | Fraud Check        | One-to-Many       |
| Application       | Demographic Segment       | Demographic Segment| Many-to-One       |
| Application       | Activation Date           | Transaction        | One-to-One        |
| Application       | application_id            | Verification Result| One-to-Many       |
| Application       | application_id            | Underwriting Decision| One-to-One      |
| Transaction       | Promotional Offer         | Offer              | Many-to-One       |
| Offer             | card_product_id           | Card Product       | Many-to-One       |

## 6. Common Data Elements in Report Requirements
1. **Application Timestamp**
2. **Approval Date**
3. **Activation Date**
4. **Acquisition Channel**
5. **Applicant Demographics (Geography, Age, Income)**
6. **Campaign Type**
7. **Credit Score**
8. **Application Outcome**
9. **Fraud Check Type**
10. **Transaction Amount**
11. **Employment Type**
12. **Offer Detail**
