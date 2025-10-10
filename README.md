# Integration and analysis of financial data from heterogeneous sources using DuckDB 🦆

This project demonstrates a comprehensive approach to analyzing user financial behavior by combining multiple data sources, including PostgreSQL tables, Parquet/Arrow transaction files, and MongoDB card data into a single analytical platform powered by DuckDB.  

The system allows financial analysts and decision-makers to explore insights across user spending, debt, income, card usage, and geographic distribution. By centralizing heterogenous data and providing fast,  analytical capabilities, DuckDB enables efficient querying, aggregation, and visualization of large datasets without the overhead of traditional database ETL pipelines.

---

## Motivation

Financial data often resides in multiple formats and systems, in this case: transactional logs in Parquet or Arrow files, user and account information in PostgreSQL, and card data in MongoDB. Integrating these sources manually is time-consuming, error-prone, and computationally expensive.

DuckDB serves as the “universal connector,” allowing analysts to query and join heterogeneous datasets directly in Python or via visualization tools such as Metabase. Its columnar storage and vectorized execution ensure high performance even on large datasets.

---

## System overview

For a financial analyst, this system offers:

- **Unified Access to Heterogeneous Data:** Combines transactional, account, and card metadata seamlessly
- **Rapid Analysis:** DuckDB’s in-memory execution enables fast queries and iterative exploration.
- **Actionable Insights:** Evaluate user spending patterns, card utilization, debt distribution, and risk factors.
- **Decision Support:** Support portfolio management and customer engagement strategies.

---

## Query optimization

DuckDB automatically applies multiple optimizations to improve query performance:  

- **Vectorized Execution:** Processes data in batches for high CPU efficiency  
- **Late Materialization:** Reads only necessary columns  
- **Predicate Pushdown:** Applies filters early to minimize scanning  
- **Join & Aggregation Optimization:** Hash aggregation and join reordering  
- **Columnar Compression:** Reduces memory and I/O for analytical datasets  

These optimizations allow analysts to run complex queries on large Parquet, Arrow, and Postgres datasets quickly, without manual indexing or tuning.  

In this project, queries were optimized by:
- **Casting only when necessary** to avoid repeated conversions.
- **Early filtering** to reduce join and aggregation workloads.
- **Direct access to columnar data** instead of intermediate tables.
- **Simplifying CTEs and subqueries** where possible.
- Measuring **average runtime** and iteratively adjusting query structures.

<img width="997" height="597" alt="image" src="https://github.com/user-attachments/assets/e6642008-a5c1-4982-93a0-fd0fd54dd049" />

## Analyzing User Spending Behavior

This project explores and analyzes user spending patterns, credit usage, and financial behavior using multiple data sources:

- **PostgreSQL tables:** User, Account  
- **Parquet/Arrow files:** transactions_parquet, transactions_arrow  
- **MongoDB:** cards  

The analysis focuses on understanding user financial habits, assessing risk, and identifying trends in spending and credit usage.

---

### 1. User Spending & Transactions
- Summarizes individual user spending, transaction volume, and number of credit cards.
- Helps identify high-value customers and analyze spending patterns across different credit scores.

### 2. Credit Utilization Overview
- Compares average credit limits to average spending per user, segmented by number of cards held.
- Useful for detecting credit usage trends, assessing financial risk, and visualizing customer behavior.

### 3. Debt Loading vs. Annual Spending
- Aggregates spending by user income brackets and total debt.
- Enables targeted marketing, debt vs. income analysis, and customer segmentation.

### 4. Credit Utilization Funnel
- Tracks the number of users across key milestones:
  - All users
  - Users with multiple cards
  - High spenders
  - Low credit score
  - Users with compromised cards
- Supports conversion analysis, risk assessment, and targeted interventions.

### 5. High-Risk Financial profiles
- Identifies users with low credit scores and high debt to pinpoint potential financial risks.
- Can be leveraged for credit monitoring, fraud prevention, and strategic financial planning.

---

## Potential Use Cases

- **Customer Segmentation:** Group users based on spending habits, income, and credit usage.  
- **Risk Assessment:** Identify high-risk users or accounts based on debt, credit score, and transaction patterns.  
- **Financial Insights:** Gain insights into trends like average spending by income, credit usage patterns, and transaction volumes.  
- **Targeted Marketing:** Use spending and credit data to design tailored campaigns and offers.  

---

<img width="1099" height="1112" alt="image" src="https://github.com/user-attachments/assets/f87d6b69-6f49-4ae9-9f1e-59d396bc863b" />
<img width="1062" height="834" alt="image" src="https://github.com/user-attachments/assets/dd2b903c-613c-4940-99ad-fea36b16d082" />

---

## Geographical Analysis of User Data

This section focuses on understanding user behavior and financial metrics in a geographical context. By mapping transactions and financial attributes to user locations, we can gain insights into regional trends, hotspots, and disparities.

---


### 1. Transaction Density by Location (Hot-Spots)
- Measures the total number of transactions per latitude and longitude.
- Useful for identifying regions with high or low financial activity.
- Can support location-based services, regional marketing, or resource allocation.

### 2. Regional Financial Overview
- Aggregates average total debt and yearly income by region.
- Helps compare financial health across different areas.
- Enables detection of high-debt regions or areas with strong income potential.
- Supports strategic planning for credit offers, regional campaigns, and risk assessment.

---

## Potential Use Cases

- **Regional Customer Segmentation:** Group users by location to tailor offers or services.  
- **Hotspot Detection:** Identify areas with high transaction volume or significant financial activity.  
- **Regional Risk Assessment:** Detect regions with higher average debt or financial stress.  
- **Market Planning:** Align marketing, credit, or operational strategies based on regional trends.  

---

<img width="1059" height="1158" alt="image" src="https://github.com/user-attachments/assets/4ced7070-9655-48fe-b36e-937dce652295" />

---

## Analyzing User Behavior by Age Group

This section focuses on understanding financial behavior and trends across different age segments. Grouping users by age or years to retirement allows for more targeted insights into spending, debt, and overall financial health.

---

### 1. Total Spending by Current Age
- Aggregates the total spending per user grouped by their current age.
- Reveals spending patterns across different age cohorts.
- Useful for identifying which age groups are most active financially or require specific financial products.

### 2. Retirement Group Debt Analysis
- Groups users by remaining years until retirement (e.g., <10, 10–19, 20–29, 30–39, 40+).
- Calculates average, minimum, and maximum total debt, as well as the number of users per group.
- Highlights potential financial stress as users approach retirement.
- Supports planning for age-targeted credit, savings, or advisory services.

---

## Potential Use Cases

- **Age-Based Segmentation:** Tailor products, marketing, or services for specific age groups.  
- **Debt Risk Management:** Identify age groups with higher financial risk.  
- **Retirement Planning:** Detect patterns in debt and income relative to retirement horizon.  
- **Targeted Offers:** Develop financial offers and educational campaigns suited to age demographics.  

---

<img width="1061" height="879" alt="image" src="https://github.com/user-attachments/assets/5cb9eb7b-5112-4958-969c-31aee15aec41" />

---

## Card Issuance and Usage Analysis

This section focuses on understanding how issued cards are being used by customers, combining metadata from card issuance with actual transaction activity. By analyzing both the number of cards issued and active usage, organizations can better assess customer engagement and risk.

---


### 1. Transactions by Card Brand
- Aggregates the number of transactions per card brand and calculates each brand's share of total transactions.
- Reveals which card brands are most actively used by customers.
- Useful for evaluating card popularity and customer engagement by brand.

### 2. Card Issuance vs. Active Cards
- Compares the total number of cards issued per brand with the number of cards actually used in transactions.
- Highlights how many cards remain inactive and which brands have higher engagement.
- Supports optimization of card issuance strategies and monitoring brand-specific usage patterns.

---

## Potential Use Cases

- **Card Brand Strategy:** Identify which card brands are most effective at driving customer activity.  
- **Customer Engagement:** Detect underutilized cards to target re-engagement campaigns.  
- **Fraud Risk Analysis:** Monitor inactive versus active cards to spot unusual patterns.  
- **Resource Allocation:** Allocate marketing or support resources to brands with higher usage.  

---

<img width="1059" height="830" alt="image" src="https://github.com/user-attachments/assets/8a06f8e3-f9d3-4060-b4da-ccfc87ca8f0d" />

---







