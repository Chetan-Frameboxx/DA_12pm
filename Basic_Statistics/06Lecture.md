# Lecture 6: Statistical Tests & Regression (Basics)

---

## Theory

### 1. Overview of Statistical Tests

Statistical tests are used in **inferential statistics** to make decisions or draw conclusions about a population using sample data.

They help answer questions such as:

* Is there a significant difference?
* Is there a relationship between variables?
* Is the observed result due to chance?

Each test is used under **specific conditions** based on:

* Data type
* Sample size
* Distribution assumptions

---

### 2. Z-Test

#### Purpose

Used to test hypotheses about the **population mean** when:

* Sample size is large (n ≥ 30)
* Population standard deviation is known
* Data is approximately normally distributed

#### Common Use Cases

* Quality control
* Manufacturing measurements

#### Example

A company claims the average delivery time is 5 days. A large sample is tested to verify this claim.

---

### 3. T-Test

#### Purpose

Used to compare means when:

* Sample size is small (n < 30)
* Population standard deviation is unknown

#### Types of T-Tests

* **One-sample t-test**: Compare sample mean with a known value
* **Independent t-test**: Compare means of two different groups
* **Paired t-test**: Compare means before and after an intervention

#### Example

Comparing average marks of students taught using two different teaching methods.

---

### 4. Chi-Square Test

#### Purpose

Used to test the relationship between **categorical variables**.

#### Key Characteristics

* Works with frequency data
* Does not require normal distribution

#### Common Applications

* Gender vs product preference
* Education level vs employment status

---

### 5. When to Use Which Test

| Scenario                       | Appropriate Test |
| ------------------------------ | ---------------- |
| Mean comparison (large sample) | Z-test           |
| Mean comparison (small sample) | T-test           |
| Categorical data relationship  | Chi-square test  |

---

### 6. Introduction to Simple Linear Regression

**Regression analysis** examines the relationship between:

* One dependent variable (Y)
* One independent variable (X)

Purpose:

* Understand relationship
* Predict values

Example:

* Advertising spend vs sales
* Study hours vs exam score

---

### 7. Regression Equation

The simple linear regression equation is:

Y = a + bX

Where:

* Y = Dependent variable
* X = Independent variable
* a = Intercept (value of Y when X = 0)
* b = Slope (change in Y for one-unit change in X)

---

### 8. Interpretation of Regression Results

#### Slope (b)

* Positive slope → Positive relationship
* Negative slope → Negative relationship

#### Intercept (a)

* Starting value of Y

#### Strength of Relationship

* Often evaluated using correlation (r) or R² (conceptual level)

---

### 9. Use of Statistics in Data Analysis Tools

#### Excel

* AVERAGE, STDEV, CORREL
* Data Analysis ToolPak (t-test, regression)

#### Power BI

* DAX measures for averages
* Trend lines and forecasting
* Statistical visuals

#### Python (Overview)

* NumPy for numerical analysis
* Pandas for data handling
* Matplotlib / Seaborn for visualization
* SciPy & Statsmodels for statistical tests

---

## Practical Examples (Full Scenarios)

### Example 1: Choosing the Right Test

Scenario:

* Comparing average sales before and after a discount campaign

Correct Test:

* Paired t-test

Reason:

* Same stores measured before and after the campaign

---

### Example 2: Simple Regression Case

Dataset:

| Advertising Spend (₹) | Sales (₹) |
| --------------------- | --------- |
| 10,000                | 50,000    |
| 20,000                | 70,000    |
| 30,000                | 90,000    |

Observation:

* As advertising spend increases, sales increase
* Positive linear relationship

---

## Practice Tasks

### Task 1: Test Identification

Identify the appropriate test:

1. Comparing average salaries of two companies
2. Checking relationship between gender and product choice

---

### Task 2: Conceptual Question

Why is t-test preferred over z-test for small samples?

---

### Task 3: Regression Interpretation

If slope (b) = 2, what does it indicate about X and Y?

---

### Task 4: Tool Mapping

Map the following to tools:

* Mean calculation
* Hypothesis testing
* Regression analysis

---

### Task 5: Real-World Application

Choose a business scenario and:

* Identify dependent and independent variables
* Decide whether a test or regression is suitable

---

## Learning Outcomes (Revisited)

By the end of this lecture, you should be able to:

* Identify appropriate statistical tests
* Understand basic hypothesis testing tools
* Interpret simple linear regression results
* Connect statistical concepts with Excel, Power BI, and Python

---

