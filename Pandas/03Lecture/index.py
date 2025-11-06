import pandas as pd

# df = pd.DataFrame({
#     "Customer": ["  Amit  ", "Priya*", "ravi", "SNEHA "],
#     "Region": ["north", "South", "EAST", "west"]
# })

# print(df)

# # Case conversions
# df["Region_lower"] = df["Region"].str.lower()
# print(df)
# df["Region_upper"] = df["Region"].str.upper()
# print(df)


# # Strip whitespace
# df["Before_length"] = df["Customer"].str.len()
# print(df)
# df["Customer_strip"] = df["Customer"].str.strip()
# print(df)
# df["After_length"] = df["Customer_strip"].str.len()
# print(df)
# df["Customer_lstrip"] = df["Customer"].str.lstrip()
# print(df)
# df["Customer_rstrip"] = df["Customer"].str.rstrip()
# print(df)



# # Search inside strings
# print(df["Region"].str.contains("east", case=False))



# sales = pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "Date": ["2023-01-05", "2023-02-10", "2023-02-25"],
#     "Total": [5000, 7000, 6500]
# })
# print(sales.dtypes)
# # Convert column to datetime
# sales["Date"] = pd.to_datetime(sales["Date"])

# # Extract components
# sales["Year"] = sales["Date"].dt.year
# print(sales)
# sales["Month"] = sales["Date"].dt.month_name()
# print(sales)
# sales["Day"] = sales["Date"].dt.day
# print(sales)



# ts = pd.Timestamp("2023-09-12 14:30:00")
# print("Year:", ts.year)
# print("Month:", ts.month)
# print("Hour:", ts.hour)

# # Comparing timestamps
# ts1 = pd.Timestamp("2023-09-12")
# ts2 = pd.Timestamp("2023-09-15")
# print(ts2 > ts1)       # True
# print(ts2 - ts1)       # 3 days


# # Orders placed in February
# feb_sales = sales[sales["Date"].dt.month == 2]
# print(feb_sales)



# df2 = pd.DataFrame({
#     "Product": ["  Laptop ", "Mobile*", " Tablet", "Camera! "],
#     "Price": [50000, 20000, 15000, 35000]
# })

# # Strip whitespace
# df2["Product"] = df2["Product"].str.strip()

# # Remove unwanted characters
# df2["Product"] = df2["Product"].str.replace("[^a-zA-Z]", "", regex=True)

# print(df2)


data = pd.DataFrame({
    "Region": ["East", "East", "West", "South", "South"],
    "Category": ["Electronics", "Accessories", "Electronics", "Accessories", "Electronics"],
    "Sales": [60000, 4200, 12000, 15000, 75000],
    "Quantity": [10, 5, 3, 7, 8]
})

print(data)

# Total sales by Region
# print(data.groupby("Region")["Sales"].sum())

# Average quantity by Category
# print(data.groupby("Category")["Quantity"].mean())

# Group by multiple columns
print(data.groupby(["Region", "Category"])["Sales"].sum())