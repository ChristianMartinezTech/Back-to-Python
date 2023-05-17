#!/usr/bin/env python3
"""
Python3 experimenting
"""


# Variable declarations
a = 5
b = 6.5
c = "Hello"
d = "a"
e = ["Hello", "What", "datatype", "is", "this"]
f = {
    "Name": "Chris",
    "Age": 26,
    "Rating": 8.5,
    "Phrase": ["Hello", "Honey", "Wasup"],
    "Dict": {
        "Name": "Chris",
        "Age": 26,
        "Rating": 8.5,
        "Phrase": ["Hello", "Honey", "Wasup"],
    },
}
g = (1, 2, "Hello")
h = True

# Printing dict
print("Dictionary time!!")
print(f)
print("#################")
print()

print("List inside dictionary!!")
print(f["Phrase"])
print(f["Phrase"][0])
print(f["Phrase"][2])
print(f["Phrase"][-1]) # Great fucking job!
print("#################")
print()

print("Dict inside dictionary!!")
print(f["Dict"])
print(f["Dict"]["Phrase"])
print(f["Dict"]["Phrase"][0])
print(f["Dict"]["Phrase"][2])
print("#################")
print()

# Printing variable type
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print("#################")
print()

# If statement
if (a + b) == 10: 
    print("Its ten")

if (a + b) == 10.5: 
    print("Its ten point five")

if (a + b) == 11: 
    print("Its eleven")

if (a + b) == 11.5: 
    print("Its eleven point five")
    
    # For loop
    for i in range(11):
        print(i)
    print(":)")
    print("#################")
    print()

    for i in range(-1, 9):
        print(i)
    print(":)")
    print("#################")
    print()

if (a + b) == 12: 
    print("Its twelve")
