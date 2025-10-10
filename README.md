# Integration and analysis of financial data from heterogeneous sources using DuckDB 🦆

## Query runtime optimization bar chart

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

This analysis leverages DuckDB to efficiently join transactional and account data with address data, supporting high-performance, location-based insights.

<img width="1059" height="1158" alt="image" src="https://github.com/user-attachments/assets/4ced7070-9655-48fe-b36e-937dce652295" />

---






