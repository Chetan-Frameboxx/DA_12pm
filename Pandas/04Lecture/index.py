import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data_large.csv")
# df.head()        # show first 5 rows
# df.info()        # types + non-null counts
# df.describe()    # numeric summary
# print(df.describe())



# # sample before
# df[["OrderID","Customer"]].head(8)
# print(df[["OrderID","Customer"]].head(8))

# # lengths before
df["cust_len_before"] = df["Customer"].str.len()

# # clean: strip edges, remove * and ! and any non-letter (keep spaces), then lower
df["Customer_clean"] = (
    df["Customer"]
      .str.strip()
      .str.replace(r"[^A-Za-z\s]", "", regex=True)
      .str.lower()
)

# # lengths after
df["cust_len_after"] = df["Customer_clean"].str.len()

df[["Customer","Customer_clean","cust_len_before","cust_len_after"]].head(8)
print(df[["Customer","Customer_clean","cust_len_before","cust_len_after"]].head(8))


# print(df)


df["Date"] = pd.to_datetime(df["Date"], errors="coerce")   # convert; invalid -> NaT
df["Year"]  = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()
df["Day"]   = df["Date"].dt.day

# # better grouping key for chronological month grouping
df["YearMonth"] = df["Date"].dt.to_period("M")   # e.g. 2023-02

print(df)


# # 1. Total sales by Region
sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(sales_by_region)

# # 2. Average sales per Category
avg_by_category = df.groupby("Category")["Sales"].mean()
print(avg_by_category)

# # 3. Max quantity per Product
max_qty_product = df.groupby("Product")["Quantity"].max()
print(max_qty_product)

# # 4. Sales by Region & Category
region_category_sales = df.groupby(["Region","Category"])["Sales"].sum()
# print(region_category_sales)



region_stats = df.groupby("Region").agg(
    total_sales = ("Sales", "sum"),
    avg_sales   = ("Sales", "mean"),
    mean_qty    = ("Quantity", "mean"),
    orders      = ("OrderID", "nunique")
).sort_values("total_sales", ascending=False)

print(region_stats)


monthly = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()
# For plotting convert to timestamp index for matplotlib
monthly_ts = monthly.to_timestamp()
monthly_ts.plot(kind="bar", title="Monthly Sales Trend", figsize=(10,4))
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()


pivot = pd.pivot_table(
    df,
    values=["Sales","Quantity"],
    index="Region",
    columns="Category",
    aggfunc={"Sales":"sum", "Quantity":"mean"},
    fill_value=0
)
print(pivot)

ct = pd.crosstab(df["Region"], df["Category"])
print(ct)

# # normalized percentage (optional)
ct_pct = pd.crosstab(df["Region"], df["Category"], normalize="index") * 100
print(ct_pct.round(1))


# # cleaned full dataset
df.to_csv("cleaned_sales.csv", index=False)

# # export pivot
pivot.to_csv("pivot_sales.csv")

# # excel:
df.to_excel("cleaned_sales.xlsx", sheet_name="Cleaned", index=False)



# # Sales distribution
df["Sales"].plot(kind="hist", bins=20, title="Sales Distribution")
plt.show()

# # Region share (pie)
df.groupby("Region")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%", title="Sales by Region")
plt.ylabel("")  # remove y-label
plt.show()

# # Sales vs Quantity scatter
df.plot(kind="scatter", x="Quantity", y="Sales", title="Sales vs Quantity")
plt.show()



# load → clean → extract date → agg → pivot → export → plot.