# Lecture 2 – Creating First Program in SQL & Data Types

## 1. Creating First Program in SQL

### Objective
To understand how to write and execute basic SQL commands using SQL Workbench or any SQL environment (like MySQL, PostgreSQL, or SQL Server).

---

### Step 1: Create a Database

```sql
CREATE DATABASE SchoolDB;
```

- **CREATE DATABASE** → Command to create a new database.
- **SchoolDB** → Name of the database.

**Use the Database:**
```sql
USE SchoolDB;
```

---

### Step 2: Create a Table

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50),
    Age INT,
    Course VARCHAR(50),
    Marks DECIMAL(5,2)
);
```

**Explanation:**
- **StudentID** → Integer value that uniquely identifies each student.
- **PRIMARY KEY** → Ensures each record has a unique ID.
- **VARCHAR(50)** → Used for text data, max 50 characters.
- **DECIMAL(5,2)** → Numeric value with 5 total digits and 2 decimal places.

---

### Step 3: Insert Data

```sql
INSERT INTO Students (StudentID, StudentName, Age, Course, Marks)
VALUES 
(1, 'Amit Sharma', 21, 'Data Analytics', 85.50),
(2, 'Neha Gupta', 22, 'Computer Science', 90.75),
(3, 'Ravi Singh', 20, 'Business Analytics', 78.25);
```

---

### Step 4: View Data

```sql
SELECT * FROM Students;
```

| StudentID | StudentName | Age | Course | Marks |
|------------|--------------|-----|---------|--------|
| 1 | Amit Sharma | 21 | Data Analytics | 85.50 |
| 2 | Neha Gupta | 22 | Computer Science | 90.75 |
| 3 | Ravi Singh | 20 | Business Analytics | 78.25 |

---

## 2. SQL Data Types

### A. Numeric Data Types

| Data Type | Description | Example |
|------------|--------------|----------|
| **INT** | Whole numbers | 10, 25 |
| **BIGINT** | Large integers | 9999999999 |
| **DECIMAL(p,s)** | Fixed point number with precision | 12.34 |
| **FLOAT** | Floating-point numbers | 3.14159 |
| **BIT** | Boolean value (0 or 1) | 1 |

---

### B. String (Character) Data Types

| Data Type | Description | Example |
|------------|--------------|----------|
| **CHAR(n)** | Fixed-length string | ‘ABC’ |
| **VARCHAR(n)** | Variable-length string | ‘John’ |
| **TEXT** | Large text data | Paragraphs or descriptions |

---

### C. Date and Time Data Types

| Data Type | Description | Example |
|------------|--------------|----------|
| **DATE** | Stores date only | '2025-11-04' |
| **TIME** | Stores time only | '10:30:00' |
| **DATETIME** | Stores both date and time | '2025-11-04 10:30:00' |
| **TIMESTAMP** | Stores date/time with auto-update | '2025-11-04 10:30:00' |

---

### D. Other Common Data Types

| Data Type | Description |
|------------|--------------|
| **BOOLEAN** | True or False |
| **BLOB** | Binary data (images, files) |
| **JSON** | Stores JSON formatted data (in modern SQL engines) |

---

### Example Table with Different Data Types

```sql
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(100),
    Salary DECIMAL(10,2),
    JoiningDate DATE,
    IsActive BOOLEAN
);
```

---

### Summary

- Always create a database before creating tables.  
- Choose the **right data type** for each column to optimize storage and accuracy.  
- Basic workflow:  
  **CREATE DATABASE → CREATE TABLE → INSERT → SELECT → UPDATE → DELETE**
