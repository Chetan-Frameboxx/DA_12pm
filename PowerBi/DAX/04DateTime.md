# Lecture: Date & Time Intelligence in Power BI (DAX)

## 1. Theory

### 1.1 Date & Time Data Types

* **Date**: Stores only date (YYYY-MM-DD)
* **Time**: Stores time (HH:MM:SS)
* **Datetime**: Combination of both
* **Duration**: Stored as number representing days

### 1.2 Importance of Date Tables

A proper **Date Table** enables:

* Time intelligence functions
* Year-to-date, month-to-date, quarter calculations
* Proper sorting and filtering

A Date Table must:

* Contain continuous dates
* Have no gaps
* Be marked as a **Date Table** in Power BI

### 1.3 Types of Date Calculations

* Extracting parts of dates (Year, Month, Quarter…)
* Formatting dates
* Time intelligence (YTD, MTD, QTD)
* Comparing periods (previous month, previous year)
* Working with durations

---

## 2. Practical Examples (Full Programs)

### 2.1 Extracting Date Parts

```DAX
Year = YEAR('Sales'[OrderDate])
MonthNumber = MONTH('Sales'[OrderDate])
MonthName = FORMAT('Sales'[OrderDate], "MMMM")
Quarter = QUARTER('Sales'[OrderDate])
Day = DAY('Sales'[OrderDate])
WeekdayName = FORMAT('Sales'[OrderDate], "dddd")
WeekNumber = WEEKNUM('Sales'[OrderDate], 2)
```

### 2.2 Creating a Date Table

```DAX
DateTable =
ADDCOLUMNS(
    CALENDAR(DATE(2018,1,1), DATE(2030,12,31)),
    "Year", YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month Name", FORMAT([Date], "MMMM"),
    "Month Short", FORMAT([Date], "MMM"),
    "Quarter", "Q" & FORMAT(QUARTER([Date]), "0"),
    "Year-Month", FORMAT([Date], "YYYY-MM")
)
```

### 2.3 Time Intelligence Functions

#### Year-To-Date (YTD)

```DAX
Sales YTD =
TOTALYTD(SUM('Sales'[SalesAmount]), 'DateTable'[Date])
```

#### Month-To-Date (MTD)

```DAX
Sales MTD =
TOTALMTD(SUM('Sales'[SalesAmount]), 'DateTable'[Date])
```

#### Quarter-To-Date (QTD)

```DAX
Sales QTD =
TOTALQTD(SUM('Sales'[SalesAmount]), 'DateTable'[Date])
```

### 2.4 Previous Period Functions

#### Previous Day

```DAX
Sales Previous Day =
CALCULATE(SUM('Sales'[SalesAmount]), PREVIOUSDAY('DateTable'[Date]))
```

#### Previous Month

```DAX
Sales Previous Month =
CALCULATE(SUM('Sales'[SalesAmount]), PREVIOUSMONTH('DateTable'[Date]))
```

#### Previous Year

```DAX
Sales Previous Year =
CALCULATE(SUM('Sales'[SalesAmount]), PREVIOUSYEAR('DateTable'[Date]))
```

### 2.5 Same Period Last Year (SPLY)

```DAX
Sales Same Period LY =
CALCULATE(SUM('Sales'[SalesAmount]), SAMEPERIODLASTYEAR('DateTable'[Date]))
```

### 2.6 Date Difference & Age Calculation

#### Difference in Days

```DAX
DateDiffDays =
DATEDIFF('Sales'[StartDate], 'Sales'[EndDate], DAY)
```

#### Difference in Months

```DAX
DateDiffMonths =
DATEDIFF('Sales'[StartDate], 'Sales'[EndDate], MONTH)
```

#### Age Calculation

```DAX
Age =
DATEDIFF('Customer'[DOB], TODAY(), YEAR)
```

### 2.7 Calculating Working Days

```DAX
Working Days =
CALCULATE(
    COUNTROWS('DateTable'),
    'DateTable'[IsWorkingDay] = TRUE()
)
```

(Assuming DateTable includes a column identifying weekends & holidays)

### 2.8 Formatting Dates

```DAX
DateFormatted = FORMAT('Sales'[OrderDate], "DD-MMM-YYYY")
TimeFormatted = FORMAT('Sales'[OrderTime], "HH:mm:ss")
```

---

## 3. Advanced Time Intelligence

### 3.1 Rolling 12 Months

```DAX
Sales Rolling 12M =
CALCULATE(
    SUM('Sales'[SalesAmount]),
    DATESINPERIOD('DateTable'[Date], MAX('DateTable'[Date]), -12, MONTH)
)
```

### 3.2 Current Month Sales

```DAX
Current Month Sales =
CALCULATE(
    SUM('Sales'[SalesAmount]),
    MONTH('DateTable'[Date]) = MONTH(TODAY()),
    YEAR('DateTable'[Date]) = YEAR(TODAY())
)
```

### 3.3 Last N Days

```DAX
Sales Last 30 Days =
CALCULATE(
    SUM('Sales'[SalesAmount]),
    DATESINPERIOD('DateTable'[Date], TODAY(), -30, DAY)
)
```

---

## 4. Common Fixes & Mistakes

### 4.1 Month Name to Month Number

```DAX
MonthNumber = MONTH(DATEVALUE("1 " & 'Sales'[MonthName]))
```

### 4.2 Sorting Month Name by Month Number

Sort **MonthName** column by **MonthNumber**.

### 4.3 Blank Dates

```DAX
Sales Without Blanks = COALESCE(SUM('Sales'[SalesAmount]), 0)
```

### 4.4 Time Comparison with Non-Date Columns

Always use **a proper date table**.

---

## 5. Practice Tasks

### Task 1

Create a Date Table from 2015 to 2035 with:

* Year
* Quarter
* Month Number
* Month Name
* Day Name
* Is Weekend

### Task 2

Calculate:

* Sales YTD
* Sales MTD
* Sales Previous Year
* Sales Same Period Last Year

### Task 3

Calculate:

* Age of customer
* Average delivery time
* Difference in weeks between two dates

### Task 4

Create:

* Rolling 3 months sales
* Rolling 6 months sales
* Rolling 12 months sales

### Task 5

Convert these month names into month numbers:

```
January
March
October
```

### Task 6

Format a date column as:

* DD/MM/YYYY
* YYYY-MM-DD
* MMM YYYY

---
