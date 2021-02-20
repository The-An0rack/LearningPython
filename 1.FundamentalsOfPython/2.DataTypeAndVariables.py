"""
Variables are of 2 types:
1. Primitive Data-types
    a. Integer
    b. Float
    c. Strings
    d. Boolean
2. Derived Data-type(Non-Primitive Data-types)
    a.List
    b.Dictionary
    c.Tuples
"""

height = 152
print("Your height is " + str(height) + "cm")
print(type(height))

val = 15.7
print("Value of val variable: " + str(val))
print(type(val))

# Both " and ' are accepted for strings
name = "Dewashish Mehta"
language = 'Python3'
print(name + "is currently learning" + language)
print(type(name))
print(type(language))

isTrue = True
print(isTrue)
print(type(isTrue))

# Multiple assignment
x,y = 20, 50
print(x,y)
x, y = y, x
