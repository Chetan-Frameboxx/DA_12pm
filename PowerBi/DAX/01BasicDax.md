# Lecture 1 — Introduction to DAX

## Theory

### 1. What is DAX?

DAX (Data Analysis Expressions) is the formula language used in Power BI for creating calculations over data models. It operates on tables and columns rather than individual cells, enabling dynamic aggregations and analytical computations.

Key points:

* Designed for tabular data models.
* Used to create calculated columns, measures, and calculated tables.
* Works closely with the data model, relationships, and filter context.

### 2. Calculated Columns vs Measures

#### Calculated Columns

* Computed **row by row** during data refresh.
* Stored in the model.
* Useful for classifications, derived data, or relationship keys.
* Always return a single value per row.

#### Measures

* Computed **on the fly** based on filters in visuals.
* Not stored; recalculated depending on context.
* Ideal for aggregations (SUM, AVG, etc.).
* React dynamically to slicers, filters, and report interactions.

**Summary:** Calculated columns solve row‑level logic; measures solve aggregated logic.

### 3. Difference Between SUM and SUMX

#### SUM

* Adds up all the values in a **single column**.
* Straightforward column aggregation.

```
Total Sales = SUM(Sales[Amount])
```

#### SUMX

* Iterates **row by row** over a table.
* Evaluates an expression for each row, then sums the results.
* Used when aggregation depends on a calculation.

```
Total Profit = SUMX(Sales, Sales[Amount] - Sales[Cost])
```

**Summary:** SUM adds column values directly; SUMX calculates for each row first, then sums.

### 4. Count Functions: COUNT, COUNTA, COUNTBLANK

#### COUNT

* Counts numeric (non-blank) values in a column.

```
Count Numeric = COUNT(Sales[Amount])
```

#### COUNTA

* Counts non-blank values, regardless of data type.

```
Count Any = COUNTA(Sales[Remark])
```

#### COUNTBLANK

* Counts blank/empty values in a column.

```
Blank Count = COUNTBLANK(Sales[Comment])
```

**Summary:**
COUNT → only numbers
COUNTA → all non-blanks
COUNTBLANK → blanks only

---

## Practical Examples

Assume a table **Sales** with columns: Date, Product, Quantity, Price, Cost, Remark.

1. **Calculated Column Example**

```
Profit = Sales[Price] - Sales[Cost]
```

2. **Measure Example (Total Sales)**

```
Total Sales = SUM(Sales[Price])
```

3. **SUMX Example (Total Profit)**

```
Total Profit = SUMX(Sales, Sales[Price] - Sales[Cost])
```

4. **Counting Values**

```
Total Orders = COUNTA(Sales[Product])
Blank Remarks = COUNTBLANK(Sales[Remark])
```

---

## Practice Tasks

1. Create a calculated column `Profit = Price - Cost`.
2. Create a measure `Total Sales` using SUM.
3. Create a measure `Total Profit` using SUMX.
4. Create three measures:

   * `Count Numeric Price = COUNT(Sales[Price])`
   * `Count Non Blank Product = COUNTA(Sales[Product])`
   * `Count Blank Remarks = COUNTBLANK(Sales[Remark])`
5. Build a simple report showing Product, Total Sales, Total Profit, and blank remark count.
