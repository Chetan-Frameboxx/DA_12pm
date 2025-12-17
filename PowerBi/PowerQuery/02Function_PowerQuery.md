# Lecture 10: Power Query Functions

## Theory

### 1. Text Functions

Power Query provides several built-in text functions to clean and transform string data.

**Common Text Functions:**

* **Text.Trim()** – Removes leading and trailing spaces.
* **Text.Clean()** – Removes non-printable characters.
* **Text.Replace()** – Replaces a substring inside text.
* **Text.Split()** – Splits text based on a delimiter.
* **Text.Combine()** – Concatenates a list of text values.
* **Text.Upper() / Text.Lower()** – Converts case.

---

### 2. Date Functions

Date functions help extract, format, and manipulate date values.

**Common Date Functions:**

* **Date.Year() / Date.Month() / Date.Day()** – Extract date components.
* **Date.AddDays()** – Add or subtract days.
* **Date.AddMonths() / Date.AddYears()** – Date arithmetic.
* **Date.Difference()** – Calculate difference between two dates.
* **Date.ToText()** – Convert date to formatted text.

---

### 3. Number Functions

Number functions are used for rounding, formatting, and performing calculations.

**Common Number Functions:**

* **Number.Round()** – Round to nearest value.
* **Number.RoundUp() / Number.RoundDown()** – Control rounding direction.
* **Number.Abs()** – Get absolute value.
* **Number.Divide()** – Safe division.
* **Number.FromText()** – Convert text into number.

---

## Practical Examples (Full Power Query Code)

### 1. Text Function Examples

```m
// Remove extra spaces
Text.Trim("   Power BI   ")

// Replace text
Text.Replace("Power BI Desktop", "Desktop", "Service")

// Split text
Text.Split("John,Doe,Manager", ",")

// Concatenate list of values
Text.Combine({"Power", "Query", "Functions"}, " ")
```

---

### 2. Date Function Examples

```m
// Extract year
Date.Year(#date(2025, 12, 11))

// Add 10 days
date = Date.AddDays(#date(2025, 12, 11), 10)

// Difference between dates
Date.Difference(#date(2025, 12, 11), #date(2025, 10, 01))

// Convert date to text
Date.ToText(#date(2025, 12, 11), "dd-MM-yyyy")
```

---

### 3. Number Function Examples

```m
// Round number
Number.Round(12.786, 2)

// Absolute value
Number.Abs(-55)

// Safe division
Number.Divide(100, 0)   // returns null instead of error
```

---

## Practice Tasks

### Text Tasks

1. Given a column "Full Name", split into First Name and Last Name.
2. Remove all leading and trailing spaces from a Product Name column.
3. Replace the word "Old" with "New" in a Description column.
4. Convert email IDs to lowercase.
5. Concatenate City and Country into a single location column.

---

### Date Tasks

1. Extract Year, Month, and Day from an OrderDate column.
2. Calculate the number of days between OrderDate and ShipDate.
3. Add 30 days to all dates in a Date column.
4. Convert all dates into DD/MM/YYYY format.
5. Create a new column showing the Quarter of each date.

---

### Number Tasks

1. Round Sales Amount to 2 decimal places.
2. Return the absolute value of Profit.
3. Divide TotalSales by Quantity (avoid division errors).
4. Convert a Text column ("1000") into a Number column.
5. Create a new column showing Discount Percentage = (Discount / Price).

---

