# Lecture Plan: What-If Analysis in Excel

## Learning Objectives
- Understand what “What-If Analysis” means in Excel.
- Use Goal Seek, Scenario Manager, and Data Tables effectively.
- Apply these tools to make data-driven decisions and forecast outcomes.

---

## 1. Introduction to What-If Analysis

### Definition:
What-If Analysis helps you change input values in formulas to see how those changes affect the results.
It’s used for forecasting, decision making, and planning.

Example:
If you have a formula to calculate profit:
```
=Revenue - Cost
```
You can use What-If Analysis to see how changing the Cost or Revenue affects the Profit.

---

## 2. Types of What-If Analysis in Excel

### A. Goal Seek
Used when you know the desired result, but want to find the input value that gives that result.

Example:
- You want a total profit of ₹50,000
- Formula: `=Revenue - Cost`
- Current Revenue: ₹2,00,000
- You want to know what Cost value gives ₹50,000 profit.

Steps:
1. Go to Data → What-If Analysis → Goal Seek
2. Set Cell: Profit cell
3. To Value: 50000
4. By Changing Cell: Cost cell
5. Click OK

Excel finds the cost value automatically.

---

### B. Scenario Manager
Used when you want to compare different sets of input values and see their impact.

Example: Comparing 3 sales plans:
| Scenario | Price | Quantity | Revenue Formula |
|-----------|--------|-----------|-----------------|
| Best Case | 120 | 500 | =120*500 |
| Average Case | 100 | 450 | =100*450 |
| Worst Case | 80 | 400 | =80*400 |

Steps:
1. Go to Data → What-If Analysis → Scenario Manager
2. Click Add to create each scenario (Best, Average, Worst)
3. Enter input cells and values.
4. Click Show to view results.
5. Use Summary to create a comparison report.

Excel generates a Scenario Summary table automatically.

---

### C. Data Tables
Used when you want to see how changing one or two variables affects the result of a formula.

Example:
You want to see how different interest rates and years affect total investment return.

Formula:
```
=Principal * (1 + Rate)^Years
```

Steps for One-Variable Table:
1. Write formula in one cell.
2. List different Rate values below or beside it.
3. Select the range → Go to Data → What-If Analysis → Data Table
4. In Column Input Cell, select the rate cell.
5. Press OK.

Steps for Two-Variable Table:
- Add different Rates (rows) and Years (columns)
- Use Row Input Cell for Years and Column Input Cell for Rate

Excel instantly generates all combinations and results.

---

## 3. Real-Life Example
Case Study: Loan Repayment
You want to know how changing interest rates or loan tenure affects EMI.

Formula:
```
=PMT(Interest Rate/12, Loan Term*12, -Loan Amount)
```
Use Data Table to test:
- Interest rates from 7% to 12%
- Tenures from 5 to 10 years

Get instant comparison of EMI values.

---

## 4. Classroom / Lab Activity
Activity 1 – Goal Seek:
Find what sales quantity is required to achieve ₹1,00,000 profit when:
- Selling price = ₹500
- Cost per unit = ₹300
- Formula: `=Quantity*(Price - Cost)`

Activity 2 – Scenario Manager:
Compare 3 business expansion plans with different investment and expected returns.

Activity 3 – Data Table:
Test how changing discount % or number of units affects total revenue.

---

## 5. Summary
| Tool | Purpose | Best Used When |
|------|----------|----------------|
| Goal Seek | Find input for a known output | One variable only |
| Scenario Manager | Compare multiple “what-if” cases | Multiple inputs |
| Data Table | View effects of variable changes | 1 or 2 variables |

---

## 6. Homework / Practice Task
Create a What-If Analysis workbook for:
"Company Profit Projection for Next Year"
- Use Goal Seek to find required sales for ₹5L profit
- Use Scenario Manager for different cost assumptions
- Use Data Table to analyze price vs quantity impact
