import matplotlib.pyplot as plt
import pandas as pd


# Load dataset
df = pd.read_csv("sales_data_large.csv")

print(df.head())


# Monthly Sales Trend
# monthly_sales = df.groupby(df["Date"].str[:7])["Sales"].sum()

# plt.figure(figsize=(8,5))
# plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b', linestyle='--')
# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()



# Sales by Region
# region_sales = df.groupby("Region")["Sales"].sum()

# plt.bar(region_sales.index, region_sales.values, color="orange")
# plt.title("Sales by Region")
# plt.xlabel("Region")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=45)

# plt.show()



plt.scatter(df["Quantity"], df["Sales"], alpha=0.5, color="green")
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()
