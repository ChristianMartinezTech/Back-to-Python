#!/usr/bin/env python3
""" Quick Python refresh before interview """


def even_odd(number):
    if number % 2 == 0:
        return "even :)"
    else:
        return "odd :("


if __name__ == "__main__":
    for i in range(10):
        print(str(i) + " is " + even_odd(i))
