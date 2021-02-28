#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 1. Weekly Challenge 6: Let's create a name game!

For this challenge you will need to create a game that will give you your 
Villain name based on the first letter of your name and your birth month.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Daniel Medina"]
__date__ = "2021/02/27"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

import datetime

Sample=['Goblin', 'Creature', 'Troll', 'King/Queen', 'Witch/Warlock', 
        'Vampire', 'Guardian', 'Fairy', 'Knight', 'Elf', 'Assasin', 
        'Sorcerer/Sorceress', 'Giant', 'Warewolf', 'Wizard', 'Ogre', 'Goblin',
        'Beast', 'Dragon', 'Ghost', 'Dwarf', 'Giant', 'Unicorn', 'Warrior', 
        'Spirit', 'Thief', 'Cyclops', 'Troll', 'Orc', 'Vampire']

string=("The Black,The Vengeful,The Dark,The Red,The Cursed,The Savage,"
"The White,The Ugly,The Treacherous,The Blue,The Wicked,The Green")

months={'Jan': '', 'Feb': '', 'Mar': '', 'Apr': '', 'May': '', 'Jun': '', 
       'Jul': '', 'Aug': '', 'Sep': '', 'Oct': '', 'Nov': '', 'Dec': ''}

def remove_repeated(list):
    i = 0
    dictionary = {}
    for name in list:
        j = 0
        letter = chr(ord('a') + i) 
        dictionary[letter] = list[i]
        for name in list:
            if i < j and list[i] == list[j]:
                list.pop(j)
            j += 1
        i += 1
    return dictionary

def convert_to_list(string):
    list = string.split(',')
    i = 0
    dictionary = {}
    for month in months:
        dictionary[month] = list[i]
        i += 1
    return dictionary

def check_input(input):
    try:
        # Convert it into number
        val = int(input)
        val = ValueError if val<1 or val>12 else val
        return val
    except ValueError:
        print(f"{input} is not a valid number.")
        return ValueError

    
def main():
    mydictionary1 = remove_repeated(Sample)
    mydictionary2 = convert_to_list(string)
    
    print("¡Hola!... qué bueno que estés de vuelta en python.")
    print("¡Esta vez nos vamos a divertir mucho!")
    print("Disculpa que te pregunte de nuevo, no tengo buena memoria.")
    name = input("\n¿Me podrías repetir tu nombre? ").lower()
    print("\n¡Oh, pero claro! ya recordé esa cara...")
    print("Te voy a ser muy honesto, tampoco recuerdo tu mes de nacimiento,"
    "estar encerrado en casa me ha afectado la memoria.\nTe juro que no "
    "vuelve a pasar, de hecho recuerdo mejor los números que los meses.")
    month = ValueError
    while (month == ValueError):
        month = input("\n¿En qué número de mes naciste? ")
        month = check_input(month)
    print("\nComo has sido muy paciente conmigo, te voy a dar algo único.\n\n"
    "Te ves emocionado, ya no puedo soportarlo, te lo diré.\n¡Quiero decirte"
    "tu nombre de VILLANO!\nQue es...")
    monthstr = datetime.date(1922, month, 1).strftime('%b')
    print(f"\n\n¡¡¡{mydictionary1[name[0]]} {mydictionary2[monthstr]}!!!")


if __name__ == "__main__":
    main()