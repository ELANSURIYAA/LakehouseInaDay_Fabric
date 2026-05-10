-- Card_Products (these products are referenced throughout)
INSERT INTO credit_card.Card_Products VALUES (1, 'Platinum Cashback Card', 'Cashback', 18.5, 2500);
INSERT INTO credit_card.Card_Products VALUES (2, 'Elite Travel Card', 'Travel', 21.0, 3500);
INSERT INTO credit_card.Card_Products VALUES (3, 'Fuel Saver Card', 'Fuel', 15.9, 999);
INSERT INTO credit_card.Card_Products VALUES (4, 'Premium Lifestyle Card', 'Premium', 24.0, 5999);
INSERT INTO credit_card.Card_Products VALUES (5, 'Everyday Value Card', 'Cashback', 17.0, 0);

-- Offers
INSERT INTO credit_card.Offers VALUES (1, 1, '5% Cashback on Groceries', '2025-07-01', '2025-12-31');
INSERT INTO credit_card.Offers VALUES (2, 2, 'Free Lounge Access', '2025-07-01', '2025-12-31');
INSERT INTO credit_card.Offers VALUES (3, 3, '1% Fuel Surcharge Waiver', '2025-07-01', '2025-12-31');
INSERT INTO credit_card.Offers VALUES (4, 4, 'Welcome Gift Voucher', '2025-07-01', '2025-09-30');
INSERT INTO credit_card.Offers VALUES (5, 5, '0% Annual Fee for 1st Year', '2025-07-01', '2025-09-30');

-- Applicants (IDs 1-25)
INSERT INTO credit_card.Applicants VALUES (1,  'Alice Johnson',  'alice.johnson@example.com', '555-0001', '1990-08-15', '912-34-1001', 'Online');
INSERT INTO credit_card.Applicants VALUES (2,  'Brian Smith',    'brian.smith@example.com',   '555-0002', '1986-11-20', '912-34-1002', 'Branch');
INSERT INTO credit_card.Applicants VALUES (3,  'Cynthia Patel',  'c.patel@example.com',       '555-0003', '1977-09-13', '912-34-1003', 'Mobile');
INSERT INTO credit_card.Applicants VALUES (4,  'David Lee',      'dlee@example.com',          '555-0004', '1982-05-06', '912-34-1004', 'Partner');
INSERT INTO credit_card.Applicants VALUES (5,  'Emma Brown',     'emma.brown@example.com',    '555-0005', '1995-12-30', '912-34-1005', 'Online');
INSERT INTO credit_card.Applicants VALUES (6,  'Frank Green',    'frank.green@example.com',   '555-0006', '1987-07-22', '912-34-1006', 'Branch');
INSERT INTO credit_card.Applicants VALUES (7,  'Gina Rivera',    'gina.rivera@example.com',   '555-0007', '1984-10-08', '912-34-1007', 'Online');
INSERT INTO credit_card.Applicants VALUES (8,  'Harris Singh',   'h.singh@example.com',       '555-0008', '1993-02-19', '912-34-1008', 'Mobile');
INSERT INTO credit_card.Applicants VALUES (9,  'Isabel Garcia',  'isa.garcia@example.com',    '555-0009', '1989-09-17', '912-34-1009', 'Online');
INSERT INTO credit_card.Applicants VALUES (10, 'John Wang',      'john.wang@example.com',     '555-0010', '1978-06-05', '912-34-1010', 'Branch');
INSERT INTO credit_card.Applicants VALUES (11, 'Krisha Desai',   'krisha.desai@example.com',  '555-0011', '1992-03-25', '912-34-1011', 'Mobile');
INSERT INTO credit_card.Applicants VALUES (12, 'Liam Martinez',  'liam.martinez@example.com', '555-0012', '1985-11-12', '912-34-1012', 'Partner');
INSERT INTO credit_card.Applicants VALUES (13, 'Maria Lopez',    'm.lopez@example.com',       '555-0013', '1990-10-15', '912-34-1013', 'Online');
INSERT INTO credit_card.Applicants VALUES (14, 'Nina Rossi',     'nina.rossi@example.com',    '555-0014', '1988-04-18', '912-34-1014', 'Branch');
INSERT INTO credit_card.Applicants VALUES (15, 'Oscar White',    'oscar.white@example.com',   '555-0015', '1991-01-23', '912-34-1015', 'Online');
INSERT INTO credit_card.Applicants VALUES (16, 'Priya Kumar',    'priya.kumar@example.com',   '555-0016', '1987-08-29', '912-34-1016', 'Partner');
INSERT INTO credit_card.Applicants VALUES (17, 'Quinn Silva',    'quinn.silva@example.com',   '555-0017', '1994-07-11', '912-34-1017', 'Mobile');
INSERT INTO credit_card.Applicants VALUES (18, 'Rajesh Menon',   'rajesh.menon@example.com',  '555-0018', '1983-02-03', '912-34-1018', 'Online');
INSERT INTO credit_card.Applicants VALUES (19, 'Sara King',      'sara.king@example.com',     '555-0019', '1990-03-19', '912-34-1019', 'Branch');
INSERT INTO credit_card.Applicants VALUES (20, 'Tomya Ulrich',   't.ulrich@example.com',      '555-0020', '1976-05-14', '912-34-1020', 'Mobile');
INSERT INTO credit_card.Applicants VALUES (21, 'Uma Das',        'uma.das@example.com',       '555-0021', '1988-12-09', '912-34-1021', 'Online');
INSERT INTO credit_card.Applicants VALUES (22, 'Vineet Malhotra','vineet.malhotra@example.com','555-0022', '1993-08-03', '912-34-1022', 'Partner');
INSERT INTO credit_card.Applicants VALUES (23, 'Will Clark',     'will.clark@example.com',    '555-0023', '1980-10-15', '912-34-1023', 'Mobile');
INSERT INTO credit_card.Applicants VALUES (24, 'Yara Abdallah',  'yara.abdallah@example.com', '555-0024', '1997-01-18', '912-34-1024', 'Branch');
INSERT INTO credit_card.Applicants VALUES (25, 'Zach Evans',     'zach.evans@example.com',    '555-0025', '1986-09-21', '912-34-1025', 'Online');

-- Credit_Scores (1 per applicant)
INSERT INTO credit_card.Credit_Scores VALUES (1, 1, 780, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (2, 2, 590, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (3, 3, 735, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (4, 4, 820, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (5, 5, 760, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (6, 6, 615, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (7, 7, 710, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (8, 8, 690, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (9, 9, 748, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (10, 10, 670, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (11, 11, 795, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (12, 12, 625, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (13, 13, 770, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (14, 14, 810, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (15, 15, 732, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (16, 16, 610, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (17, 17, 780, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (18, 18, 798, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (19, 19, 660, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (20, 20, 585, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (21, 21, 755, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (22, 22, 800, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (23, 23, 722, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (24, 24, 788, '2025-06-30');
INSERT INTO credit_card.Credit_Scores VALUES (25, 25, 630, '2025-06-30');

-- Applications (linked to both Applicants and Card_Products)
INSERT INTO credit_card.Applications VALUES (1, 1, 1,  '2025-07-01', 'Approved', '2025-07-03', NULL);
INSERT INTO credit_card.Applications VALUES (2, 2, 2,  '2025-07-02', 'Rejected', NULL, 'Low credit score');
INSERT INTO credit_card.Applications VALUES (3, 3, 4,  '2025-07-02', 'Pending', NULL, NULL);
INSERT INTO credit_card.Applications VALUES (4, 4, 3,  '2025-07-02', 'Approved', '2025-07-05', NULL);
INSERT INTO credit_card.Applications VALUES (5, 5, 2,  '2025-07-03', 'Approved', '2025-07-08', NULL);
INSERT INTO credit_card.Applications VALUES (6, 6, 5,  '2025-07-03', 'Rejected', NULL, 'Insufficient income proof');
INSERT INTO credit_card.Applications VALUES (7, 7, 1,  '2025-07-04', 'Approved', '2025-07-09', NULL);
INSERT INTO credit_card.Applications VALUES (8, 8, 2,  '2025-07-04', 'Pending', NULL, NULL);
INSERT INTO credit_card.Applications VALUES (9, 9, 3,  '2025-07-04', 'Approved', '2025-07-10', NULL);
INSERT INTO credit_card.Applications VALUES (10,10,1,  '2025-07-05', 'Pending', NULL, NULL);
INSERT INTO credit_card.Applications VALUES (11,11,5,  '2025-07-05', 'Approved', '2025-07-12', NULL);
INSERT INTO credit_card.Applications VALUES (12,12,3,  '2025-07-06', 'Rejected', NULL, 'Fail on address verification');
INSERT INTO credit_card.Applications VALUES (13,13,2,  '2025-07-06', 'Approved', '2025-07-13', NULL);
INSERT INTO credit_card.Applications VALUES (14,14,1,  '2025-07-07', 'Pending', NULL, NULL);
INSERT INTO credit_card.Applications VALUES (15,15,5,  '2025-07-07', 'Approved', '2025-07-16', NULL);
INSERT INTO credit_card.Applications VALUES (16,16,4,  '2025-07-07', 'Rejected', NULL, 'High existing debt');
INSERT INTO credit_card.Applications VALUES (17,17,3,  '2025-07-08', 'Approved', '2025-07-18', NULL);
INSERT INTO credit_card.Applications VALUES (18,18,2,  '2025-07-08', 'Approved', '2025-07-20', NULL);
INSERT INTO credit_card.Applications VALUES (19,19,1,  '2025-07-09', 'Pending', NULL, NULL);
INSERT INTO credit_card.Applications VALUES (20,20,3,  '2025-07-09', 'Rejected', NULL, 'Failure on KYC check');
INSERT INTO credit_card.Applications VALUES (21,21,5,  '2025-07-09', 'Approved', '2025-07-20', NULL);
INSERT INTO credit_card.Applications VALUES (22,22,1,  '2025-07-10', 'Pending', NULL, NULL);
INSERT INTO credit_card.Applications VALUES (23,23,2,  '2025-07-10', 'Approved', '2025-07-22', NULL);
INSERT INTO credit_card.Applications VALUES (24,24,4,  '2025-07-11', 'Approved', '2025-07-25', NULL);
INSERT INTO credit_card.Applications VALUES (25,25,5,  '2025-07-12', 'Rejected', NULL, 'Invalid SSN');

-- Address_History (two per applicant: current & permanent)
INSERT INTO credit_card.Address_History VALUES (1, 1, 'Current',   '123 Elm St',  'New York',   'NY', '10001');
INSERT INTO credit_card.Address_History VALUES (2, 1, 'Permanent', '900 Oak Ave', 'Brooklyn',   'NY', '11201');
INSERT INTO credit_card.Address_History VALUES (3, 2, 'Current',   '5 Lakeview',  'Dallas',     'TX', '75201');
INSERT INTO credit_card.Address_History VALUES (4, 2, 'Permanent', '98 Central',  'Houston',    'TX', '77002');
-- ...Continue up to id 50 for all applicants

-- Employment_Info (one per applicant)
INSERT INTO credit_card.Employment_Info VALUES (1,  1,  'Acme Corp',   'Data Analyst',     9800,  'Salaried');
INSERT INTO credit_card.Employment_Info VALUES (2,  2,  'Smith Retail','Branch Manager',   7500,  'Salaried');
INSERT INTO credit_card.Employment_Info VALUES (3,  3,  'Patel Stores','Owner',           16500, 'Self-employed');
INSERT INTO credit_card.Employment_Info VALUES (4,  4,  'Tech Advance','Engineer',         12000, 'Salaried');
-- ...Continue up to id 25

-- Document_Submissions (two per application, types rotated)
INSERT INTO credit_card.Document_Submissions VALUES (101, 1, 'ID',           '2025-07-01', TRUE);
INSERT INTO credit_card.Document_Submissions VALUES (102, 1, 'Income Proof',  '2025-07-01', TRUE);
INSERT INTO credit_card.Document_Submissions VALUES (103, 2, 'ID',          '2025-07-02', TRUE);
INSERT INTO credit_card.Document_Submissions VALUES (104, 2, 'Address Proof','2025-07-02', FALSE);
-- ...Continue for all applications, IDs 101–150

-- Verification_Results (one per application)
INSERT INTO credit_card.Verification_Results VALUES (1, 1, 'Identity', 'Pass', '2025-07-02');
INSERT INTO credit_card.Verification_Results VALUES (2, 2, 'Income',   'Fail', '2025-07-03');
INSERT INTO credit_card.Verification_Results VALUES (3, 3, 'Address',  'Pass', '2025-07-04');
-- ...Continue for all application IDs

-- Underwriting_Decisions (one per application)
INSERT INTO credit_card.Underwriting_Decisions VALUES (1, 1, 'Approved', NULL, '2025-07-03');
INSERT INTO credit_card.Underwriting_Decisions VALUES (2, 2, 'Rejected', 'Low credit score', '2025-07-04');
-- ...Continue for all applications

-- Campaigns (5, rotated)
INSERT INTO credit_card.Campaigns VALUES (1, 'Summer Travel Bonanza', 'Email', '2025-06-01', '2025-08-31');
INSERT INTO credit_card.Campaigns VALUES (2, 'Cashback Carnival',     'SMS',   '2025-07-01', '2025-08-31');
INSERT INTO credit_card.Campaigns VALUES (3, 'Petrol Saver Week',     'Social','2025-07-10', '2025-07-31');
INSERT INTO credit_card.Campaigns VALUES (4, 'Premium Welcome',       'Branch','2025-06-15', '2025-09-15');
INSERT INTO credit_card.Campaigns VALUES (5, 'Everyday Offers',       'Email', '2025-07-01', '2025-09-30');

-- Application_Campaigns (one per application, cycling campaign_ids)
INSERT INTO credit_card.Application_Campaigns VALUES (1, 1, 2);
INSERT INTO credit_card.Application_Campaigns VALUES (2, 2, 3);
INSERT INTO credit_card.Application_Campaigns VALUES (3, 3, 1);
-- ...Continue for all applications up to 25

-- Activations (approved applications only, activate 1-15)
INSERT INTO credit_card.Activations VALUES (1, 1, '2025-07-04', 1200.0);
INSERT INTO credit_card.Activations VALUES (2, 4, '2025-07-05', 950.5);
INSERT INTO credit_card.Activations VALUES (3, 5, '2025-07-09', 2500.0);
-- ...Continue for each application with status='Approved'

-- Fraud_Checks (one per application)
INSERT INTO credit_card.Fraud_Checks VALUES (1, 1, 'GeoIP',  'Pass',   '2025-07-01');
INSERT INTO credit_card.Fraud_Checks VALUES (2, 2, 'Velocity','Review', '2025-07-02');
INSERT INTO credit_card.Fraud_Checks VALUES (3, 3, 'Identity','Pass',   '2025-07-03');
-- ...Continue for all application IDs

-- Offer_Performance (one per offer)
INSERT INTO credit_card.Offer_Performance VALUES (1, 1, 120, 48);
INSERT INTO credit_card.Offer_Performance VALUES (2, 2, 95,  32);
INSERT INTO credit_card.Offer_Performance VALUES (3, 3, 110, 59);
INSERT INTO credit_card.Offer_Performance VALUES (4, 4, 75,  23);
INSERT INTO credit_card.Offer_Performance VALUES (5, 5, 99,  44);

