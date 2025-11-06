# Lecture 4: Table Modification & Relationships

### 1 THEORY

#### 1. FOREIGN KEY

A Foreign Key links two tables together. It ensures data consistency
between a Parent Table (Primary Key) and a Child Table (Foreign Key).

**Example:**

``` sql
CREATE TABLE marks (
  mark_id INT PRIMARY KEY,
  student_id INT,
  marks INT,
  FOREIGN KEY (student_id) REFERENCES students(id)
);
```

#### 2. ALTER TABLE Command

Used to modify the structure of an existing table.

**ADD Column**

``` sql
ALTER TABLE students
ADD email VARCHAR(50);
```

**MODIFY Data Type**

``` sql
ALTER TABLE students
MODIFY marks FLOAT;
```

**RENAME Column**

``` sql
ALTER TABLE students
RENAME COLUMN course TO course_name;
```

**DROP Column**

``` sql
ALTER TABLE students
DROP COLUMN email;
```

#### 3. RENAME Table

Used to rename an existing table.

``` sql
RENAME TABLE students TO student_info;
```

#### 4. TRUNCATE Command

Used to remove all rows from a table but keep the structure.

``` sql
TRUNCATE TABLE students;
```

#### 5. DROP Table

Used to delete a table and all its data permanently.

``` sql
DROP TABLE students;
```

#### 6. CASCADE

When using FOREIGN KEY with ON DELETE CASCADE, deleting a parent row
automatically deletes matching child rows.

**Example:**

``` sql
CREATE TABLE marks (
  mark_id INT PRIMARY KEY,
  student_id INT,
  marks INT,
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);
```

------------------------------------------------------------------------

### 2 PRACTICAL EXAMPLES (FULL PROGRAMS)

**Example 1 -- Create Foreign Key Relationship**

``` sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  course VARCHAR(30)
);

CREATE TABLE marks (
  mark_id INT PRIMARY KEY,
  student_id INT,
  marks INT,
  FOREIGN KEY (student_id) REFERENCES students(id)
);
```

**Example 2 -- Add a New Column**

``` sql
ALTER TABLE students
ADD email VARCHAR(100);
```

**Example 3 -- Modify Data Type**

``` sql
ALTER TABLE students
MODIFY course VARCHAR(50);
```

**Example 4 -- Rename a Column**

``` sql
ALTER TABLE students
RENAME COLUMN course TO course_name;
```

**Example 5 -- Drop a Column**

``` sql
ALTER TABLE students
DROP COLUMN email;
```

**Example 6 -- Rename Table**

``` sql
RENAME TABLE students TO student_info;
```

**Example 7 -- TRUNCATE vs DROP**

``` sql
-- Remove all rows but keep table
TRUNCATE TABLE student_info;

-- Delete table permanently
DROP TABLE student_info;
```

**Example 8 -- Cascade Delete**

``` sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50)
);

CREATE TABLE marks (
  mark_id INT PRIMARY KEY,
  student_id INT,
  marks INT,
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

-- Inserting data
INSERT INTO students VALUES (1, 'Aman'), (2, 'Neha');
INSERT INTO marks VALUES (101, 1, 85), (102, 2, 90);

-- Delete parent row and observe cascade effect
DELETE FROM students WHERE id = 1;

SELECT * FROM marks;  -- Record for student_id 1 is also deleted
```

------------------------------------------------------------------------

### 3 PRACTICE TASKS

1.  Create a table `teachers` with `teacher_id`, `name`, and `subject`.
2.  Add a column `email` to `teachers`.
3.  Modify the `subject` column to increase its length.
4.  Rename column `subject` to `subject_name`.
5.  Drop the `email` column from `teachers`.
6.  Rename table `teachers` to `faculty`.
7.  Create `faculty_salary` table with a FOREIGN KEY referencing
    `faculty`.
8.  Add `ON DELETE CASCADE` and test by deleting one faculty.
9.  Use `TRUNCATE` on `faculty_salary`.
10. Use `DROP TABLE` to remove both tables.
