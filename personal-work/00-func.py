#!/usr/bin/env python3
""" Quick program to work as a Python func reminder """


def opening_msg():
    # Quick Hello mgs
    return "Hello"


def closing_msg():
    # Quick Hello mgs
    return "Bye"


if __name__ == "__main__":

    for x in range(10):
        if (x % 2) == 0:
            print('{} {}'.format(opening_msg(), x))
        else:
            print('{} {}'.format(closing_msg(), x))
