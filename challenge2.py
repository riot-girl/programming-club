#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021  Pam Martinez <pamemart@cisco.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

""" 
Level 1. Weekly Challenge2: Variable, Operators, Input/Output
We will ask the user for their name, numbers to do basic operations, strings 
and their age.
"""

__author__ = "Pam Martinez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Martín Escorza"]
__date__ = "2021/02/25"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__license__ = "GPLv3"
__maintainer__ = "Pam Martinez"
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
    print("\nIt is really simple to do scriptiong with me... But I can do a lot of things... Let me show you.")
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
    print(f"{number1} * {number2} = {number1 * number2}")
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