# Python Lecture 2 – Input/Output, Data Types, and Operators


## 1. Input and Output in Python

### Output (`print()`)
- The `print()` function is used to display information.
- You can print strings, numbers, and variables.

print("Hello, World!")        # printing text
x = 10
print("The value of x is", x) # printing with variables
```

➡️ `print()` automatically adds a space between arguments and a newline at the end.


### Input (`input()`)
- The `input()` function is used to take input from the user.
- By default, input is always a **string**.

name = input("Enter your name: ")
print("Welcome,", name)
```

#### Converting input
age = int(input("Enter your age: "))   # convert input to integer
height = float(input("Enter your height: ")) # convert input to float
print("Next year, you will be", age + 1)


## 2. Data Types

Python has different built-in data types. The most commonly used are:

### Basic Data Types
- **int** → whole numbers (10, -5, 0)  
- **float** → decimal numbers (3.14, -2.5)  
- **str** → strings/text ("hello", 'Python')  
- **bool** → Boolean values (True, False)  

a = 10          # int
b = 3.14        # float
c = "Python"    # str
d = True        # bool

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>


### Type Conversion
You can convert between types using built-in functions:  
- `int()`, `float()`, `str()`, `bool()`

x = "123"
print(int(x) + 5)    # 128
print(float(x) + 2)  # 125.0

 Converting invalid strings to numbers gives an error:
y = "abc"
# int(y)  → Error!


## 3. Operators in Python

Operators are symbols that perform operations on variables and values.


### Arithmetic Operators
- Addition `+`  
- Subtraction `-`  
- Multiplication `*`  
- Division `/`  
- Floor Division `//`  
- Modulus `%` (remainder)  
- Exponentiation `**` (power)

a, b = 10, 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000


### Comparison Operators
Used to compare values (result is `True` or `False`).  
- Equal `==`  
- Not Equal `!=`  
- Greater `>`  
- Less `<`  
- Greater or Equal `>=`  
- Less or Equal `<=`  

print(5 == 5)  # True
print(5 != 3)  # True
print(7 > 2)   # True
print(4 < 2)   # False


### Logical Operators
Used to combine conditions.  
- `and` → True if both are True      
- `or` → True if at least one is True  
- `not` → reverses True/False  

x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False


### Assignment Operators
Used to assign values.  
- `=` assign  
- `+=` add and assign   
- `-=` subtract and assign  
- `*=` multiply and assign  
- `/=` divide and assign  

num = 10
num += 5  # same as num = num + 5
print(num)  # 15

---

### Example: Combining Input, Data Types, and Operators
# Program to calculate area of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print("The area of rectangle is:", area)

---

##  Summary
- Learned how to use **`print()`** for output and **`input()`** for user input.  
- Understood **basic data types** (int, float, str, bool).  
- Practiced **operators**: arithmetic, comparison, logical, assignment.  

---

##  Practice Exercises
1. Write a program that asks the user for their **name** and **age**, then prints:  
   `"Hello <name>, you are <age> years old."`

2. Write a program that takes two numbers as input and prints:  
   - Their sum  
   - Their difference  
   - Their product  
   - Their quotient  

3. Write a program that asks for a number and checks:  
   - Is it even or odd? (Hint: `% 2`)  

4. Write a program to calculate the **area of a circle** (Area = π × r², take π = 3.14).  
