# **Lecture 13: Data Modeling & Relationships in Power BI**

## **Theory**

### **1. Star & Snowflake Schema**

* **Star Schema**

  * Centered around a **Fact Table**.
  * Surrounded by **Dimension Tables**.
  * Simple, efficient, preferred for Power BI.

* **Snowflake Schema**

  * Dimensions further split into sub-dimensions.
  * More normalized structure.
  * Slightly more complex relationships.

---

### **2. Fact vs Dimension Tables**

* **Fact Table**

  * Stores transactions, numerical values, metrics.
  * Examples: Sales, Orders, Payments.
  * Columns: Quantities, Prices, Revenue, Profit.

* **Dimension Table**

  * Stores descriptive/contextual information.
  * Examples: Customers, Products, Calendar.
  * Columns: Names, Categories, Segments.

---

### **3. Creating & Managing Relationships**

* Importance of **Primary Key (PK)** and **Foreign Key (FK)**.
* Star Schema relationship:

  * Dimension (PK) → Fact (FK)
* Manage using Power BI:

  * **Manage Relationships** window
  * Create, edit, delete relationships
  * View in **Model View**

---

### **4. Cardinality & Cross-Filter Direction**

* **Cardinality Types**

  * One-to-Many (1:*): Most common (Dimension → Fact)
  * One-to-One (1:1): Rare
  * Many-to-Many (*:*): Avoid unless necessary

* **Cross Filter Direction**

  * **Single**: Preferred for Star Schema
  * **Both**: Use carefully; may create ambiguous paths

---

## **Practical Examples**

### **Example 1: Building a Star Schema**

Tables:

* FactSales (Sales Data)
* DimCustomers
* DimProducts
* DimDate

Steps:

1. Import all tables.
2. Identify Keys:

   * DimCustomer.CustomerID → FactSales.CustomerID
   * DimProducts.ProductID → FactSales.ProductID
   * DimDate.Date → FactSales.OrderDate
3. Create relationships in Power BI Model View.

---

### **Example 2: Checking Cardinality**

* CustomerID appears once in Customers table.
* CustomerID repeats many times in Sales table.
* Result → One-to-Many relationship.

---

### **Example 3: Cross Filter Direction Use Case**

Scenario: You want a slicer to filter multiple dimensions.

* In most cases, keep **Single Direction**.
* Enable **Both Direction** only if justified.

---

## **Practice Tasks**

### **Task 1: Build a Star Schema**

Using the provided datasets:

* Create **FactSales**
* Create **DimCustomers**
* Add a **DimDate** table
* Build relationships accordingly.

### **Task 2: Identify PK & FK**

Find keys for:

* Sales
* Customers
* Products

### **Task 3: Analyze Cardinality**

Check if each relationship is:

* 1:* or *:* or 1:1

### **Task 4: Create a Snowflake Schema**

Split Customer table into:

* Customer Basic Info
* Customer Category Info

Then connect it to the model.

### **Task 5: Build a Report**

Create visuals:

* Sales by Region
* Sales by Customer Category
* Top 10 Products
* Date Hierarchy Analysis (Year → Month → Day)
