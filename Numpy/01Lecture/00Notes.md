# NumPy (Lecture 1: Basics)

1. What is NumPy & Why use it?

- NumPy = Numerical Python → A Python library for fast numerical calculations.
- Works with arrays (much faster than Python lists).
- Used in Data Analysis, Machine Learning, and Scientific Computing.

- Why not just Python lists?
    - NumPy arrays take less memory
    - Faster operations
    - Lots of built-in mathematical functions

2. Installing & Importing NumPy

- Install (only once):
- pip install numpy

- Import (in Python code):
- import numpy as np


<!-- python -m venv myenv -->

<!-- myenv\Scripts\activate -->

3. Creating Arrays

- From Python List:

- arr = np.array([1, 2, 3, 4, 5])
- print(arr)      # [1 2 3 4 5]


- Multi-Dimensional (2D Array):

- arr2d = np.array([[1,2,3],[4,5,6]])
- print(arr2d)

# [[1 2 3]
#  [4 5 6]]


-  Special Arrays:

- np.zeros((3,3))     # 3x3 matrix of 0s
- np.ones((2,4))      # 2x4 matrix of 1s
- np.arange(0,10,2)   # [0,2,4,6,8]
- np.linspace(0,1,5)  # 5 values between 0 and 1

4. Array Attributes

- arr = np.array([[1,2,3],[4,5,6]])
- print(arr.ndim)   # Dimensions (2)
- print(arr.shape)  # Rows & Columns (2,3)
- print(arr.size)   # Total elements (6)
- print(arr.dtype)  # Data type (int32, float64, etc.)

5. Indexing & Slicing

- 1D Array:

- arr = np.array([10,20,30,40,50])
- print(arr[0])     # 10
- print(arr[-1])    # 50
- print(arr[1:4])   # [20 30 40]


- 2D Array:

- arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
- print(arr2d[1,2])     # Row 1, Col 2 → 6
- print(arr2d[0:2, 1:3]) # Subarray [[2 3],[5 6]]

6. Basic Mathematical Operations

- Element-wise operations:

- arr = np.array([1,2,3,4])
- print(arr + 2)    # [3 4 5 6]
- print(arr * 3)    # [3 6 9 12]
- print(arr ** 2)   # [1 4 9 16]


-  Useful functions:

- print(np.sqrt(arr))   # Square root
- print(np.sum(arr))    # Sum of elements
- print(np.mean(arr))   # Average
- print(np.max(arr))    # Maximum value

7. Random Numbers

- np.random.rand(3,3)        # 3x3 random numbers between 0 and 1
- np.random.randint(1,10,5)  # 5 random integers between 1 and 9


# Practice Task

1. Create a NumPy array of numbers 1–10.
2. Generate a 3x3 array of all zeros.
3. Create an array with values from 0–20 with step 2.
4. Create a 2D array (3x3) and access the middle element.
5. Slice an array [10,20,30,40,50,60] to get [20,30,40].
6. Create an array [1,2,3,4,5] and multiply each element by 10.
7. Find sum, mean, and max of an array [5,10,15,20,25].
8. Generate 10 random integers between 100 and 200.
9. Create a 4x4 array of random numbers and print its shape & size.`
10. Create an array of squares of numbers from 1–10 using NumPy.*-/*-/`