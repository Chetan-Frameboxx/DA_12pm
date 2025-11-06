# print(10/0)
# print("hello")

# print(int("abc"))


# try:
#     num = int(input("Enter a number: "))
#     # num = input("Enter a number: ")
#     # num = 0
#     print(10 / num)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Please enter a valid number.")
# finally:
#     print("Completed...")



# try:
#     f = open("data.txt", "r")
#     content = "NAMASTE BHARAT"
#     # print(f.write(content))
#     print(f.read())
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Closing file...")





# DOubt 


age = int(input("Enter age: "))
# age = 0
if age < 0:
    raise ValueError("Age cannot be negative!")
else:
    print("Your age is:", age)

