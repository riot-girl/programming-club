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


def validate_chars():
    test = False
    while test == False:
        password = input("Type the new password: ")
        test = False if password[0] == '.' or password[0] == '-' or password[-1] == '.' or password[-1] == '-' else True
        if test == False:
            print ("Incorrect password, . or - are not allowed at the beginning nor at the end")
    return password

def validate2(password):
    test = False
    while test == False:
        password2 = input("Type the new password again: ")
        test = True if password == password2 else False
        if test == False:
            print ("Passwords are not the same, try again.")
