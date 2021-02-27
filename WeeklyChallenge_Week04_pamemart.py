#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021  Pam Martínez <pamemart@cisco.com>
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
Level 1. Weekly Challenge 4: For this week’s challenge, you are planning a trip
overseas.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Luis Uribe"]
__date__ = "2021/02/26"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__license__ = "GPLv3"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

from typing import List


def check_input(input):
    try:
        # Convert it into number
        val = int(input)
        return val
    except ValueError:
        print(f"{input} is not a valid number.")
        return ValueError

def tasks():
    print(">>>Hello! Please tell what you need to complete before your trip:")
    mylist = []
    for i in range (1, 6):
        mylist.append(input(f"Task {i}: "))
    i = ValueError
    while i == ValueError:
        i = input("\n>>>Which task you need to help remembering: ")
        i = check_input(i)
        if i != ValueError and (i < 1 or i > 5):
            print ("Try again.")
            i = ValueError
    print(f"You need to: {mylist[i-1]}")
    print("\n>>>You forgot an intermediate task.")
    task = input("What was it? ")
    i = ValueError
    while i == ValueError:
        i = input("\n>>>Which position should you do this task: ")
        i = check_input(i)
        if i != ValueError and (i < 1 or i > 5):
            print ("Try again.")
            i = ValueError
    mylist.insert(i-1,task)
    print("\n>>>And I will remind you to use the WC :)")
    mylist.append("Use the restroom")
    print(f"\n>>>Here is all you have to do before the trip:\n{mylist}")
    for i in range(0, 2):
        mylist.pop(0)
    print("\n>>>By the way you already did the 1st and 2nd task. Let's forget "
    f"about those:\n{mylist}")
    return mylist

def store_tuple():
    print("\n>>>Tell me your name and passport number and I will keep them"
    " safe!")
    name = input("Name: ")
    passn = input("Passport Number: ")
    mytuple = (name, passn)
    print(f"This will be safely stored: {mytuple}")
    return mytuple

def setset():
    print("\n>>>Here comes your friend...")
    countries = input("Countries you've been to: ").strip().split()
    countries1 = set()
    countries1.update(countries)
    countries = input("Countries your friend has been to: ").strip().split()
    countries2 = set()
    countries2.update(countries)
    countries = countries2.difference(countries1)
    str_countries = " ".join(map(str,countries))
    print(f"\nYour friend has gone to {str_countries} but you haven't.")
    countries = countries1.difference(countries2)
    str_countries = " ".join(map(str,countries))
    print(f"You have been to {str_countries} but your friend hasn't.")
    countries = countries1.intersection(countries2)
    str_countries = ",".join(map(str,countries))
    print(f"Both have been to: {str_countries}.")
    return countries1, countries2

def passengers():
    print("\nThis is the system's information:")
    passengers = {'G123456':{'Seat':'12A', 'Flight': 123},
             'G989494':{'Seat':'27D', 'Flight': 1009}}
    print(passengers)
    return passengers

def main():
    mylist = tasks()
    mytuple = store_tuple()
    myset1, myset2 = setset()
    mydict = passengers()

if __name__ == "__main__":
    main()