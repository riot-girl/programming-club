#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 1. Weekly Challenge 8: Packages Creation and Installation: Policy 
compliance in daily meals expenses amount.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Martin Escorza"]
__date__ = "2021/03/01"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

import pycountry
import requests
import json
import cv2

def check_input(input):
    try:
        # Convert it into number
        val = float(input)
        return val
    except ValueError:
        print(f"{input} is not a valid number.")
        return ValueError

def exrate():
    # pulling the currency info from exchangerate-api.com
    json_data = requests.get('https://api.exchangerate-api.com/v4/latest/'
    'USD').json()
    # displaying the currency options
    while json_data['rates']:
        countrycode = json_data['rates'].popitem()[0]
        print(f"{countrycode}.- ", end=" ")
        for i in range(0,len(pycountry.currencies)-1):
            country = list(pycountry.currencies)[i]
            if country.alpha_3 == countrycode:
                print(f"{country.name}")
    currency = ''
    json_data = requests.get('https://api.exchangerate-api.com/v4/latest/'
    'USD').json()
    while json_data['rates'].get(currency) == None: 
        # "currency" variable is the 3 letters code introduce by program user.
        currency = input("Select the currency of expenses made: ").upper()
        # validating 'currency' is a valid code
        if json_data['rates'].get(currency) == None:
            print("Incorrect value, try again.")
    # 'json_rate' is the exchange currency vs USD
    json_rate = 1 / json_data['rates'][currency]
    print(f"Exchange rate: 1 {currency} equals {json_rate:.2f} USD.")
    return json_rate, currency

def capture_expenses(currency):
    # 'expenses' is a list with all the expenses to be captured
    expenses = []
    # in 'totalexp' we will store the total spent
    totalexp = 0
    print("\n\nPlease introduce items.")
    # 'cont' -> variable fo flag if we wish to continue capturing expenses
    cont = True
    i = 0
    while cont == True:
        # expense is a list for each expense [concept, amount]
        expense = [0, 0]
        expense[0] = (input(f"Concept {i+1}: "))
        # validating that expense[1], which is the amount, is a valid number
        expense[1] = ValueError 
        while expense[1] == ValueError:
            expense[1] = input(f"Amount {i+1} ({currency}): ")
            expense[1] = check_input(expense[1])
        totalexp += expense[1]
        expenses.append(expense)
        # Do you want to continue? loop
        yesno = ''
        while yesno != 'yes' and yesno != 'no':
            yesno = input("Do you want to add another item? " 
            "(Yes/No): ").lower()
            cont = True if yesno == 'yes' else False
        i += 1
    return expenses, totalexp

def print_report(expenses, totalexp, currency, json_rate):
    # printing expenses report
    print("\n\n\nExpenses Report")
    print("***************")
    print(f"Concept\tAmount{currency}\tAmount (USD)".expandtabs(30))
    print("==================================================================="
    "=====")
    i = 0
    for items in expenses:
        print(f"{expenses[i][0]}\t{expenses[i][1]:.2f}\t"
        f"{expenses[i][1]*json_rate:.2f}".expandtabs(30))
        i += 1
    print("-------------------------------------------------------------------"
    "-----")
    # printing totals
    print(f"Totals:\t{totalexp} {currency}\t{totalexp*json_rate:.2f}"
    " USD".expandtabs(30))
    

def main():
    json_rate, currency = exrate()
    expenses, totalexp = capture_expenses(currency)
    print_report(expenses, totalexp, currency, json_rate)
    image = (cv2.imread("compliance.jpg") if totalexp*json_rate < 100 
    else cv2.imread("noncompliance.jpg"))
    cv2.imshow("Title", image)
    cv2.waitKey()


if __name__ == "__main__":
    main()