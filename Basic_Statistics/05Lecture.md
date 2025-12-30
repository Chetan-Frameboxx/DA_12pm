# Lecture 5: Inferential Statistics & Hypothesis Testing

---

## Theory

### 1. Introduction to Inferential Statistics

**Inferential statistics** focuses on drawing conclusions about a **population** based on information obtained from a **sample**.

Key idea:

> We do not analyze the entire population; instead, we use samples to make informed decisions.

Inferential statistics helps answer questions like:

* Is this result due to chance or a real effect?
* Can we generalize sample findings to the population?

---

### 2. Sampling Techniques

Sampling is the process of selecting a subset of data from a population.

#### Common Sampling Methods

**1. Simple Random Sampling**

* Every item has an equal chance of selection
* Example: Randomly selecting students from a class list

**2. Stratified Sampling**

* Population divided into groups (strata)
* Samples taken from each group
* Example: Selecting employees from each department

**3. Systematic Sampling**

* Selecting every nth item
* Example: Every 10th customer

**4. Convenience Sampling**

* Based on availability
* Fast but may be biased

---

### 3. Central Limit Theorem (Conceptual)

The **Central Limit Theorem (CLT)** states:

> When sample size is sufficiently large, the sampling distribution of the mean approaches a normal distribution, regardless of the population distribution.

Key points:

* Sample size typically ≥ 30
* Enables use of normal distribution assumptions
* Foundation of hypothesis testing and confidence intervals

---

### 4. Hypothesis Testing Framework

**Hypothesis testing** is a structured approach to making decisions using data.

General steps:

1. Define hypotheses
2. Choose significance level (α)
3. Calculate test statistic / p-value
4. Make decision
5. Draw conclusion

---

### 5. Null and Alternative Hypothesis

#### Null Hypothesis (H₀)

* Assumes **no effect or no difference**
* Default assumption

Example:

* Average delivery time is 3 days

#### Alternative Hypothesis (H₁ or Hₐ)

* Represents a **new claim or effect**

Example:

* Average delivery time is not 3 days

---

### 6. p-value and Significance Level

#### Significance Level (α)

* Threshold for decision-making
* Common values: 0.05 or 0.01

#### p-value

* Probability of observing results as extreme as the sample, assuming H₀ is true

#### Decision Rule

* If p-value ≤ α → Reject H₀
* If p-value > α → Fail to reject H₀

---

### 7. Type I and Type II Errors

| Error Type    | Meaning                      | Example          |
| ------------- | ---------------------------- | ---------------- |
| Type I Error  | Rejecting a true H₀          | False alarm      |
| Type II Error | Failing to reject a false H₀ | Missed detection |

Relationship:

* Lower α reduces Type I error but may increase Type II error

---

## Practical Examples (Full Scenarios)

### Example 1: Quality Control Scenario

Claim:

* A factory claims average bottle weight is 1 liter

Hypotheses:

* H₀: Mean weight = 1 liter
* H₁: Mean weight ≠ 1 liter

If p-value = 0.03 and α = 0.05:

* Reject H₀
* Conclusion: Bottle weight differs from 1 liter

---

### Example 2: Marketing Campaign Analysis

* Null Hypothesis: New campaign does not increase sales
* Alternative Hypothesis: New campaign increases sales

Result:

* p-value = 0.12

Decision:

* Fail to reject H₀
* No strong evidence that campaign improved sales

---

## Practice Tasks

### Task 1: Conceptual Understanding

Explain why inferential statistics is needed instead of analyzing only descriptive statistics.

---

### Task 2: Identify Hypotheses

Write H₀ and H₁ for:

* A claim that average exam score is 70

---

### Task 3: Decision Making

If α = 0.05 and p-value = 0.01:

* What decision will you take?
* Why?

---

### Task 4: Error Identification

Classify the error:

* A disease test shows positive when the person is healthy

---

### Task 5: Real-World Application

Choose a real-world claim and:

* Define population and sample
* Write null and alternative hypotheses

---

## Learning Outcomes (Revisited)

By the end of this lecture, you should be able to:

* Understand the role of inferential statistics
* Explain sampling techniques and CLT conceptually
* Formulate null and alternative hypotheses
* Interpret p-values and significance levels
* Identify Type I and Type II errors

---

