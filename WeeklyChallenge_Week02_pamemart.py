#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 1. Weekly Challenge2: Variable, Operators, Input/Output
We will ask the user for their name, numbers to do basic operations, strings 
and their age.
"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Martín Escorza"]
__date__ = "2021/02/25"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

def check_input(input):
    try:
        # Convert it into number
        val = float(input)
        return val
    except ValueError:
        print("This is not a valid number.")
        return ValueError

def main():
    print("Hello World! I'm Python... What's your name?")
    name = input()
    print(f"Nice to meet you, {name}.")
    print("\nIt is really simple to do scriptiong with me... But I can do a"
    " lot of things... Let me show you.")
    print("\nI can add two numbers and give you the result.")
    print("Give me one number.")
    number1 = ValueError
    while number1 == ValueError:
        number1 = input("Number: ")
        number1 = check_input(number1)
    print("Give me another number.")
    number2 = ValueError
    while number2 == ValueError:
        number2 = input("Another number: ")
        number2 = check_input(number2)
    print(f"{number1:.2f} * {number2:.2f} = {(number1 * number2):.2f}")
    print("\nI can do Boolean operations as well...")
    print("Give me one string.")
    string1 = input("String: ")
    print("Give me another string.")
    string2 = input("Another string: ")
    print(f"{string1} is equal to {string2}? {string1 == string2}")
    print("\nHow old are you?")
    age = ValueError
    while age == ValueError:
        age = input("Age: ")
        age = check_input(age)
    print(f"In 5 years you will be {int(age) + 5} OMG! You're really old!")
    print("\nC U Next Time :D with more Python")
    n = 0
    while n < 8:
        print(n * "*")
        n += 1

if __name__ == "__main__":
    main()