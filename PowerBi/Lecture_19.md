# Lecture 19: AI Visuals & Insights in Power BI

## Topic: Key Influencer Visual, Decomposition Tree, Smart Narratives, Quick Insights

---

## 1. Introduction to AI Visuals in Power BI

### 1.1 Theory

Power BI AI visuals use built-in machine learning and analytics capabilities to automatically discover patterns, trends, and key drivers in data without writing complex DAX or code.

AI visuals help:

* Identify reasons behind performance changes
* Break down metrics dynamically
* Generate automatic textual insights
* Quickly explore datasets for hidden patterns

These visuals are especially useful for:

* Business users
* Management dashboards
* Exploratory data analysis

---

## 2. Key Influencer Visual

### 2.1 Theory

The **Key Influencer visual** identifies factors that influence a selected metric the most. It answers questions like:

* Why is profit high or low?
* What factors influence customer churn?
* What drives sales growth?

It works by analyzing relationships between the **analyzed metric** and explanatory fields.

---

### 2.2 How Key Influencer Works

* Select a numeric or categorical outcome
* Power BI evaluates other fields
* Ranks influencers based on impact
* Shows positive and negative influencers

Types of Analysis:

* **Top Influencers** (most impactful factors)
* **Key Segments** (groups with highest or lowest outcomes)

---

### 2.3 Practical Example (Conceptual)

Scenario:

* Analyze: **Profit**

Influencers:

* Product Category
* Region
* Customer Segment
* Discount Level

Insight:

* High discounts strongly reduce profit
* Corporate customers generate higher profit

---

### 2.4 Practice Tasks

1. Create a Key Influencer visual for Profit
2. Add Product, Region, and Customer Segment as influencers
3. Identify top 3 positive and negative influencers
4. Interpret results in business language

---

## 3. Decomposition Tree

### 3.1 Theory

The **Decomposition Tree** allows users to break down a measure into contributing dimensions interactively. It helps answer:

* What contributes to total sales?
* Why is performance changing?

Unlike static visuals, users can drill dynamically using AI-driven or manual splits.

---

### 3.2 Key Features

* Dynamic drill-down
* AI splits (High value / Low value)
* Manual splits by dimensions
* Root cause analysis

---

### 3.3 Practical Example (Conceptual)

Scenario:

* Measure: **Total Sales**

Breakdown:

* Region → Category → Sub-Category → Product

AI Insight:

* AI highlights Region with highest sales automatically

---

### 3.4 Practice Tasks

1. Create a Decomposition Tree for Total Sales
2. Break down by Region and Product Category
3. Use AI split to identify top contributors
4. Explain findings

---

## 4. Smart Narratives

### 4.1 Theory

**Smart Narratives** automatically generate textual summaries of visuals and data trends using AI. They convert data insights into readable explanations.

Used for:

* Executive summaries
* Automated reporting
* Storytelling dashboards

---

### 4.2 Features of Smart Narratives

* Auto-generated insights
* Dynamic updates with filters
* Custom editable text
* KPI explanations

---

### 4.3 Practical Example (Conceptual)

Scenario:

* Dashboard with Sales, Profit, and Growth

Smart Narrative Output:

* Sales increased compared to last month
* Profit decreased due to higher discounts
* West region performed best

---

### 4.4 Practice Tasks

1. Add a Smart Narrative visual to a report page
2. Apply slicers and observe text changes
3. Edit narrative to add business context
4. Use it as an executive summary

---

## 5. Quick Insights in Power BI

### 5.1 Theory

**Quick Insights** automatically analyze datasets to uncover patterns such as:

* Trends
* Outliers
* Correlations
* Seasonality

It provides instant insights without manual visual creation.

---

### 5.2 How Quick Insights Works

* Power BI runs background algorithms
* Generates insight cards
* Each card includes a suggested visual

Limitations:

* Works best on clean datasets
* Requires aggregated data

---

### 5.3 Practical Example (Conceptual)

Insights Generated:

* Sales spike in Q4
* Profit anomaly in one region
* Strong correlation between discount and sales

---

### 5.4 Practice Tasks

1. Run Quick Insights on a dataset
2. Review at least 5 insight cards
3. Add one insight to a report
4. Validate whether insight makes business sense

---

## 6. Comparison of AI Visuals

| Feature       | Key Influencer   | Decomposition Tree  | Smart Narrative | Quick Insights |
| ------------- | ---------------- | ------------------- | --------------- | -------------- |
| Purpose       | Identify drivers | Root cause analysis | Text summary    | Auto discovery |
| Interactivity | Medium           | High                | Low             | Low            |
| User Control  | Medium           | High                | Medium          | Low            |

---

## 7. Summary

* AI visuals reduce manual analysis effort
* Key Influencers explain *why* outcomes occur
* Decomposition Tree supports interactive analysis
* Smart Narratives enhance storytelling
* Quick Insights enable fast exploration

---

## 8. Assignment

Create a Power BI report using:

1. One Key Influencer visual
2. One Decomposition Tree
3. One Smart Narrative
4. Run Quick Insights and include at least one insight

Document insights and business conclusions.

---

