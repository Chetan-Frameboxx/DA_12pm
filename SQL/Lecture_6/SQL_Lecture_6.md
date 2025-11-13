## Lecture 7: SQL Joins

### SQL for Data Analysts (MySQL)

---

##  Base Tables for Joins

Before learning about JOINs, let’s create two simple tables that we will use in all examples.

```sql
CREATE DATABASE analytics_demo;
USE analytics_demo;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT,
  product VARCHAR(50),
  amount DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (name, city) VALUES
('Rohan', 'Mumbai'),
('Priya', 'Delhi'),
('Karan', 'Pune'),
('Neha', 'Chennai');

INSERT INTO orders (customer_id, product, amount) VALUES
(1, 'Laptop', 50000),
(3, 'Mobile', 20000),
(1, 'Mouse', 1500),
(5, 'Headphones', 3000);
```

---

##  Theory

###  What is a JOIN?

A **JOIN** in SQL is used to combine data from **two or more tables** based on a related column between them — usually a **primary key** in one table and a **foreign key** in another.

Example:
If you have a **Customers** table and an **Orders** table, you can join them using the `customer_id` column that appears in both.

---

###  Why Analysts Use Joins

* To connect information stored in multiple tables (e.g., sales, products, customers).
* To create unified reports from relational datasets.
* To avoid data duplication and keep databases normalized.

---

###  Types of SQL Joins

#### 1. **INNER JOIN**

Returns only matching records from both tables.

```sql
SELECT customers.customer_id, customers.name, orders.order_id, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

**Result:** Only customers who placed at least one order.

---

#### 2. **LEFT JOIN (LEFT OUTER JOIN)**

Returns all records from the **left table**, and the matching ones from the right table.

```sql
SELECT customers.name, orders.order_id, orders.amount
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;
```

**Result:** All customers, even those without orders (with NULL in order columns).

---

#### 3. **RIGHT JOIN (RIGHT OUTER JOIN)**

Returns all records from the **right table**, and the matching ones from the left table.

```sql
SELECT customers.name, orders.order_id, orders.amount
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;
```

**Result:** All orders, even if their customer record is missing.

---

#### 4. **FULL JOIN (FULL OUTER JOIN)**

Returns all records when there is a match in **either** left or right table.

>  MySQL doesn’t support FULL JOIN directly — you can simulate it using `UNION`.

```sql
SELECT customers.name, orders.order_id, orders.amount
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
UNION
SELECT customers.name, orders.order_id, orders.amount
FROM customers
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
```

---

###  Joining Multiple Tables

You can join more than two tables in a single query.

```sql
SELECT customers.name, orders.order_id, products.product_name, orders.amount
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id
INNER JOIN products ON orders.product_id = products.product_id;
```

**Result:** Combines customer info, order details, and product names together.

---

###  Real-World Data Joining Example (Sales + Customers)

Imagine two tables:

**customers**

| customer_id | name  | city    |
| ----------- | ----- | ------- |
| 1           | Rohan | Mumbai  |
| 2           | Priya | Delhi   |
| 3           | Karan | Pune    |
| 4           | Neha  | Chennai |

**orders**

| order_id | customer_id | product    | amount |
| -------- | ----------- | ---------- | ------ |
| 101      | 1           | Laptop     | 50000  |
| 102      | 3           | Mobile     | 20000  |
| 103      | 1           | Mouse      | 1500   |
| 104      | 5           | Headphones | 3000   |

Query:

```sql
SELECT customers.name, customers.city, orders.product, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

**Output:** Returns only customers who made purchases (Rohan and Karan).

---

##  Practical Example (Full Program)

```sql
CREATE DATABASE analytics_demo;
USE analytics_demo;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT,
  product VARCHAR(50),
  amount DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (name, city) VALUES
('Rohan', 'Mumbai'),
('Priya', 'Delhi'),
('Karan', 'Pune'),
('Neha', 'Chennai');

INSERT INTO orders (customer_id, product, amount) VALUES
(1, 'Laptop', 50000),
(3, 'Mobile', 20000),
(1, 'Mouse', 1500),
(5, 'Headphones', 3000);

SELECT c.name, c.city, o.product, o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;
```

---

##  Practice Tasks 

1. Create two tables: `employees` and `departments`.
2. Insert sample data for 4 employees and 2 departments.
3. Write a query using **INNER JOIN** to list employee names with their department names.
4. Write a **LEFT JOIN** to show all departments, even if they have no employees.
5. Write a **RIGHT JOIN** to show all employees, even if their department ID is missing.
6. Simulate a **FULL JOIN** between both tables using `UNION`.
7. Create a third table `projects` and perform a **multi-table JOIN** among all three tables.

---

