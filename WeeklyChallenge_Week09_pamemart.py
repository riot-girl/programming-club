#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 1. Weekly Challenge 9: Parse Avaya PBX dump to Cisco phone information
You are a new team member to the collab team, you’re given the task to parse a 
complete Avaya dump and create a new file having the cisco equivalent to that 
same configuration.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Alexis Gómez"]
__date__ = "2021/03/01"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

def read_file(name):
    # reading file 'name'
    file = open(name, 'r')
    # creating an array of 'lines' rows
    lines = []
    for line in file:
        if len(line) > 1:
            # split each row in colums
            row = [] 
            word = ""
            for letter in line:
                if letter != ',' and letter != '\n':
                    word += letter
                else:
                    row.append(word)
                    word = ""
        lines.append(row)
    file.close()
    return lines

def convert(lines, name):
    # reading file 'name'
    file = open(name, 'w')
    # creating headers
    file.write("extension,name,#_line_buttons,#_blfs_buttons,"
    "#_speeddial_buttons,cisco_model\n")
    i = 0
    # reading 'lines' content
    for line in lines:
        i += 1
        # if plk_count > 0
        if len(line[4]) > 0 and line[4] != 'plk_count':
            # adding extension and name info 
            file.write(line[0]+',')
            file.write(line[1]+',')
            # initializing variables to count buttons
            line_buttons = 0
            blfs_buttons = 0
            speed_dial = 0
            j = i
            # adding buttons
            while j < i+int(line[4]):
                if lines[j][2] == "Line (ring)":
                    line_buttons += 1
                if lines[j][2] == "BLF":
                    blfs_buttons += 1
                if lines[j][2] == "Speed-dial":
                    speed_dial += 1
                j += 1
            # selecting phone model
            totalb = line_buttons + blfs_buttons + speed_dial
            model = '8841' if totalb < 6 else '8851'
            kem = 1 + int((totalb-5)/36) 
            model = model+' + '+str(kem)+' KEMs' if totalb > 5 else model
            # adding buttons and model info
            file.write(str(line_buttons)+',')
            file.write(str(blfs_buttons)+',')
            file.write(str(speed_dial)+',')
            file.write(model+'\n')
    file.close()       

def main():
    lines = read_file('Weekly Challenge 9.csv')
    convert(lines,'Weekly Challenge 9b.csv')

if __name__ == "__main__":
    main()