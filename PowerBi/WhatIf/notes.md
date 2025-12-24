# What-If Analysis in Power BI (Complete Guide)

---

## 1. Introduction to What-If Analysis

**What-If Analysis** in Power BI is a technique used to simulate different business scenarios by changing input values (assumptions) and instantly observing their impact on key metrics such as **Sales, Cost, and Profit**.

It is mainly implemented using:

* What-If Parameters
* DAX Measures
* Slicers
* Interactive visuals

This approach is widely used for **decision making, forecasting, pricing strategy, and financial planning**.

---

## 2. Why Use What-If Analysis

What-If Analysis helps answer questions like:

* What happens to profit if a 10% discount is applied?
* How much discount can be given without making a loss?
* How do pricing decisions affect overall revenue?

Common use cases:

* Sales and pricing strategy
* Budget planning
* Profit forecasting
* Business simulations

---

## 3. Dataset Overview

**Table Name:** `sample`

### Important Columns

* `Quantity`
* `Unit Price`
* `Cost Price`
* `Product`
* `Category`
* `Region`

Numeric columns are required for What-If Analysis.

---

## 4. Measures BEFORE What-If Analysis (Base Measures)

These measures represent the **actual business values** without any assumptions applied.

---

### 4.1 Total Quantity

```DAX
Total Quantity =
SUM('sample'[Quantity])
```

---

### 4.2 Total Sales

```DAX
Total Sales =
SUMX(
    'sample',
    'sample'[Quantity] * 'sample'[Unit Price]
)
```

**Explanation:**

* Sales must be calculated row by row
* `SUMX` performs row-level multiplication correctly
* Avoid using `SUM × SUM`

---

### 4.3 Total Cost

```DAX
Total Cost =
SUMX(
    'sample',
    'sample'[Quantity] * 'sample'[Cost Price]
)
```

---

### 4.4 Profit (Before Discount)

```DAX
Profit =
[Total Sales] - [Total Cost]
```

At this stage, all values are **static** and do not change dynamically.

---

## 5. Creating the What-If Parameter (Discount % Slicer)

The What-If Parameter allows users to interactively change a value using a slicer.

---

### 5.1 Steps to Create New Parameter

1. Go to the **Modeling** tab
2. Click **New Parameter → Numeric Range**
3. Configure the parameter as follows:

| Setting            | Value          |
| ------------------ | -------------- |
| Name               | Discount %     |
| Data Type          | Decimal Number |
| Minimum            | 0              |
| Maximum            | 30             |
| Increment          | 1              |
| Default            | 0              |
| Add slicer to page | Yes            |

4. Click **Create**

---

### 5.2 What Power BI Automatically Creates

Power BI automatically creates:

1. A table named `Discount %`
2. A column named `Discount %[Discount %]`
3. A measure named `Discount % Value` (calculator icon)
4. A slicer on the report page

**Important Rule:**
Always use the **measure** `Discount % Value` in DAX calculations, not the column.

---

## 6. Measures AFTER What-If Analysis

These measures change dynamically when the slicer value changes.

---

### 6.1 Discount Amount

```DAX
Discount Amount =
[Total Sales] * ('Discount %'[Discount % Value] / 100)
```

**Why `/100` is required:**

* Parameter values range from 0 to 30
* Must convert to percentage (0–0.30)

---

### 6.2 Sales After Discount

```DAX
Sales After Discount =
[Total Sales] - [Discount Amount]
```

This represents revenue after applying the discount.

---

### 6.3 Profit After Discount

```DAX
Profit After Discount =
[Sales After Discount] - [Total Cost]
```

This is the final profit based on the selected discount scenario.

---

## 7. Recommended Visual Setup

### Card Visuals

* Total Sales
* Total Cost
* Profit (Before Discount)
* Discount Amount
* Sales After Discount
* Profit After Discount

### Slicer

* Discount %

### Table / Matrix

* Product
* Sales After Discount
* Profit After Discount

---

## 8. How What-If Analysis Works (Flow)

1. User moves the **Discount % slicer**
2. Parameter measure value changes
3. Discount Amount recalculates
4. Sales After Discount updates
5. Profit After Discount updates
6. All visuals refresh automatically

This enables **real-time scenario simulation**.

---

## 9. Business Insights from What-If Analysis

* Identify maximum safe discount
* Detect products that become unprofitable first
* Analyze impact of pricing decisions
* Support data-driven business decisions

---

## 10. Key Rules to Remember

* Use `SUMX` when multiplying columns
* Do not use symbols like `×` or `%` in DAX
* Always use the parameter **measure**, not the column
* Convert percentage parameters using `/100`

---

## 11. Interview-Ready Explanation

> I used What-If Parameters in Power BI to simulate discount scenarios. A slicer dynamically adjusts the discount percentage, and DAX measures recalculate sales and profit in real time to support pricing decisions.

---

## 12. Possible Extensions

* Price Increase % What-If
* Cost Reduction % What-If
* Multiple parameters together
* Full business simulation dashboard

---

**End of What-If Analysis Documentation**
