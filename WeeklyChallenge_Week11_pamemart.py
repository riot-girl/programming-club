#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 1. Weekly Challenge 11: Regex II

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Ángel Niembro"]
__date__ = "2021/03/04"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"


import re


"""
You feel really confident with your Python skills and ask to the project 
architect to assign the responsibility over a missing feature, after realizing 
that you have just learn everything about RegEx, she asks you to write a code 
which analyze a log file and respond to some questions.

The customer provide a sample of the log file, which should be considered only 
as a tiny portion of the total of the daily generated logs, mentioning that 
most of them have a correct formatting (TIMESTAMP – SEVERITY - MSSG).

As part of the first development phase, your code must read this log file and 
answer to the following questions:
1. When did the first warning occurred?
2. Print the logs which does not match the standard format.
3. List the different severities and its appearance count
4. After analyzing the logs, provide some log formatting recommendations to the
customer (as comments at the beginning of your code)
"""


def read_file(name):
    # reading file 'name'
    file = open(name, 'r')
    # returning values row by row
    return (row for row in file)

def first_warning(pattern_date, pattern_warning,file):  
    logs = read_file(file)  
    for line in logs:
        date = re.findall(pattern_date, line)
        warning = re.findall(pattern_warning, line)
        if warning:
            print(f'Date and time of first warning: {date[0]}.\n')
            break

def unformatted(pattern,file):
    logs = read_file(file)
    for line in logs:
        format = re.search(pattern, line)
        if format == None:
            print(f'Bad format: {line}')

def severities (file):
    patterns = {
        'error' : '^\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}\s\[ERROR\]',
        'warning' : '^\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}\s\[WARNING\]',
        'info' : '^\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}\s\[INFO\]',
        'debug' : '^\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}\s\[DEBUG\]'
        }
    levels = {}
    while patterns:
        logs = read_file(file)
        level = patterns.popitem()
        counter = 0
        for line in logs:
            if re.search(level[1], line):
                counter += 1
        levels[level[0]] = counter
    print(f'Total messages')
    print(f'--------------')
    while levels:
        level = levels.popitem()
        print(f'{level[0]} - {level[1]}')

def main():
    patterns = {
        'date' : '^\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}',
        'warning' : '^\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}\s\[WARNING\]',
        'format' : '^\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}\s\[([A-Z])+\]\s.*$'
    }
    file = 'Weekly Challenge 11_log_sample.log'
    first_warning(patterns['date'],patterns['warning'],file)
    unformatted(patterns['format'],file)
    severities(file)


if __name__ == "__main__":
    main()