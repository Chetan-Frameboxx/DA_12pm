import numpy as np

data = np.loadtxt("numbers.csv", delimiter=",", skiprows=1)  # skip header
print("Data:\n", data)
print("Shape:", data.shape)



# data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)
# data = np.genfromtxt("students.csv", delimiter=",", skip_header=1, usecols=(1,2))
# data = np.genfromtxt("students.csv", delimiter=",", skip_header=1, usecols=(1,2), filling_values= 0)
# print("Data:\n", data)


data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)

# age = data[:,1]  # First column
marks = data[:,2]  # second column
# mean_age = np.nanmean(age)
# age = np.nan_to_num(age, nan=mean_age)
mean_marks = np.nanmean(marks)
marks = np.nan_to_num(marks, nan=mean_marks)

print("Marks after handling NaN:", marks)
# print("Age after handling NaN:", age)



data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)

ages = data[:,1]   # first column
marks = data[:,2]  # second column

print("Ages:", ages)
nan_marks = np.nanmean(marks)
marks = np.nan_to_num(marks, nan=nan_marks)
print("Marks:", marks)
print("Average Marks:", nan_marks)
print("Top 2 Marks:", np.sort(marks)[-2:])
print("reverse", np.sort(marks)[::-1])
# print(np.sort(marks)[-2:])





arr = np.array([[1, 90], [2, 85], [3, 95]])
np.savetxt("output.csv", arr, delimiter=",", fmt="%d", header="ID,Marks", comments='')
print("Data saved to output.csv")




sales = np.genfromtxt("sales.csv", delimiter=",", skip_header=1)

quantity = sales[:,1]
price = sales[:,2]

# Handle NaN in price
mean_price = np.nanmean(price)
price = np.nan_to_num(price, nan=mean_price)

# Total sales for each row
total_sales = quantity * price
print("Total Sales per product:", total_sales)

# Overall total
print("Grand Total Sales:", np.sum(total_sales))