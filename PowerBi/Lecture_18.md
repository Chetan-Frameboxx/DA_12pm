# Lecture 18: Power BI Optimization

## Topic: Data Model Optimization, Performance Analyzer Tool, Best Practices for Faster Dashboards

---

## 1. Data Model Optimization

### 1.1 Theory

Data Model Optimization in Power BI focuses on designing efficient data structures so that reports load faster, consume less memory, and respond quickly to user interactions.

A poorly designed data model leads to:

* Slow report loading
* Delays when using slicers or filters
* High memory usage
* Poor user experience

An optimized data model ensures:

* Faster DAX calculations
* Better compression
* Scalable reports

#### Key Concepts

**Star Schema**

* Central **Fact table** (Sales, Orders, Transactions)
* Surrounding **Dimension tables** (Date, Product, Customer)
* One-to-many relationships

**Why Star Schema is Important**

* Faster query performance
* Simpler DAX formulas
* Better storage engine optimization

---

### 1.2 Data Model Optimization Techniques

#### 1. Remove Unnecessary Columns

* Delete unused columns from tables
* Remove auto-generated index columns
* Avoid loading raw text columns not used in visuals

#### 2. Reduce Cardinality

* Cardinality = number of unique values in a column
* High cardinality columns slow down performance

Examples:

* Use Year instead of full DateTime where possible
* Replace long text columns with numeric keys

#### 3. Choose Correct Data Types

* Use **Whole Number** instead of Decimal when possible
* Use **Date** instead of DateTime if time is not required
* Avoid storing numbers as text

#### 4. Disable Auto Date/Time

* Power BI creates hidden date tables by default
* This increases model size

Recommended:

* Turn off Auto Date/Time
* Create a single custom Date table

#### 5. Optimize Relationships

* Avoid bi-directional relationships unless required
* Use single direction (Dimension → Fact)
* Avoid many-to-many relationships when possible

---

### 1.3 Practical Example (Conceptual)

**Before Optimization**

* One large table with Sales, Customer, Product, Date
* DateTime column with timestamp
* Text-based IDs

**After Optimization**

* FactSales table
* DimDate, DimCustomer, DimProduct tables
* Integer keys
* Date column without time

Result:

* Faster visuals
* Smaller file size
* Simpler DAX

---

### 1.4 Practice Tasks

1. Identify unused columns in an existing Power BI dataset
2. Convert DateTime columns to Date where time is not required
3. Split a flat table into Fact and Dimension tables
4. Disable Auto Date/Time and create a custom Date table

---

## 2. Performance Analyzer Tool

### 2.1 Theory

The **Performance Analyzer** is a built-in Power BI tool used to measure how long visuals take to load and identify performance bottlenecks.

It helps analyze:

* DAX query execution time
* Visual rendering time
* Report performance issues

---

### 2.2 Components of Performance Analyzer

Each visual is broken into:

1. **DAX Query**

   * Time taken to execute DAX
   * Indicates inefficient calculations

2. **Visual Display**

   * Time taken to render the chart
   * Affected by chart type and data volume

3. **Other**

   * Minor overhead processing

---

### 2.3 How to Use Performance Analyzer

Step-by-step Process:

1. Go to **View → Performance Analyzer**
2. Click **Start Recording**
3. Interact with slicers or visuals
4. Click **Stop Recording**
5. Review time taken by each visual

You can also:

* Copy DAX queries for optimization
* Identify slow-performing visuals

---

### 2.4 Practical Example

Scenario:

* A table visual takes 5 seconds to load

Analysis:

* DAX Query: 4 seconds
* Visual Display: 1 second

Conclusion:

* DAX measure needs optimization
* Possibly using complex iterators or unnecessary filters

---

### 2.5 Practice Tasks

1. Run Performance Analyzer on an existing report
2. Identify the slowest visual
3. Note whether delay is due to DAX or rendering
4. Rewrite one slow measure using simpler logic

---

## 3. Best Practices for Faster Dashboards

### 3.1 Theory

Dashboard performance depends on:

* Data model design
* DAX efficiency
* Visual selection
* User interaction patterns

Following best practices ensures smooth user experience even with large datasets.

---

### 3.2 Best Practices

#### 1. Optimize DAX Measures

* Avoid unnecessary CALCULATE usage
* Prefer SUM over SUMX when possible
* Avoid FILTER inside measures unless required

#### 2. Limit Number of Visuals

* Too many visuals increase load time
* Use multiple pages instead of one heavy page

#### 3. Use Appropriate Visual Types

* Tables and matrices are slower than charts
* Avoid high-cardinality columns in tables

#### 4. Reduce Slicer Complexity

* Avoid slicers with thousands of values
* Use dropdown slicers instead of list

#### 5. Use Aggregated Data

* Summarize data at required granularity
* Avoid row-level detail if not needed

#### 6. Enable Query Reduction

* Turn on query reduction options
* Prevent unnecessary queries on slicer selection

---

### 3.3 Practical Example

Poor Design:

* 15 visuals on one page
* Multiple slicers with large lists
* Complex calculated columns

Optimized Design:

* 6–8 visuals per page
* Dropdown slicers
* Measures instead of calculated columns

Result:

* Faster loading
* Better interactivity

---

### 3.4 Practice Tasks

1. Reduce visuals on a report page to under 8
2. Replace a table visual with a chart
3. Convert calculated columns to measures
4. Change slicers from list to dropdown

---

## 4. Summary

* Optimized data models improve performance and scalability
* Performance Analyzer helps identify slow visuals and DAX
* Following dashboard best practices ensures faster user experience

---

## 5. Assignment

Create a Power BI report and:

1. Apply data model optimization techniques
2. Analyze report using Performance Analyzer
3. Document at least 3 performance improvements
4. Present before vs after performance comparison

---

