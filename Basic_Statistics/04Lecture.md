# Lecture 4: Probability & Correlation

---

## Theory

### 1. Basics of Probability

**Probability** measures the likelihood or chance of an event occurring.

* Probability values lie between **0 and 1**
* 0 → Event will not occur
* 1 → Event will definitely occur

Probability helps in **decision-making under uncertainty**, which is very common in data analysis.

---

### 2. Sample Space and Events

#### Sample Space (S)

The **sample space** is the set of all possible outcomes of an experiment.

Example:

* Tossing a coin → S = {Head, Tail}
* Rolling a die → S = {1, 2, 3, 4, 5, 6}

#### Event (E)

An **event** is a subset of the sample space.

Example:

* Getting a Head
* Rolling an even number

---

### 3. Probability Formula

Probability of an event:

Probability(E) = Number of favorable outcomes / Total number of outcomes

---

### 4. Probability Rules

#### 4.1 Addition Rule

Used when finding probability of **either** event occurring.

* For mutually exclusive events:
  Probability(A or B) = Probability(A) + Probability(B)

Example:

* Probability of rolling a 1 or 6 on a die

---

#### 4.2 Multiplication Rule

Used when finding probability of **both** events occurring.

* For independent events:
  Probability(A and B) = Probability(A) × Probability(B)

Example:

* Probability of getting Head in two coin tosses

---

### 5. Real-World Probability Examples

* Probability of a customer clicking an ad
* Probability of a loan default
* Probability of rain based on historical data
* Probability of a product being returned

Probability models are widely used in:

* Risk analysis
* Forecasting
* Machine learning models

---

### 6. Correlation

**Correlation** measures the **strength and direction of relationship** between two variables.

Examples:

* Advertising spend vs sales
* Study hours vs exam score

Correlation does **not** imply causation.

---

### 7. Types of Correlation

#### 7.1 Positive Correlation

* Both variables increase or decrease together
* When X increases, Y increases

Example:

* Experience vs salary

---

#### 7.2 Negative Correlation

* One variable increases while the other decreases

Example:

* Price vs demand

---

#### 7.3 No Correlation

* No visible relationship between variables

Example:

* Shoe size vs intelligence

---

### 8. Correlation Coefficient (r)

The **correlation coefficient (r)** quantifies correlation strength.

* r ranges from **-1 to +1**

| Value of r | Interpretation               |
| ---------- | ---------------------------- |
| +1         | Perfect positive correlation |
| 0          | No correlation               |
| -1         | Perfect negative correlation |

Higher absolute value of r → stronger relationship

---

### 9. Correlation vs Causation

A strong correlation does **not** mean one variable causes the other.

Examples:

* Ice cream sales and drowning incidents (both related to summer)
* Screen time and sleep issues

Always check:

* Logical relationship
* External factors
* Business or domain context

---

## Practical Examples (Full Scenarios)

### Example 1: Probability in Business

A company finds:

* 60% customers buy Product A
* 30% customers buy Product B

Questions:

* Probability a customer buys Product A
* Probability a customer buys both products (if independent)

---

### Example 2: Correlation Analysis

Dataset:

| Study Hours | Exam Score |
| ----------- | ---------- |
| 2           | 40         |
| 4           | 55         |
| 6           | 70         |
| 8           | 85         |

Observation:

* As study hours increase, exam score increases
* Strong positive correlation

---

## Practice Tasks

### Task 1: Sample Space

List the sample space for:

* Tossing two coins

---

### Task 2: Probability Calculation

Find probability of:

* Rolling an odd number on a die

---

### Task 3: Identify Correlation Type

Classify the relationship:

1. Temperature vs ice cream sales
2. Speed vs travel time
3. Shoe size vs exam marks

---

### Task 4: Conceptual Question

Why does correlation not imply causation?

---

### Task 5: Real-World Dataset

Choose any two related variables and:

* Identify correlation type
* Explain the relationship in business terms

---

## Learning Outcomes (Revisited)

By the end of this lecture, you should be able to:

* Apply basic probability rules
* Understand sample space and events
* Identify positive, negative, and no correlation
* Interpret correlation coefficient values
* Distinguish between correlation and causation

---

