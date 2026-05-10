-- Table: Applicants
CREATE TABLE credit_card.Applicants (
  applicant_id INT PRIMARY KEY NOT NULL,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  phone_number VARCHAR(15) NOT NULL,
  dob DATE NOT NULL,
  ssn VARCHAR(11) UNIQUE,
  channel VARCHAR(50)
);

-- Table: Applications
CREATE TABLE credit_card.Applications (
  application_id INT PRIMARY KEY NOT NULL,
  applicant_id INT NOT NULL,
  card_product_id INT NOT NULL,
  application_date DATE NOT NULL,
  status VARCHAR(30) NOT NULL,
  approval_date DATE,
  rejection_reason VARCHAR(255),
  FOREIGN KEY (applicant_id) REFERENCES credit_card.Applicants(applicant_id),
  FOREIGN KEY (card_product_id) REFERENCES credit_card.Card_Products(card_product_id)
);

-- Table: Card_Products
CREATE TABLE credit_card.Card_Products (
  card_product_id INT PRIMARY KEY NOT NULL,
  card_name VARCHAR(100) NOT NULL,
  category VARCHAR(50),
  interest_rate FLOAT CHECK (interest_rate >= 0),
  annual_fee FLOAT CHECK (annual_fee >= 0)
);

-- Table: Credit_Scores
CREATE TABLE credit_card.Credit_Scores (
  credit_score_id INT PRIMARY KEY NOT NULL,
  applicant_id INT NOT NULL,
  score INT CHECK (score BETWEEN 300 AND 900),
  score_date DATE NOT NULL,
  FOREIGN KEY (applicant_id) REFERENCES credit_card.Applicants(applicant_id)
);

-- Table: Document_Submissions
CREATE TABLE credit_card.Document_Submissions (
  document_id INT PRIMARY KEY NOT NULL,
  application_id INT NOT NULL,
  document_type VARCHAR(50),
  upload_date DATE NOT NULL,
  verified_flag BOOLEAN,
  FOREIGN KEY (application_id) REFERENCES credit_card.Applications(application_id)
);

-- Table: Verification_Results
CREATE TABLE credit_card.Verification_Results (
  verification_id INT PRIMARY KEY NOT NULL,
  application_id INT NOT NULL,
  verification_type VARCHAR(50),
  result VARCHAR(30),
  verified_on DATE,
  FOREIGN KEY (application_id) REFERENCES credit_card.Applications(application_id)
);

-- Table: Underwriting_Decisions
CREATE TABLE credit_card.Underwriting_Decisions (
  decision_id INT PRIMARY KEY NOT NULL,
  application_id INT NOT NULL,
  decision VARCHAR(30),
  decision_reason VARCHAR(255),
  decision_date DATE,
  FOREIGN KEY (application_id) REFERENCES credit_card.Applications(application_id)
);

-- Table: Campaigns
CREATE TABLE credit_card.Campaigns (
  campaign_id INT PRIMARY KEY NOT NULL,
  campaign_name VARCHAR(100) NOT NULL,
  channel VARCHAR(50),
  start_date DATE NOT NULL,
  end_date DATE NOT NULL
);

-- Table: Application_Campaigns
CREATE TABLE credit_card.Application_Campaigns (
  app_campaign_id INT PRIMARY KEY NOT NULL,
  application_id INT NOT NULL,
  campaign_id INT NOT NULL,
  FOREIGN KEY (application_id) REFERENCES credit_card.Applications(application_id),
  FOREIGN KEY (campaign_id) REFERENCES credit_card.Campaigns(campaign_id)
);

-- Table: Activations
CREATE TABLE credit_card.Activations (
  activation_id INT PRIMARY KEY NOT NULL,
  application_id INT NOT NULL,
  activation_date DATE,
  first_transaction_amount FLOAT CHECK (first_transaction_amount >= 0),
  FOREIGN KEY (application_id) REFERENCES credit_card.Applications(application_id)
);

-- Table: Fraud_Checks
CREATE TABLE credit_card.Fraud_Checks (
  fraud_check_id INT PRIMARY KEY NOT NULL,
  application_id INT NOT NULL,
  check_type VARCHAR(50),
  check_result VARCHAR(30),
  check_date DATE,
  FOREIGN KEY (application_id) REFERENCES credit_card.Applications(application_id)
);

-- Table: Offers
CREATE TABLE credit_card.Offers (
  offer_id INT PRIMARY KEY NOT NULL,
  card_product_id INT NOT NULL,
  offer_detail VARCHAR(255),
  valid_from DATE,
  valid_to DATE,
  FOREIGN KEY (card_product_id) REFERENCES credit_card.Card_Products(card_product_id)
);

-- Table: Offer_Performance
CREATE TABLE credit_card.Offer_Performance (
  offer_analytics_id INT PRIMARY KEY NOT NULL,
  offer_id INT NOT NULL,
  applications_count INT CHECK (applications_count >= 0),
  activations_count INT CHECK (activations_count >= 0),
  FOREIGN KEY (offer_id) REFERENCES credit_card.Offers(offer_id)
);

-- Table: Address_History
CREATE TABLE credit_card.Address_History (
  address_id INT PRIMARY KEY NOT NULL,
  applicant_id INT NOT NULL,
  address_type VARCHAR(50),
  street VARCHAR(100),
  city VARCHAR(50),
  state VARCHAR(50),
  zip VARCHAR(10),
  FOREIGN KEY (applicant_id) REFERENCES credit_card.Applicants(applicant_id)
);

-- Table: Employment_Info
CREATE TABLE credit_card.Employment_Info (
  employment_id INT PRIMARY KEY NOT NULL,
  applicant_id INT NOT NULL,
  employer_name VARCHAR(100),
  job_title VARCHAR(100),
  income FLOAT CHECK (income >= 0),
  employment_type VARCHAR(50),
  FOREIGN KEY (applicant_id) REFERENCES credit_card.Applicants(applicant_id)
);
