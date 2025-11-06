
#  PowerPivot with Real-World Sales & Product Data

##  Session Overview

**Objective:**
Students will learn to:
1. Import multiple datasets into PowerPivot  
2. Create data relationships  
3. Build measures using DAX  
4. Design KPIs  
5. Analyze performance using PivotTables & Slicers  

**Files Used:**
- `SalesData.xlsx`
- `ProductData.xlsx`  
(Common Key: **ProductID**)

---

## 1. Introduction to PowerPivot

### What is PowerPivot?
PowerPivot is an Excel add-in that lets you:
- Import and model **large data** from multiple sources.
- Build **relationships** between tables (like databases).
- Use **DAX formulas** for advanced calculations.
- Create **interactive dashboards** directly in Excel.

### Example Use Case:
You have two datasets:
- **Sales Data:** Transaction-level details (Orders, Quantity, Sales, Profit)
- **Product Data:** Master info about each product (Name, Category, Price)

Goal → Connect both and analyze:  
> “Which category or region generates the most profit?”

---

## 2. Enabling PowerPivot

1. Open Excel → **File → Options → Add-ins**  
2. Choose **COM Add-ins** → Click **Go**  
3. Check **Microsoft PowerPivot for Excel** → Click **OK**

A new **PowerPivot** tab appears on the Ribbon.

---

## 3. Importing Data into PowerPivot

### Step-by-Step:
1. Open a new Excel file.  
2. Go to **PowerPivot → Manage → Home → Get External Data → From Other Sources**  
3. Choose **Excel File → Browse → SalesData.xlsx**  
4. Tick the **table** → Check “Add this data to Data Model” → Finish.  
5. Repeat for **ProductData.xlsx**.

 Both tables are now added to the **Data Model**.

---

## 4. Creating Relationships

### Why?
PowerPivot needs to link tables to combine information.

### Steps:
1. In PowerPivot → Click **Diagram View**  
2. Drag **ProductID** from `SalesData` → **ProductID** in `ProductData`

 One-to-Many Relationship: One Product → Many Sales

---

## 5. Creating Measures using DAX

**DAX (Data Analysis Expressions)** = Excel formulas for PowerPivot.

### Example Measures:

| Measure Name | Formula | Meaning |
|---------------|----------|---------|
| Total Sales | `=SUM(SalesData[Sales])` | Total Sales |
| Total Profit | `=SUM(SalesData[Profit])` | Total Profit |
| Total Quantity | `=SUM(SalesData[Quantity])` | Quantity Sold |
| Profit Margin | `=DIVIDE([Total Profit], [Total Sales])` | Profit % |
| Average Order Value | `=DIVIDE([Total Sales], COUNTROWS(SalesData))` | Avg Sales per Order |

### Optional DAX:
```DAX
Sales by Category = CALCULATE([Total Sales], VALUES(ProductData[Category]))
High Margin Sales = CALCULATE([Total Sales], FILTER(SalesData, [Profit Margin] > 0.15))
```

---

## 6. Creating KPI in PowerPivot

### Example: Profit Margin KPI
1. Right-click on `Profit Margin` → **Create KPI**  
2. **Target Value:** `0.15` (15%)  
3. **Status Icons:** Traffic Lights  
   - Green: ≥ 15%  
   - Yellow: 10–15%  
   - Red: < 10%  
4. Click OK

 KPI indicator appears in PivotTable.

---

## 7. Create PivotTable Report

### Steps:
1. **Insert → PivotTable → Use This Workbook’s Data Model**  
2. Add:
   - Rows → `ProductData[Category]`  
   - Values → `Total Sales`, `Profit Margin (KPI)`  
3. Add **Slicer** for `Region` or `Customer`.

 Interactive Dashboard:
- Compare sales & profit by category and region.
- Identify underperforming categories using KPI color codes.

---

## 8. Dashboard Enhancement

Enhance the dashboard using:
- **Conditional Formatting** for heatmaps  
- **Slicers** for Region, Year, Category  
- **Bar or Column Charts**  
- **Card visuals** for KPIs

---

## 9. Practice Tasks for Students

### Task 1: Data Modeling
- Import both datasets into PowerPivot.  
- Create relationship on **ProductID**.

### Task 2: Create Measures
- Total Sales  
- Total Profit  
- Profit Margin  
- Total Quantity  
- Average Order Value  

### Task 3: Create KPI
- Target margin = 15%  
- Add KPI for Profit Margin

### Task 4: Build Dashboard
- PivotTable showing Category vs Region  
- Add KPI icons & slicers

---

##  Summary

 You learned:
- How to link multiple tables in PowerPivot  
- How to use DAX for advanced calculations  
- How to create KPI indicators  
- How to build interactive dashboards

---

## 📁 Optional Extensions

**Add a Date Table** for time intelligence (Yearly/Monthly trends).

**Example: Sales Growth %**
```DAX
Sales Growth % =
DIVIDE(
    [Total Sales] - CALCULATE([Total Sales], PREVIOUSYEAR('SalesData'[OrderDate])),
    CALCULATE([Total Sales], PREVIOUSYEAR('SalesData'[OrderDate]))
)
```
