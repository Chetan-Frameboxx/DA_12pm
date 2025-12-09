# Power Query Practice Tasks Using the Uncleaned 1000-Row Dataset

This document provides a complete list of cleaning, transformation, and analysis tasks that can be practiced using the uncleaned dataset generated for Power Query.

---

# 1. Data Cleaning / Standardization Tasks

## 1.1 Clean the Name Column

* Remove leading and trailing spaces.
* Convert names to Proper Case (John, Alice, Bob).
* Replace incorrect variants (john, JON, john␣).
* Replace null/blank values with "Unknown".

## 1.2 Clean the City Column

* Trim unnecessary spaces.
* Correct misspellings (Banglore → Bangalore).
* Standardize text case (mumbai → Mumbai).
* Replace null values.

## 1.3 Clean the Product Column

* Convert text to Proper Case.
* Fix inconsistent values (MOBILE → Mobile, laptop → Laptop).
* Handle missing entries.

## 1.4 Clean the Quantity Column

* Convert text values to numbers ("3" → 3).
* Convert word numbers ("five" → 5).
* Replace nulls with 0.
* Remove or correct invalid entries.

## 1.5 Clean the Price Column

* Remove extra spaces ("15000␣" → 15000).
* Convert shortened values ("20k" → 20000).
* Convert the column to numeric data type.
* Replace missing prices as needed.

---

# 2. Date Cleaning Tasks

## 2.1 Standardize Date Format

* Convert all date formats (YYYY-MM-DD, DD-MM-YYYY, MM/DD/YYYY) into one format.
* Ensure the data type is Date, not Text.

## 2.2 Add Date-Based Columns

* Year
* Month Name
* Quarter
* Week Number

---

# 3. Status Column Cleaning

* Trim internal and external spaces.
* Standardize values:

  * " delivered " → Delivered
  * "CANCELLED" → Cancelled
  * null → Unknown

---

# 4. Data Transformation Tasks

## 4.1 Add New Columns

* **TotalAmount = Quantity × Price**
* **OrderAge = Today's Date − OrderDate**
* Categorize cities into groups (e.g., Metro vs Non-Metro).

## 4.2 Remove Duplicates

* Identify duplicates based on Name + City + Product.
* Find duplicates by OrderDate.

---

# 5. Filtering and Sorting Tasks

## 5.1 Filtering Tasks

* Filter rows with missing prices.
* Filter orders above 50,000.
* Filter only Delivered orders.

## 5.2 Sorting Tasks

* Sort prices high → low.
* Sort order dates old → new.

---

# 6. Grouping & Aggregation Tasks

Use **Group By** in Power Query to create summaries.

* Total sales per city.
* Total quantity sold per product.
* Average order value per month.
* Count of orders by status (Delivered, Pending, Cancelled).

---

# 7. M-Code Practice Tasks

Write custom M-code using:

* **IF statements**
* **Text functions** (Text.Trim, Text.Proper, Text.Upper)
* **Number functions**
* **Date functions**

Examples:

* Custom conditional columns.
* Custom value replacements.
* Custom transformations.

---

# 8. Power BI Practice Using Cleaned Data

After cleaning the data, load it into Power BI and create:

* City-wise sales chart.
* Product revenue analysis.
* Monthly order trend.
* Status distribution chart.

---

# 9. ETL Workflow Simulation

Practice a full professional ETL pipeline:

### Extract

* Import the messy CSV.

### Transform

* Apply all cleaning and transformation steps.

### Load

* Load into Power BI or Excel.
* Create dashboards or pivot reports.

---
