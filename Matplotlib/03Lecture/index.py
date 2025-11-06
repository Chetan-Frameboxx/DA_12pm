import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)   # 1000 random numbers (normal distribution)

plt.hist(data, bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram Example")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()


sizes = [30, 20, 25, 25]
labels = ["North", "South", "East", "West"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Sales by Region")
plt.show()


data = [7, 8, 5, 6, 10, 12, 7, 8, 15, 25]

plt.boxplot(data)
plt.title("Box Plot Example")
plt.ylabel("Values")
plt.show()



x = np.arange(3)  # groups
men = [20, 35, 30]
women = [25, 32, 34]

plt.bar(x - 0.2, men, width=0.4, label="Men")
plt.bar(x + 0.2, women, width=0.4, label="Women")

plt.xticks(x, ["Group A", "Group B", "Group C"])
plt.legend()
plt.title("Grouped Bar Chart")
plt.show()



men = [20, 35, 30]
women = [25, 32, 34]

plt.bar(x, men, label="Men")
plt.bar(x, women, bottom=men, label="Women")

plt.xticks(x, ["Group A", "Group B", "Group C"])
plt.legend()
plt.title("Stacked Bar Chart")
plt.show()


import pandas as pd

sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [200, 250, 300, 400],
    "Profit": [50, 80, 120, 150]
})

# Line chart
sales.plot(x="Month", y="Sales", kind="line", marker="o", title="Monthly Sales")

# Bar chart
sales.plot(x="Month", y=["Sales", "Profit"], kind="bar")

plt.show()