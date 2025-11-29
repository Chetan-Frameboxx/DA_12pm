# Excel Lookup Functions Explained

## 1. VLOOKUP

Vertical Lookup – searches for a value in the first column of a table and returns a value from another column in the same row.

### Syntax

```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

### Parameters

* **lookup_value**: value you want to find
* **table_array**: table to search
* **col_index_num**: column number to return value from
* **range_lookup**: TRUE (approx.) or FALSE (exact)

### Example

**Table:**

| A   | B     |
| --- | ----- |
| ID  | Name  |
| 101 | Rahul |
| 102 | Sneha |

**Formula:**

```
=VLOOKUP(102, A2:B4, 2, FALSE)
```

**Result → Sneha**

### Limitations

* Must search the first column only
* Cannot look left side
* Slower on large datasets

---

## 2. HLOOKUP

Horizontal Lookup – checks for a value in the first row and returns a value from a specific row below it.

### Syntax

```
=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])
```

### Example

**Row:**

| A    | B     | C     |
| ---- | ----- | ----- |
| ID   | 101   | 102   |
| Name | Rahul | Sneha |

**Formula:**

```
=HLOOKUP("Name", A1:C2, 2, FALSE)
```

**Result → Rahul**

### Limitations

* Only works horizontally
* First row must contain lookup value

---

## 3. XLOOKUP (Modern, Most Powerful)

Replacement for VLOOKUP & HLOOKUP.

### Syntax

```
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```

### Why XLOOKUP is better

* Can look left, right, up, down
* No need for column numbers
* Exact match by default
* Can return multiple values

### Example

```
=XLOOKUP(102, A2:A4, B2:B4)
```

**Result → Sneha**

### Extra Features

* Wildcard searching
* Reverse search (bottom to top)
* Can return entire row or column

---

## 4. INDEX + MATCH (Traditional but powerful)

A combination used before XLOOKUP existed. Equivalent or better than VLOOKUP.

### MATCH Function

Finds the row/column number of a value.

**Syntax:**

```
=MATCH(lookup_value, lookup_array, [match_type])
```

### INDEX Function

Returns a value from a specific row and column.

**Syntax:**

```
=INDEX(return_range, row_num, [column_num])
```

### Combined (INDEX–MATCH)

```
=INDEX(return_range, MATCH(lookup_value, lookup_array, 0))
```

### Example

```
=INDEX(B2:B4, MATCH(102, A2:A4, 0))
```

**Result → Sneha**

### Advantages

* Can look left
* Very fast
* More flexible than VLOOKUP

---

## When to Use What?

| Function      | Direction | Best Use                 |
| ------------- | --------- | ------------------------ |
| VLOOKUP       | Downwards | Simple vertical lookup   |
| HLOOKUP       | Across    | Simple horizontal lookup |
| XLOOKUP       | Any       | Modern, most flexible    |
| INDEX + MATCH | Any       | Advanced control, faster |
