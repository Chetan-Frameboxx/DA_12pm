# Lecture 1 – Statistical Foundations for Data Analysis

---

## Theory

### 1. Number System

In data analysis, numbers are the backbone of all calculations. Understanding number systems helps in correct data interpretation.

**a) Natural Numbers**
1, 2, 3, 4, ... (Counting numbers)

**b) Whole Numbers**
0, 1, 2, 3, ...

**c) Integers**
-5, -2, 0, 3, 10

**d) Rational Numbers**
Numbers expressed as fractions (e.g., 1/2, 3.5)

**e) Irrational Numbers**
π, √2 (Non-terminating, non-repeating)

**f) Real Numbers**
All rational and irrational numbers (used most in analytics)

---

### 1.1 Number System Conversions

Conversions are mainly used in **computer systems, data storage, and low-level data processing**.

#### a) Decimal to Binary

Steps:

1. Divide the decimal number by 2
2. Write remainder
3. Repeat until quotient becomes 0
4. Read remainders from bottom to top

**Example:** 10 (Decimal)

* 10 ÷ 2 = 5 (R 0)
* 5 ÷ 2 = 2 (R 1)
* 2 ÷ 2 = 1 (R 0)
* 1 ÷ 2 = 0 (R 1)

Result: **1010 (Binary)**

---

#### b) Binary to Decimal

Steps:

1. Multiply each digit by powers of 2
2. Add the results

**Example:** 1011 (Binary)

= (1×2³) + (0×2²) + (1×2¹) + (1×2⁰)
= 8 + 0 + 2 + 1 = **11 (Decimal)**

---

#### c) Decimal to Octal

Steps:

1. Divide by 8
2. Write remainder
3. Read from bottom to top

**Example:** 65 (Decimal) → **101 (Octal)**

---

#### d) Decimal to Hexadecimal

Uses base 16 (0–9, A–F)

**Example:** 26 (Decimal)

* 26 ÷ 16 = 1 (R 10 → A)
* 1 ÷ 16 = 0 (R 1)

Result: **1A (Hexadecimal)**

---

#### e) Binary to Hexadecimal

Group binary digits into sets of 4.

**Example:** 11010110

* 1101 → D
* 0110 → 6

Result: **D6 (Hexadecimal)**

---

**Note for Data Analysts:**

* Decimal: Used in reports & dashboards
* Binary: Used internally by computers
* Hexadecimal: Used in memory addresses & colors

---

### 2. Types of Data

Data is classified based on **nature and measurement**.

#### A. Qualitative (Categorical Data)

Descriptive data that represents **qualities or categories**.

* **Nominal Data**
  Categories without order (Gender, Country, Product Type)

* **Ordinal Data**
  Categories with order (Ratings, Satisfaction Level, Education Level)

---

#### B. Quantitative (Numerical Data)

Data that can be **measured numerically**.

* **Discrete Data**
  Countable values (Number of orders, Employees)

* **Continuous Data**
  Measurable values (Salary, Height, Revenue)

---

### 3. Measures of Central Tendency

Used to identify the **central or typical value** of a dataset.

#### a) Mean (Average)

Sum of all values ÷ Number of values

Used when data is **normally distributed**.

#### b) Median

Middle value after sorting the data.

Best for **skewed data** such as income or salary.

#### c) Mode

Most frequently occurring value.

Useful for **categorical data**.

---

### 4. Measures of Dispersion (Spread of Data)

Shows how **spread out** the data values are.

#### a) Range

Maximum value − Minimum value

#### b) Variance

Average of squared differences from the mean.

Indicates how far values are from the mean.

#### c) Standard Deviation

Square root of variance.

Most commonly used measure of spread.

#### d) Interquartile Range (IQR)

Q3 − Q1

Helps identify **outliers**.

---

## Practical Examples (Conceptual)

### Example 1: Salary Data

* Mean salary may be high due to top executives
* Median gives a better picture of typical employee salary
* Standard deviation shows salary inequality

---

### Example 2: Student Marks

* Mean marks show overall performance
* Range shows performance gap
* IQR identifies extreme scorers

---

### Example 3: Sales Data

* Mean daily sales for forecasting
* Standard deviation to measure volatility

---

## Practice Tasks

### Task 1

Classify the following into correct number types:

* -15
* 3.75
* √9

---

### Task 2

Identify the data type:

* Customer ID
* Product Price
* Feedback Rating (1–5)

---

### Task 3

Given data: 10, 12, 14, 18, 46

* Calculate Mean
* Find Median
* Identify Mode

---

### Task 4

Explain why median is preferred over mean for income data.

---

### Task 5

Which measure of dispersion would you use to detect outliers and why?

---

## Key Takeaways

* Numbers define how data is processed
* Correct data type selection avoids wrong analysis
* Central tendency explains **where data centers**
* Dispersion explains **how data varies**

---

