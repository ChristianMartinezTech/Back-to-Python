#!/usr/bin/env python3
""" Python Collections: Strings, Tuples, Lists, and Dictionaries """


if __name__ == "__main__":

    # Strings
    string_1 = "hola a todos"
    string_2 = """HOLA, 
    A,
     TODOS"""
    print(type(string_1))
    print(string_1[0])
    print(string_1[-1])
    print("HOLA" in string_2)
    print("--------------------")


    # Lists
    list_1 = ["A", "B", "C", "1", "2", "3"] # Can hold any type of datatype inside
    list_2 = list(("c", "b", "a", "3", "2", "1")) # Ordered, Chageable
    print(type(list_1))
    print("A" in list_1)
    print(len(list_2))
    print("--------------------")


    # Tuples
    tuple_1 = ("a", "b", "c") # Can hold only the same data type
    tuple_2 = tuple(("1", "2", "3")) # Ordered, Unchangeable, allows duplicates
    print(type(tuple_1))
    print(tuple_2[0])
    print(tuple_2[-1])
    print("--------------------")

    # Sets
    set_1 = {"apple", "banana", "cherry", 1, 2} # Can hold multiple datatypes 
    set_2 = set((True, 1, 2)) # Unordered, Unchangeable*, Unindexed, No duplicated
    print(type(set_1))
    print(set_2)
    print("--------------------")

    # Dictionaries
    dict_1 = {
    "str" : "hola a todos",
    "lst" : {
    "number" : 1
    }
    }

    dict_2 = dict(string = string_1, list = list_1, tuple = tuple_1)

    print(type(dict_1))
    print(dict_1)
    print(dict_2["string"])
