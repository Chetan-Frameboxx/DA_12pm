# Loops 


   



# 1. while loop 

# i = 0
# print(i)

# while i <= 10:
#     print(i)
#     i += 1

# print("Start")
# i = 1
# print(i)

# while i <= 10:
#     print("Namaste Bharat")
#     i += 1

# print("End")


# print("Start")
# i = 10
# print("Initial : ", i)

# while i > 0:
#     print(i)
#     i -= 1

# print("End")






# print("Namaste Bharat")
# print("Namaste Bharat")
# print("Namaste Bharat")
# print("Namaste Bharat")
# print("Namaste Bharat")
# print("Namaste Bharat")
# print("Namaste Bharat")
# print("Namaste Bharat")



# 2. For loop


# list = ["Orange", "Mango", "kiwi", "Banana", "Papaya "]



# for item in list:
#     print(item)



# print(arr)
# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[4])



# 3. Using range()

# for i in range(5):
#     print("Number:", i)



# range(n)  -> o to n -1
# range(start, stop)
# range(start, stop, step)


# for i in range(5, 10):
#     print("Number:", i)

# for i in range(1, 10, 2):
#     print("Number:", i)



# Loop Control Statements



# break


# for i in range(10):
#     if i == 5:
#         break

#     print(i)


# continue


# for i in range(10):
#     if i % 2 == 0:
#         continue
        
#     print(i)



# Pattern Prints


# for i in range(5):            #  Outer loop
#     for j in range(1, ):        #  Inner Loop             
#          print(i, j)


# i=0
# while i < 5:                    # Outer Loop
#     j=i
#     while j > 0 :                 # Inner Loop
#         j -= 1
#         # print(j)
#         print(j, end="")
#     # print("*")
#     print(i)
#     i += 1
    
    
    
# rows = 0
    
# for i in range(rows, 6, 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()



rows = 5
    
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()









