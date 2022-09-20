#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:36:09 2022

@author: w.yang-leeyoung
"""

def to_seconds():
    
    cont = "y"
    
    while cont.lower() == 'y':
        hours = int(input('please enter hours '))
        minutes = int(input('please enter minutes '))
        seconds = int(input('please enter hours seconds '))
        seconds_in_hours = hours * 60 * 60
        seconds_in_minutes = minutes * 60
        total_seconds = seconds + seconds_in_minutes + seconds_in_hours
        print('There are {} seconds in {} hours, {} minutes, and {} seconds'.format(total_seconds, hours, minutes, seconds))
        cont = input("Would you like to do another conversion? ")
        
to_seconds()
        