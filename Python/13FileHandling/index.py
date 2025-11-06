# # Open a file in write mode
# f = open("example.txt", "w")

# # Write data to the file
# f.write("Hello, this is a test file Namaste.\n")


# # Read data from the file 
# f = open("example.txt", "r")
# print(f.read())


# # Close the file
# f.close()



# # Open file in read mode
# f = open("example.txt", "r")

# # Read the whole content
# content = f.read()
# print(content)

# # Close file
# f.close()


# with open("example.txt", "r") as f:
#     content = f.read()
#     print(content)



# # Write mode (overwrites file)
# with open("example.txt", "w") as f:
#     f.write("Overwriting the previous content.\n")

# # Append mode (adds at the end)
# with open("example.txt", "a") as f:
#     f.write("This line is added at the end.\n")



# With JSON 


# import json

# data = {"name": "Rohan", "age": 22, "skills": ["Python", "JavaScript"]}

# with open("data.json", "w") as f:
#     json.dump(data, f)  # Convert dict to JSON and save



# with open("data.json", "r") as f:
#     data = json.load(f)  # Convert JSON back to Python dict
#     print(data)  
#     print(data["name"])  


# With CSV 


import csv

header = ["Name", "Age", "City"]
rows = [
    ["Rohan", 22, "Delhi"],
    ["Ravi", 25, "Mumbai"],
    ["Kishan", 28, "Ahm"]
]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)


# with open("data.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
