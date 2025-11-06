
# Lecture 7: Statistical & Analytical Functions in Excel

## Lecture Objectives
By the end of this lecture, learners will be able to:

- Use conditional counting and summing functions.  
- Perform ranking and descriptive statistics.  
- Analyze large datasets using summary functions.

---

## 1. Introduction to Statistical & Analytical Functions
Statistical and analytical functions are used in Excel to **summarize, measure trends, and analyze patterns**.  
These functions help data analysts understand **performance metrics, averages, outliers, and distributions** within a dataset.

---

## 2. COUNT, COUNTA, COUNTBLANK

| Function | Purpose | Example |
|-----------|----------|----------|
| `COUNT(range)` | Counts cells containing numbers | `=COUNT(B2:B100)` |
| `COUNTA(range)` | Counts cells containing any data (numbers or text) | `=COUNTA(A2:A100)` |
| `COUNTBLANK(range)` | Counts empty cells | `=COUNTBLANK(C2:C100)` |

**Use Case:** Count how many sales records contain valid sales data and how many are blank.

---

## 3. Conditional Counting and Summing Functions

### COUNTIF
Counts cells that meet a specific condition:  
```excel
=COUNTIF(B2:B100, ">10000")
```
Counts sales greater than 10,000.

### COUNTIFS
Counts cells that meet multiple conditions:  
```excel
=COUNTIFS(B2:B100, ">10000", C2:C100, "West")
```

### SUMIF
Adds values based on a single condition:  
```excel
=SUMIF(A2:A100, "North", C2:C100)
```
Sum of sales from North region.

### SUMIFS
Adds values based on multiple conditions:  
```excel
=SUMIFS(C2:C100, A2:A100, "West", B2:B100, ">15000")
```

---

## 4. AVERAGEIF and AVERAGEIFS

These functions calculate conditional averages.

| Function | Example | Meaning |
|-----------|----------|----------|
| `AVERAGEIF(range, criteria, avg_range)` | `=AVERAGEIF(A2:A100, "South", C2:C100)` | Average of sales for South region |
| `AVERAGEIFS(avg_range, range1, criteria1, range2, criteria2)` | `=AVERAGEIFS(C2:C100, A2:A100, "West", B2:B100, ">10000")` | Average sales where region is West and sales > 10,000 |

---

## 5. RANK, RANK.EQ, and RANK.AVG

Used to **rank numerical data** such as sales or performance scores.

| Function | Description | Example |
|-----------|--------------|----------|
| `RANK(number, ref, [order])` | Returns rank of a number | `=RANK(B2, B2:B100, 0)` |
| `RANK.EQ` | Returns same rank for equal values | `=RANK.EQ(B2, B2:B100)` |
| `RANK.AVG` | Returns average rank for ties | `=RANK.AVG(B2, B2:B100)` |

---

## 6. LARGE, SMALL, and PERCENTILE Functions

| Function | Purpose | Example |
|-----------|----------|----------|
| `LARGE(array, k)` | Returns k-th largest value | `=LARGE(B2:B100, 1)` → Highest sales |
| `SMALL(array, k)` | Returns k-th smallest value | `=SMALL(B2:B100, 3)` → 3rd smallest value |
| `PERCENTILE.INC(array, k)` | Returns value at a given percentile | `=PERCENTILE.INC(B2:B100, 0.9)` → 90th percentile value |

---

## 7. Descriptive Statistics

| Function | Description | Example |
|-----------|--------------|----------|
| `AVERAGE(range)` | Mean value | `=AVERAGE(B2:B100)` |
| `MEDIAN(range)` | Middle value | `=MEDIAN(B2:B100)` |
| `MODE.SNGL(range)` | Most frequent value | `=MODE.SNGL(B2:B100)` |
| `STDEV.S(range)` | Standard deviation (sample) | `=STDEV.S(B2:B100)` |
| `VAR.S(range)` | Variance (sample) | `=VAR.S(B2:B100)` |
| `MAX/MIN(range)` | Highest or lowest value | `=MAX(B2:B100)` / `=MIN(B2:B100)` |

---

## 8. Data Analysis Example

**Scenario:**  
A sales manager wants to analyze:
- Total sales per region  
- Average sales per employee  
- Top 5 performers  
- Standard deviation of monthly sales  

**Functions Used:**
- `SUMIFS` for total region-wise sales  
- `AVERAGEIFS` for average performance  
- `LARGE` for top performers  
- `STDEV.S` for variation

---

## 9. Best Practices
- Use **structured table references** for dynamic ranges.  
- Use **named ranges** to simplify complex formulas.  
- Combine **conditional and statistical functions** for deeper insights.  

---

## Lecture 7 – Interview QnA

1. What is the difference between COUNT and COUNTA?  
2. How do SUMIF and SUMIFS differ?  
3. Which function would you use to find the top 3 sales values?  
4. What does the RANK function do?  
5. What is the purpose of STDEV.S and when is it used?  
6. How can you find the 90th percentile of a dataset?  
7. What is the difference between MEDIAN and MODE?  
8. What is the advantage of using COUNTIFS over COUNTIF?  
9. What’s the difference between sample and population functions in Excel?  
10. Give an example of how you would use SUMIFS in a business report.

---

## Lecture 7 – Practical Assignment (No Hints)

1. Count how many employees made sales above 20,000.  
2. Count how many sales were made in the “West” region.  
3. Find the total sales for each region.  
4. Find the average sales where the target was above 30,000.  
5. Determine the highest and lowest sale in the dataset.  
6. Rank all employees based on their sales amount.  
7. Find the top 5 and bottom 5 performers using LARGE and SMALL.  
8. Calculate the standard deviation and variance of all sales.  
9. Find the 75th percentile of the Sales Amount column.  
10. Prepare a summary table showing Region, Total Sales, Average Sales, and Number of Employees.
