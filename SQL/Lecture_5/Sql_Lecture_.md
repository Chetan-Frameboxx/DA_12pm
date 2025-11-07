# Lecture 6: SQL Clauses & Aggregate Functions

---

## 1 THEORY

### 1. GROUP BY Clause

Used to **group rows** that have the same values into summary rows (e.g., total marks per course).

**Syntax:**

```sql
SELECT column, AGGREGATE_FUNCTION(column)
FROM table_name
GROUP BY column;
```

---

### 2. HAVING Clause

Works like `WHERE`, but is used **after GROUP BY** to filter aggregated results.

```sql
SELECT course, AVG(marks)
FROM students
GROUP BY course
HAVING AVG(marks) > 70;
```

---

### 3. LIMIT Clause (MySQL Specific)

Used to limit the number of records returned.

```sql
SELECT * FROM students LIMIT 5;
```

---

### 4. IN Clause

Filters data that matches **any value** in a given list.

```sql
SELECT * FROM students
WHERE course IN ('BCA', 'MCA');
```

---

### 5. BETWEEN Clause

Filters records within a given range.

```sql
SELECT * FROM students
WHERE marks BETWEEN 60 AND 90;
```

---

### 6. LIKE Clause

Performs pattern matching using `%` (any number of characters) and `_` (single character).

```sql
SELECT * FROM students
WHERE name LIKE 'A%';
```

---

### 7. Aggregate Functions

| Function | Description        | Example                          |
| -------- | ------------------ | -------------------------------- |
| COUNT()  | Counts rows        | SELECT COUNT(*) FROM students;   |
| SUM()    | Adds values        | SELECT SUM(marks) FROM students; |
| AVG()    | Calculates average | SELECT AVG(marks) FROM students; |
| MAX()    | Highest value      | SELECT MAX(marks) FROM students; |
| MIN()    | Lowest value       | SELECT MIN(marks) FROM students; |

---

### 8. SQL Command Execution Order

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT

---

## 2 PRACTICAL EXAMPLES (FULL PROGRAMS)

### Example 1 – GROUP BY

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  course VARCHAR(20),
  marks INT
);

INSERT INTO students VALUES
(1, 'Aman', 'BCA', 75),
(2, 'Neha', 'MCA', 90),
(3, 'Karan', 'BCA', 65),
(4, 'Riya', 'BBA', 80),
(5, 'Meena', 'MCA', 88);

-- Average marks per course
SELECT course, AVG(marks) AS average_marks
FROM students
GROUP BY course;
```

---

### Example 2 – HAVING

```sql
-- Courses where average marks > 70
SELECT course, AVG(marks) AS avg_marks
FROM students
GROUP BY course
HAVING AVG(marks) > 70;
```

---

### Example 3 – LIMIT

```sql
-- Top 3 students by marks
SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 3;
```

---

### Example 4 – IN and BETWEEN

```sql
-- Students in BCA or MCA with marks between 70 and 90
SELECT * FROM students
WHERE course IN ('BCA', 'MCA')
AND marks BETWEEN 70 AND 90;
```

---

### Example 5 – Aggregate Functions

```sql
-- Summary of student marks
SELECT 
  COUNT(*) AS total_students,
  SUM(marks) AS total_marks,
  AVG(marks) AS average_marks,
  MAX(marks) AS highest_marks,
  MIN(marks) AS lowest_marks
FROM students;
```

---

## 3 PRACTICE TASKS (FOR STUDENTS)

1. Count the total number of students in the table.
2. Display the highest and lowest marks.
3. Show total marks obtained by students in each course.
4. Display the average marks per course using GROUP BY.
5. Show only those courses whose average marks exceed 80 using HAVING.
6. Display the top 2 scoring students using ORDER BY and LIMIT.
7. Show all students whose marks are between 60 and 90.
8. Display all students enrolled in BCA or MCA using IN.
9. Find the total number of unique courses (COUNT(DISTINCT course)).
10. Display names of students whose names start with ‘N’ using LIKE.
