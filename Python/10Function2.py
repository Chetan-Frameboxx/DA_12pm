# Function (tuple) - *args



# def add_all(*numbers):
#     return sum(numbers)

# print(add_all(2, 4, 6, 8))  


# Function (dictionary) - **kwargs


# def student_info(**details):
#     for key, value in details.items():
#         print(key, ":", value)

# student_info(name="Ravi", age=20, subject="Math")




# Recursion



# def factorial(n):
#     if n == 0 or n == 1:   # base case
#         return 1
#     return n * factorial(n-1)   # recursive call

# print(factorial(5))   # 120




# Scope 


num1 = 10


print(num1)


def inside():
    num2 = 20
    print(num1)
    print(num2)
    

inside()




# print(num2) => X




# Practice Task 


# 1. Write a function sum_all(*nums) that returns the total of any numbers passed.
# 2. Create a function print_details(**info) that prints all key-value pairs.
# 3. Show the difference between local and global variable with the same name.
# 4. Write a recursive function to print numbers from 1 to 5.
# 5. Write a recursive function to calculate the sum of first n natural numbers.
# 6. Create a recursive function to find Fibonacci numbers.
# 7. Make a function average(*values) that returns the average of numbers.
# 8. Write a function that accepts student info using **kwargs and prints it in sentence form.
# 9. Create a counter using a global variable that increments each time a function is called.
# 10. Write a recursive function to reverse a string.
