import numpy as np

# 1D Array 

arr =np.array([1,2,3,4,5])
print(arr)


# 2D Array 

arr2d =np.array([[1,2,3,4], [5,6,7,8]])
print(arr2d)

# 3D Array 

arr3d =np.array([[1,2,3,4], [5,6,7,8], [9,8,7,6]])
print(arr3d)


# Size of an Array 

print(arr.size)
print(arr2d.size)
print(arr3d.size)

# Shape of an Array 

print(arr.shape)
print(arr2d.shape)
print(arr3d.shape)


# Sum


sum_arr = np.sum(arr)
print(sum_arr)
sum_arr2d = np.sum(arr2d)
print(sum_arr2d)
sum_arr3d = np.sum(arr3d)
print(sum_arr3d)

# sqrt


sqrt_arr = np.sqrt(arr)
print(sqrt_arr)
sqrt_arr2d = np.sqrt(arr2d)
print(sqrt_arr2d)
sqrt_arr3d = np.sqrt(arr3d)
print(sqrt_arr3d)


new_arr = [1,4,9,16,25,36,49,64,81]
new_arr_sqrt = np.sqrt(new_arr)
print(new_arr_sqrt)


print(np.mean(arr))  
print(np.max(arr)) 


# Random Numbers

print(np.random.rand(2,3))
print(np.random.randint(1,10,5))



# Zeros 


print(np.zeros((3,3)))

# Ones 


print(np.ones((3,3)))

# dtype

print(arr.dtype)



# Sort 

a = [2, 1, 45, 3, 8]

print(np.sort(a))

# transpose

print(np.transpose(arr2d))
print(np.transpose(arr3d))


# ravel 


print(np.ravel(arr3d))
