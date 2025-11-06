# Lecture 4: Filtering, Sorting, Updating & Deleting Data
---

## 1 THEORY

### Filtering Data using WHERE Clause
The `WHERE` clause filters rows based on given conditions.
It helps you show only the data that meets your criteria.

**Syntax:**
```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

---

### Comparison Operators

| Operator | Description | Example |
|-----------|-------------|----------|
| = | Equal to | `marks = 80` |
| > | Greater than | `marks > 75` |
| < | Less than | `marks < 50` |
| BETWEEN | Between two values | `marks BETWEEN 60 AND 90` |
| LIKE | Pattern matching | `name LIKE 'A%'` |
| <> or != | Not equal to | `course <> 'BBA'` |

---

### Sorting Data using ORDER BY
Used to sort data in ascending (`ASC`) or descending (`DESC`) order.  
By default, it sorts in ascending order.

**Syntax:**
```sql
SELECT column1, column2
FROM table_name
ORDER BY column_name ASC|DESC;
```

---

### UPDATE Command
Used to modify existing data in a table.  
Always use a `WHERE` clause to avoid updating all records.

**Syntax:**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

---

### DELETE Command
Used to remove records from a table.  
Without `WHERE`, all data in the table will be deleted.

**Syntax:**
```sql
DELETE FROM table_name
WHERE condition;
```

---

## 2 PRACTICAL EXAMPLES (FULL PROGRAMS)

Each program starts from table creation for clarity and safety.

---

### Example 1 – Filtering with WHERE Clause
```sql
-- Step 1: Create Table
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  course VARCHAR(30),
  marks INT
);

-- Step 2: Insert Sample Data
INSERT INTO students (id, name, course, marks) VALUES
(1, 'Aman', 'BCA', 78),
(2, 'Neha', 'MCA', 90),
(3, 'Riya', 'BBA', 62),
(4, 'Karan', 'BCA', 55),
(5, 'Meena', 'MCA', 88);

-- Step 3: Filter Students with Marks > 70
SELECT * 
FROM students
WHERE marks > 70;
```

---

### Example 2 – Sorting Data
```sql
-- Sort Students by Marks in Descending Order
SELECT name, course, marks
FROM students
ORDER BY marks DESC;
```

---

### Example 3 – Filtering + Sorting Combined
```sql
-- Display Only BCA Students, Sorted by Marks (Lowest to Highest)
SELECT name, marks
FROM students
WHERE course = 'BCA'
ORDER BY marks ASC;
```

---

### Example 4 – Updating Data
```sql
-- Update Marks of a Specific Student
UPDATE students
SET marks = 95
WHERE name = 'Neha';

-- Verify Update
SELECT * FROM students WHERE name = 'Neha';
```

---

### Example 5 – Deleting a Record
```sql
-- Delete a Student Record
DELETE FROM students
WHERE id = 4;

-- Verify Deletion
SELECT * FROM students;
```

---

## 3 PRACTICE TASKS

1. Display all students who have marks greater than 70.  
2. Show names and courses of students enrolled in BCA.  
3. Display all students whose names start with the letter ‘A’.  
4. List students whose marks are between 60 and 90.  
5. Show all students except those in the BBA course.  
6. Display student names and marks, sorted by marks in descending order.  
7. Display all students whose course name ends with “A”.  
8. Update marks of a student named ‘Riya’ to 85.  
9. Delete the student record whose id = 5.  
10. Show all students with marks greater than 60 and order them by name (A–Z).
