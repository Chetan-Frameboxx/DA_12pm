# Lecture 3: Measures of Dispersion & Data Distribution

---

## Theory

### 1. What are Measures of Dispersion?

Measures of dispersion describe **how spread out or scattered** the data values are around a central value.

While measures of central tendency tell us *where the center is*, measures of dispersion tell us:

> *How much the data varies from the center.*

Why dispersion matters:

* Two datasets can have the same mean but very different variability
* Helps assess **risk, consistency, and stability** in data

---

### 2. Range

#### Definition

The **range** is the difference between the maximum and minimum values in a dataset.

#### Formula

Range = Maximum value − Minimum value

#### Characteristics

* Simple to calculate
* Highly sensitive to outliers
* Does not describe overall spread well

#### Example

Dataset: 10, 20, 30, 40, 50
Range = 50 − 10 = 40

---

### 3. Variance

#### Definition

Variance measures the **average squared deviation** of each data value from the mean.

#### Concept (Simplified)

* Find the mean
* Subtract mean from each value
* Square the differences
* Take the average

#### Key Points

* Variance is always non-negative
* Units are **squared**, which can be hard to interpret
* Used as a base for standard deviation

#### Interpretation

Higher variance → data is more spread out

---

### 4. Standard Deviation

#### Definition

Standard deviation is the **square root of variance** and measures average distance of data points from the mean.

#### Why Standard Deviation is Preferred

* Same unit as original data
* Easy to interpret
* Widely used in business and analytics

#### Interpretation

* Low SD → data points are close to the mean (consistent)
* High SD → data points are far from the mean (volatile)

---

### 5. Frequency Distribution

#### Definition

A **frequency distribution** summarizes data by showing how often each value or group of values occurs.

#### Types

* Ungrouped frequency distribution
* Grouped frequency distribution (class intervals)

#### Benefits

* Simplifies large datasets
* Helps visualize distribution patterns
* Forms the base for histograms and charts

---

### 6. Normal Distribution

#### Definition

A **normal distribution** is a symmetric, bell-shaped distribution where:

* Mean = Median = Mode
* Most values lie near the center

#### Characteristics

* Symmetrical around the mean
* Predictable pattern
* Common in natural and business data

Examples:

* Heights of people
* Test scores
* Measurement errors

---

### 7. Skewness

Skewness describes the **asymmetry** of a data distribution.

#### 7.1 Positive Skewness (Right-Skewed)

* Long tail on the right side
* Mean > Median > Mode

Examples:

* Income distribution
* Property prices

---

#### 7.2 Negative Skewness (Left-Skewed)

* Long tail on the left side
* Mean < Median < Mode

Examples:

* Easy exam scores
* Employee performance ratings

---

### 8. Outliers and Their Impact

#### Definition

An **outlier** is an extreme value that deviates significantly from other data points.

#### Impact of Outliers

* Increases range and standard deviation
* Distorts mean
* Can mislead analysis if not handled properly

Common causes:

* Data entry errors
* Rare events
* Exceptional cases

---

## Practical Examples (Full Scenarios)

### Example 1: Comparing Two Datasets

Dataset A: 48, 49, 50, 51, 52
Dataset B: 10, 30, 50, 70, 90

* Both have the same mean
* Dataset B has higher range and standard deviation

Conclusion: Dataset B is more variable

---

### Example 2: Salary Distribution

Salaries (₹): 20,000, 25,000, 30,000, 35,000, 2,00,000

* Range and SD are very high
* Mean is misleading
* Distribution is positively skewed

Correct analysis focuses on:

* Median salary
* Identifying outlier impact

---

## Practice Tasks

### Task 1: Range Calculation

Find the range:

* 5, 12, 18, 25, 40

---

### Task 2: Variability Comparison

Two classes have the same average marks.
Why can their standard deviation be different?

---

### Task 3: Identify Distribution Type

Classify the following as normal, positively skewed, or negatively skewed:

1. Income data
2. Heights of students
3. Marks in a very easy exam

---

### Task 4: Outlier Analysis

Dataset: 15, 18, 20, 22, 100

* Identify the outlier
* Explain its impact on mean and standard deviation

---

### Task 5: Real-World Application

Choose any dataset and:

* Identify range
* Comment on variability
* Describe the distribution shape

---

## Learning Outcomes (Revisited)

By the end of this lecture, you should be able to:

* Measure data variability using range and standard deviation
* Understand frequency and normal distribution
* Identify skewness and outliers
* Interpret spread and distribution patterns in real-world data

---

