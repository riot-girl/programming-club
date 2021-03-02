#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 1. Weekly Challenge 7: Creating users
In this weekly challenge you will be doing everything with your own functions that are located
in a module that will be created by you as well.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Diego Zaragoza"]
__date__ = "2021/02/28"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

from WeeklyChallenge_Week07mod_pamemart import validate_chars, validate2

def main():
    print("Welcome to the user generator tool")
    print("---------------------------------")
    name = input("Please type the First user name: ")
    password1 = validate_chars()
    validate2(password1)
    name = input("Please type the Second user name: ")
    password2 = validate_chars()
    validate2(password2)
    
if __name__ == "__main__":
    main()