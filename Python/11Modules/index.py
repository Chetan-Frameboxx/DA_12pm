# import module_greet
# import module_greet as mg
# import add as a
# from add import addTwoNumber ,addThreeNumber
# import math
# import random
# import datetime
# from myPac import addNum, multiply

import requests

import numpy as np


import add as a

a.addThreeNumber(4,5,3)



# print(module_greet.greet("Rohan"))
# print(mg.greet("Rohan"))
# print(add.addTwoNumber(4,5))
# print(add.addThreeNumber(4,5,9))
# print(a.addTwoNumber(4,5))
# print(a.addThreeNumber(4,5,9))


# math 

# print(math.sqrt(81))
# print(math.pow(2,3))
# print(math.isfinite(12))
# print(math.ceil(8.4))
# print(math.floor(8.4))

# random

# print(random.randint(1, 10))  
# print(random.choice(["red", "blue", "green"]))  




# datetime 


# print(datetime.date(day=12,month=5, year=2000))







# Package 


# print(addNum.addTwoNum(4,3))
# print(multiply.multiplyTwoNum(4,3))



# res = requests.get("https://api.github.com/users/jayramin")
# print(res.status_code)


# data = res.json()

# print(data["login"])
# print(data["name"])



# arr = [1,2,3,4,5,6]
arr = np.array([1,2,3,4,5])
print(arr)

arr2d = np.array([[1,2,3,4,5], [4,5,6,7,8]])
print(arr2d)

arr3d = np.array([[1,2,3,4,5], [4,5,6,7,8], [1,2,2,4,5]])
print(arr3d)
# print(np.size(arr))
# print(np.transpose(arr))
# print(np.ravel(arr))


print(np.zeros((2, 5)))
print(np.ones((5, 5)))










# Refrenece 




# https://docs.python.org/3/library/math.html


# https://docs.python.org/3/library/random.html


# https://docs.python.org/3/library/datetime.html