# str = 'Rohan'
# str = "Rohan"
# str = "Rohan, Plays 'Football'"
# print(str)


# Methods of String 


str  = "my Name is Rohan"
str1  = "  my Name is Rohan      "

# print(str)
# print(str[0])
# print(str[1])
# print(str[2])
# print(str[3])
# print(str.__len__())



print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.replace("Rohan","Anuj"))
print("Rohan" in "my Name is Rohan")
print("Py" in "Python")     # True
print("Java" not in "Python") # True
print(str.count("a"))
print(str.find("Roh")) 
print(str1.strip())
print(str.split())
# print(str[0:5])
# print(str[0:])
print(str[:8])
print(str)
print(str.title())


str3 = "My Name Is Rohan"
print(str3.istitle())




# f-String, and format()

name = "Suresh"
age = "20"


# print(f"Hey, My name is {name}, and I'm {age} year old.")
# print("Hey, My name is {}, and I'm {} year old.".format(name, age))
# print("Hey, My name is {}, and I'm {} year old.".format("Ramesh", 30))



print("Namaste" + " " + "Bharat") # Concatination  or concat
# print((10 + int("10"))) # Concatination  or concat



print("Namaste\n" * 5)





# Loops 


# word = "Code"
# for ch in word:
#     print(ch)

for ele in str:
    print(ele)
    



k = 250
print(f"User pressed the: {k}")


# \': Inserts a literal single quote within a string delimited by single quotes.
# \": Inserts a literal double quote within a string delimited by double quotes.
# \\: Inserts a literal backslash.
# \n: Inserts a newline character, moving subsequent text to a new line.
# \t: Inserts a horizontal tab character, creating a tab space.
# \r: Inserts a carriage return, moving the cursor to the beginning of the current line.
# \b: Inserts a backspace character.
# \f: Inserts a form feed character.
# \ooo: Represents an octal value for a character (e.g., \101 for 'A').
# \xhh: Represents a hexadecimal value for a character (e.g., \x41 for 'A').





