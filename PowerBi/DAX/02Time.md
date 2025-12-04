# **Time Intelligence in Power BI Using the Dataset**


---

# **1. Theory**

Time Intelligence allows us to compare business performance across periods using date-based calculations. With an order-based dataset like ours, Time Intelligence helps answer questions such as:

* Are sales improving compared to last year?
* Which quarter performed the best?
* Are we growing month over month?
* What is the Year-to-Date (YTD) profit?
* What are the rolling 3-month trends?

To unlock these insights, we rely on:

* A proper **Date Table** (continuous date range)
* DAX Time Intelligence functions like **TOTALYTD**, **SAMEPERIODLASTYEAR**, **DATEADD**, **DATESINPERIOD**, etc.

---

## **1.1 Theory of Each Time Intelligence Formula**

### **TOTALYTD() — Year-to-Date Logic**

This function accumulates values from the start of the year up to the current date. It automatically respects your Date table’s year boundaries, even if your fiscal year is different.
It answers: *“How much have we sold so far this year?”*

### **TOTALMTD() — Month-to-Date Logic**

TOTALMTD gathers values from the first day of the month to the date selected in the filter context. Useful for monthly performance tracking.
It answers: *“What is the progress of this month so far?”*

### **TOTALQTD() — Quarter-to-Date Logic**

Similar to MTD/YTD, but for business quarters. Great for companies evaluating quarter-based growth.
It answers: *“How is this quarter doing compared to the previous?”*

### **SAMEPERIODLASTYEAR() — YOY Comparison**

Pulls the exact date range from the previous year. If today is 15th March 2024, it returns 15th March 2023.
It answers: *“Did we perform better than the same dates last year?”*

### **DATEADD() — Shift Date Context**

Moves the date context by a fixed number of days, months, quarters, or years — without caring about calendar structure.
It answers: *“What were the sales one month ago?”*

### **PARALLELPERIOD() — Period Shift (Whole Periods)**

Shifts context by whole calendar periods. It doesn’t depend on the current date context boundaries.
It answers: *“What were the sales in the previous quarter as a full block?”*

### **DATESINPERIOD() — Rolling Windows**

Creates a dynamic sliding window (e.g., last 3 months, last 30 days). Ideal for trend analysis.
It answers: *“What is the trend over the last N months/days?”*

---

# **2. Practical Examples (Full DAX Programs)** (Full DAX Programs)**

## **2.1 Create Base Measures**

```
Total Sales = SUM(Orders[Sales])
Total Profit = SUM(Orders[Profit])
Total Quantity = SUM(Orders[Quantity])
```

---

## **2.2 Year-to-Date Calculations**

```
Sales YTD =
    TOTALYTD(
        [Total Sales],
        'Date'[Date]
    )

Profit YTD =
    TOTALYTD(
        [Total Profit],
        'Date'[Date]
    )
```

---

## **2.3 Month-to-Date / Quarter-to-Date**

```
Sales MTD =
    TOTALMTD(
        [Total Sales],
        'Date'[Date]
    )

Sales QTD =
    TOTALQTD(
        [Total Sales],
        'Date'[Date]
    )
```

---

## **2.4 Same Period Last Year (YOY Comparison)**

```
Sales Last Year =
    CALCULATE(
        [Total Sales],
        SAMEPERIODLASTYEAR('Date'[Date])
    )
```

```
YOY Growth % =
    DIVIDE([Total Sales] - [Sales Last Year], [Sales Last Year])
```

---

## **2.5 Rolling 3-Month Sales**

```
Rolling 3 Month Sales =
    CALCULATE(
        [Total Sales],
        DATESINPERIOD(
            'Date'[Date],
            MAX('Date'[Date]),
            -3,
            MONTH
        )
    )
```

---

## **2.6 Sales Last Month / Last Quarter**

```
Sales Last Month =
    CALCULATE(
        [Total Sales],
        DATEADD('Date'[Date], -1, MONTH)
    )
```

```
Sales Last Quarter =
    CALCULATE(
        [Total Sales],
        DATEADD('Date'[Date], -1, QUARTER)
    )
```

---

# **3. Practice Tasks**

## **Task 1 — Build the Model**

* Create a Date table
* Mark it as a Date table
* Connect Orders[OrderDate] → Date[Date]

## **Task 2 — Create Basic Measures**

* Total Sales
* Total Profit
* Total Quantity

## **Task 3 — Time Intelligence Measures**

* Sales YTD
* Sales MTD
* Sales Last Year
* YOY Growth (%)
* Rolling 3-Month Sales

## **Task 4 — Visual Build**

Build these visuals:

* Line chart: Sales vs Sales Last Year
* Card: YTD Sales
* Clustered column chart: Sales by Region
* Moving trend chart: Rolling 3-Month Sales

## **Task 5 — KPI Dashboard**

Create a small dashboard showing:

* Total Sales
* Sales YTD
* YOY Growth (%)
* Top 5 Customers by Sales
* Profit by Region

---
