#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Switch identification challenge

"""
You are now a Junior network engineer, not because your skills but because
you have to perform the dirty job.

Today, you have received an enormous list of equipment descriptions, from which
you have to identify the switch model and build up an inventory for the lab,
this is, the number of switches with each different model code you have already
organized the data in a super-fancy list of tuples with the following format:

(HN, SBS, SM, RU, 100GE)

HN = Hostname
SBS = Shared Buffer Space
SM = System Memory
RU = Rack Unit
100GE = Number of 100 GE Ports IN USE

Since you are a proficient DC network engineer, you must know how to identify
the switch model, I am joking, you have been told that EVERY switch are from
the Nexus 3400 series and  after looking into Cisco web page, you have access
to this comparison table:

https://www.cisco.com/c/en/us/products/switches/nexus-3000-series-switches/models-comparison.html#~tab-nexus3400

OBJECTIVE

Save the inventory in a appropriate data structure so that the Hostname data is
not lost and at the same time you can access the number of devices with that
model.

SIDE NOTE

You are about to learn how to cycle efficiently through a list of tuples in
your programming club sessions so in the meantime you start by classifying a
single device or you can try to build a for loop using the provided code:

for switch in total_switches:
    <YOUR CODE>
    # Accessing a single switch tuple (the "current" one)
    total_switches[switch]
    <MORE CODE>

Take single switch by using total_switches[1], the single_switch variable or
cycle through them with the for loop!

PS: If you are using a single switch your output dictionary might look awkward
but disregard that, use the proper data structure to display the inventory.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Ángel Niembro"]
__date__ = "2021/02/27"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

total_switches = [
    ("nx3k154", "70MB", "-", "1RU", 32),
    ("nx3k456", "20MB", "16GB", "1RU", 6),
    ("nx3k234", "70MB", "-", "4RU", 64),
    ("nx3k222", "22MB", "16GB", "2RU", 64),
    ("nx3k787", "70MB", "-", "4RU", 33)
    ]

single_switch = ("nx3k1", "70MB", "-", "1RU", 32)

# Here starts your code :=

def model(switches_tuple):
    i = 0
    switches_dictionary = {}
    for switch in switches_tuple:
        if switches_tuple[i][1] == "70MB":
            if switches_tuple[i][3] == "1RU":
                switches_dictionary[switch] = "Nexus 3432D-S"
            else:
                switches_dictionary[switch] = "Nexus 3408-S"
        elif switches_tuple[i][1] == "20MB":
            switches_dictionary[switch] = "Nexus 3464C"
        else:
            switches_dictionary[switch] = "Nexus 34180YC"
        i += 1
    return switches_dictionary

def main():
    total_switches.append(single_switch)
    switches_dictionary = model(total_switches)
    print(switches_dictionary)

if __name__ == "__main__":
    main()