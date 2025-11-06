# Dictionaries in Python


details = {
    "name": "Rohan",
    "age" : 20,
    "isLoggedIn" : True
    
}


# print(details)
# print(details["name"])
# print(details["age"])
# print(details["isLoggedIn"])



Student_details = {
    "s1" : {
    "name": "Rohan",
    "age" : 20,
    "course" : "Wd"
    
},
    "s2" : {
    "name": "Suresh",
    "age" : 22,
    "course" : "Fullstack"
    
}
    ,
   "s3" : {
    "name": "Ramesh",
    "age" : 25,
    "course" : "Data Science"
    
},
  "s4" : {
    "name": "Pooja",
    "age" : 20,
    "course" : "Digital Marketing"
    
}
}


print(Student_details)
# print(Student_details)
print(Student_details["s4"])
Student_details["s4"]["name"] = "Hetal"
print(Student_details["s4"])

print(Student_details["s4"]["name"])