import pandas as pd


# data = {
#     "Name": ["Amit", "Ravi", "Priya"],
#     "Age": [23, 25, 22],
#     "Score": [85, 90, 88]
# }



# df = pd.DataFrame(data)
# print(df)


# data = [
#     ["Amit", 23, 85],
#     ["Ravi", 25, 90],
#     ["Priya", 22, 88]
# ]

# df  = pd.DataFrame(data, columns=["Name","Age", "Score"], index=["RowA","RowB", "RowC"])
# print(df)



data = {
    "Name": pd.Series(["Suresh", "Ramesh", "Mahesh", "Mukesh"], index=["A", "B", "C", "D"]),
    "Age": pd.Series([23, 25, 22, 27], index=["A", "B", "C", "D"]),
    "Score": pd.Series([85, 90, 88, 75], index=["A", "B", "C","D"])
}


# Atttribute 

df =pd.DataFrame(data)
print(df)
# print('\nShape :', df.shape)
# print('\nSize :', df.size)
# print('\nDimenssion :', df.ndim)
# print('\ncolumns Name :', df.columns)
# print('\nData type :', df.dtypes)
# print('\nIndex :', df.index )
# print('\nValues :', df.values )




# DataFrame Methods


# print(df.head(2))
# print(df.tail(1))
# df.info()
# print(df.describe())

