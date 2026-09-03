# Healthcare Data Analytics – Project

---

##  Dashboard Visual Previews

### 1. Executive Healthcare Overview
![Dashboard 1 – Healthcare Overview](./dashboard_1_overview.png)

### 2. Patient Demographics & Geographic Distribution
![Dashboard 2 – Patient Demographics](./dashboard_2_demographics.png)

### 3. Healthcare Cost & Financial Coverage
![Dashboard 3 – Healthcare Cost & Coverage](./dashboard_3_cost_coverage.png)

---

##  Project Overview

This project is an end-to-end healthcare data analytics project designed to analyze
patient demographics, healthcare encounters, medical conditions, medications,
healthcare expenses, insurance coverage, providers, organizations, and geographic
distribution.

The project follows a complete analytics workflow:

Raw Healthcare Data
        ↓
Python Data Cleaning & EDA
        ↓
SQL Analysis
        ↓
Tableau Visualization
        ↓
Business Insights & Recommendations

The objective is to transform raw healthcare records into meaningful insights that
can support operational, demographic, and financial decision-making.

---

## Business Objectives

The project aims to answer questions such as:

- How many unique patients are in the dataset?
- How many healthcare encounters occurred?
- What are the major encounter types?
- What are the most common medical conditions?
- Which medications have the highest record counts?
- What is the demographic composition of patients?
- Where are patients geographically concentrated?
- How do healthcare expenses vary across patient segments?
- How does insurance coverage vary?
- Which providers and organizations have the highest activity/revenue?
- What business areas require further investigation?

---

## Dataset

The project uses related healthcare tables including:

- Patients
- Encounters
- Conditions
- Medications
- Providers
- Organizations
- Payers

The patient data includes demographic and financial information such as gender,
race, ethnicity, marital status, healthcare expenses and healthcare coverage.

---

# Tools & Technologies

### Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

Used for:
- Data cleaning
- Data preprocessing
- Missing-value analysis
- Data validation
- Exploratory Data Analysis
- Pattern identification

### SQL
- MySQL / SQL

Used for:
- Data querying
- Filtering
- Aggregation
- Joins
- Distinct counts
- Business analysis
- Ranking and Top-N analysis

### Tableau

Used for:
- KPI dashboards
- Interactive visualizations
- Trend analysis
- Demographic analysis
- Geographic mapping
- Cost analysis
- Insurance analysis
- Business storytelling

### Excel

Used for:
- Supporting analysis
- Validation
- Reporting

---

# Key Metrics

The final analysis contains:

- 1,171 unique patients
- 53,346 unique encounters
- 5,855 providers
- 1,119 organizations

These metrics are calculated using appropriate distinct counts at the relevant
entity level.

---

# Tableau Dashboards

## Dashboard 1 – Healthcare Overview

![Dashboard 1 Overview](./dashboard_1_overview.png)

### Purpose

Provides an executive-level overview of healthcare activity.

### Main Components

- Total Patients
- Total Encounters
- Total Providers
- Total Organizations
- Patient Encounter Trends
- Encounters by Type
- Patient Distribution by Gender
- Top 10 Conditions
- Top 10 Medications

### Key Question

> What is happening across the healthcare system?

---

## Dashboard 2 – Patient Demographics

![Dashboard 2 Patient Demographics](./dashboard_2_demographics.png)

### Purpose

Analyzes the composition and geographic distribution of the patient population.

### Main Components

- Total Patients
- Patient Distribution by Gender
- Patient Distribution by Race
- Patient Distribution by Ethnicity
- Patient Distribution by Marital Status
- Geographic Map by City

### Key Question

> Who are the patients and where are they located?

---

## Dashboard 3 – Healthcare Cost & Coverage

![Dashboard 3 Healthcare Cost & Coverage](./dashboard_3_cost_coverage.png)

### Purpose

Analyzes healthcare spending and insurance coverage.

### Main Components

- Healthcare Expenses by Gender
- Healthcare Coverage by Gender
- Patient Distribution by Healthcare Coverage
- Average Healthcare Expense by Age Group
- Patient Distribution by Healthcare Expense
- Average Healthcare Expense by Gender

### Key Question

> What does healthcare cost and how is it covered?

---

# Key Business Insights

### Patient & Encounter Activity

The dataset contains 53,346 encounters across 1,171 unique patients,
showing substantially more encounter activity than unique patients.

### Gender

Female patients represent 609 patients (52.0%), while male patients represent
562 patients (48.0%).

### Race

White patients represent 965 patients (82.4%), followed by Black patients,
Asian patients, Native patients and Other categories.

### Ethnicity

Non-Hispanic patients represent 1,058 patients (90.4%), while Hispanic patients
represent 113 patients (9.6%).

### Encounter Type

Wellness encounters account for 35.82% and ambulatory encounters account for
35.50%, making them the largest encounter categories.

### Medical Conditions

Viral sinusitis is the highest-volume condition with 1,248 records.

### Medications

Hydrochlorothiazide 25 MG has the highest medication record count with
3,954 records.

### Healthcare Expenses

Total healthcare expenses are approximately $895.75M.

Average healthcare expense:

- Male: $776,616
- Female: $754,167

### Insurance Coverage

Total recorded healthcare coverage is approximately $15.14M.

Male coverage:
$8.53M

Female coverage:
$6.61M

### Hospital / Organization Revenue

VA Boston Healthcare System is the highest-revenue organization in the
Top 10 view at approximately $595K.

---

# Business Recommendations

1. Monitor wellness and ambulatory encounters because they represent the largest
   encounter segments.

2. Track high-volume respiratory conditions and medication utilization.

3. Separate total-cost analysis from average-cost analysis when comparing
   patient segments.

4. Investigate high-expense patient groups for financial and operational review.

5. Improve completeness of demographic fields before using them for detailed
   segmentation.

6. Combine geographic concentration with organization revenue and utilization
   for regional planning.

---

# Data Quality Considerations

- Some demographic fields contain unknown or incomplete values.
- Record counts and distinct-patient counts represent different analytical
  concepts.
- Age is derived/grouped from birthdate rather than being a native patient field.
- The analysis is descriptive and does not establish clinical causality.
- Financial values are dataset measures for analytical demonstration.

---

# Project Workflow

1. Data Collection & Understanding
2. Data Cleaning using Python
3. Exploratory Data Analysis using Python
4. SQL Querying & Analytical Analysis
5. Tableau Visualization
6. Dashboard Development
7. Business Insight Generation
8. Recommendations

---

# Suggested Repository Structure

Healthcare-Data-Analytics/
│
├── data/
│   ├── patients.csv
│   ├── encounters.csv
│   ├── conditions.csv
│   ├── medications.csv
│   ├── providers.csv
│   ├── organizations.csv
│   └── payers.csv
│
├── python/
│   ├── data_cleaning.py
│   └── exploratory_analysis.py
│
├── sql/
│   └── healthcare_analysis.sql
│
├── tableau/
│   └── healthcare_analytics.twbx
│
├── screenshots/
│   ├── dashboard_overview.png
│   ├── dashboard_demographics.png
│   └── dashboard_cost_coverage.png
│
├── documentation/
│   └── project_documentation.pdf
│
└── README.md

---

# Skills Demonstrated

- Python
- Pandas
- NumPy
- SQL
- MySQL
- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Tableau
- Excel
- KPI Development
- Business Analysis
- Data Storytelling
- Dashboard Design
- Analytical Thinking
