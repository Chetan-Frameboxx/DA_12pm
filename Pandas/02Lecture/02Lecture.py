import pandas as pd



df = pd.read_csv("sales.csv")

# print(df)


# # Single column
# print(df["Product"])

# # Multiple columns
# print(df[["Product", "Price"]])



# Single row
# print(df.loc[0])     # by label
# print(df.iloc[0])    # by position

# Multiple rows
# print(df.loc[0:2])    # 0, 1,2
# print(df.loc[0:2:2])    # 



# Price > 10000
# print(df[df["Price"] > 10000])

# Electronics only
# print(df[df["Category"] == "Electronics"])

# Multiple conditions
# print(df[(df["Category"] == "Accessories") & (df["Quantity"] > 5)])


# Sort by Price
# print(df.sort_values(by="Price"))

# Sort by Total (highest first)
# print(df.sort_values(by="Total", ascending=False))


# Add Profit column
# df["Profit"] = df["Total"] * 0.10
# print(df)

# # Drop Date column
# df = df.drop("Date", axis=1)
# print(df)



# Default index
# print(df.index)

# # Set OrderID as index
# df = df.set_index("OrderID")
# print(df)

# # Reset to default
# df = df.reset_index()
# print(df)


# Detect missing values
# print(df.isnull().sum())

# Drop rows with missing values
# df_cleaned = df.dropna()
# print(df_cleaned)

# Fill missing values with a constant
# df["Price"].fillna(0, inplace=True)
# print(df)

# Fill missing with mean
# df["Price"].fillna(df["Price"].mean(), inplace=True)

# print(df)



# Check duplicates
# print(df.duplicated())
# print(df.duplicated().sum())

# Drop duplicates
# df = df.drop_duplicates()
# print(df)




# Check data types
# print(df.dtypes)

# Convert Price to float
# df["Price"] = df["Price"].astype(float)
# print(df)

# Convert Date to datetime
print(df)
# df["Date"] = pd.to_datetime(df["Date"])
# print(df)   => Error Will solve Later