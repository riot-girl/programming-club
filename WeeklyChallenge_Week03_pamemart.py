#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 1. Weekly Challenge3: Create an expense calculator with python

For this weekly challenge we will need to do a little calculator that asks for 
a monthly income, the amount of expenses that were made on the month, and for 
each one, concept of the expense and the amount. After getting all the 
information, you should display a formatted report of the expenses as well as 
the amount left for the rest of the month.
"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Alexis Gómez"]
__date__ = "2021/02/26"
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
        print(f"{input} is not a valid number.")
        return ValueError

def capture_expenses(items):
    expenses = []
    totalexp = 0
    print("\n\n-------------- Capturing the Expenses --------------")
    print("\nPlease enter the amount followed by the concept of your expense, "
    "separated by a comma.\ne.g. 400,Hyrule Warriors expansion")
    for i in range(items):
        expense = []
        while len(expense) !=2:
            amount = ValueError
            while amount == ValueError:
                expense = input(f"\nExpense {i+1}: ").strip().split(',')
                amount = expense[0]
                amount = check_input(amount)
            if len(expense) != 2:
                print("Incorrect number of arguments. Please enter the amount "
                "followed by the concept of your expense separated by a comma."
                "\ne.g. 400, Hyrule Warriors expansion")
        expenses.append(expense)
        totalexp += amount
        i += 1
    return expenses, totalexp

def print_report(income, items, expenses, totalexp):
    print("\n\n\n************************** Expense Report *************************")
    for i in range(items):
        print (f"{expenses[i][1]} ................. ${expenses[i][0]}")
    print(f"Montly income: ${income:.2f}")
    print(f"Montly purchases: {items} - Total spent: ${totalexp:.2f}")
    print(f"Money left: {income - totalexp:.2f}")
    

def main():
    print("############### Welcome to your Expense Calculator ###############")
    income = ValueError
    while income == ValueError:
        income = input("\nEnter the monthly income: ")
        income = check_input(income)
    items = ValueError
    while items == ValueError:
        items = input("\nEnter the total of expenses to be captured: ")
        items = int(check_input(items))
    expenses, totalexp = capture_expenses(items)
    print_report(income, items, expenses, totalexp)
        
if __name__ == "__main__":
    main()