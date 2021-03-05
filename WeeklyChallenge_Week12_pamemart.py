#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Level 1. Weekly Challenge 12: Exception Handling

You need to create a file handler menu with the following options:
- Create
- Read
- Save to File
- Exit

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Daniel Medina"]
__date__ = "2021/03/04"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

from os import error, system
import time
from getpass import getpass

def check_input(input):
    try:
        # Convert input into number
        val = int(input)
        if val < 1 or val > 3:
            print(f"{input} is not a valid number.\n\n")
            time.sleep(1)
            return ValueError
        else:
            return val
    except ValueError:
        print(f"{input} is not a valid number.\n\n")
        time.sleep(1)
        return ValueError

def check_number(input):
    try:
        # Convert input into number
        val = float(input)
        return val
    except ValueError:
        print(f"{input} is not a valid number.\n\n")
        time.sleep(1)
        return ValueError

def menu():
    option = ValueError
    while option == ValueError:
        system('clear')
        print('Menu:')
        print ('1. Create File')
        print ('2. Read File')
        print ('3. Save to File')
        print ('Exit with Ctrl+C')
        option = input('\nOption: ')
        option = check_input(option)
    return option

def create():
    try:
        filename = input('\nFilename: ')
        file = open(filename, 'x')
    except FileNotFoundError:
        print('You must enter a filename.\n')
        time.sleep(1)
        return error
    except FileExistsError:
        print('File alredy exists.\n')
        time.sleep(1)
        return error
    except OSError as exc:
        if exc.errno == 36:
            print ("Your filename is too long, try again.\n")
            time.sleep(1)
            return error
    except KeyboardInterrupt:
        return 'exitprogram'
    except:
        print('Something went wrong.\n')
        time.sleep(1)
        return error
    else:
        print(f'{filename} created.')
        time.sleep(2)
    finally:
        file_exists = 'file' in locals() or 'file' in globals()
        if file_exists:
            file.close()
         
def read():
    try:
        filename = input('\nFilename: ')
        file = open(filename, 'r')  
    except FileNotFoundError:
        print ("Filename does not exist, try again.\n")
        time.sleep(1)
        return error
    except OSError as exc:
        if exc.errno == 36:
            print ("Your filename is too long, try again.\n")
            time.sleep(1)
        return error
    except KeyboardInterrupt:
        return 'exitprogram'
    except:      
        print('Something went wrong.\n')
        time.sleep(1)
        return error
    else:
        print(file.readlines())
        enter = getpass('\n\nPresiona ENTER para regresar al menú principal.')
    finally:
        file_exists = 'file' in locals() or 'file' in globals()
        if file_exists:
            file.close()

def save():
    try:
        number1 = ValueError
        while number1 == ValueError:
            number1 = input(f'Insert first number: ')
            number1 = check_number(number1)
        number2 = ValueError
        while number2 == ValueError:
            number2 = input(0000000f'Insert second number: ')
            number2 = check_number(number2)
        filename = input('\nFilename: ')
        file = open(filename, 'w')
        result = number1/number2
        file.write(str(result))
    except FileNotFoundError:
        print ("You need to enter a filename, try again.\n")
        time.sleep(1)
        return error
    except OSError as exc:
        if exc.errno == 36:
            print ("Your filename is too long, try again.\n")
            time.sleep(1)
            return error
    except KeyboardInterrupt:
        return 'exitprogram'
    except ZeroDivisionError:
        print('Cannot divide by zero, try again.\n')
        time.sleep(1)
        return error
    except:      
        print('Something went wrong.')
        time.sleep(1)
        return error
    else:
        print (f'{number1} * {number2} = {result}')
        enter = getpass('\n\nPresiona ENTER para regresar al menú principal.')
    finally:
        file_exists = 'file' in locals() or 'file' in globals()
        if file_exists:
            file.close()
        
def main():
    try:
        continuate = True
        flag = error
        while continuate:
            option = menu()
            if option == 1:
                flag = error
                while flag == error:
                    flag = create()   
            elif option == 2:
                flag = error
                while flag == error:
                    flag = read()
            elif option == 3:
                flag = error
                while flag == error:
                    flag = save()
            if flag == 'exitprogram':
                print('\n\n¡Adiós!\n\n')
                break
    except KeyboardInterrupt:
        print('\n\n¡Adiós!\n\n')

if __name__ == "__main__":
    main()