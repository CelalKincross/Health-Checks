#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:08:40 2022

@author: w.yang-leeyoung
"""
import re
def extract_pid(log_line):
    result = re.search(r"\[(\d+)\]", log_line)
    if result != None:
        print(result[1])
    else:
        print("No pids found")
    
    


#log_line = "this text has a [car]"
#extract_pid(log_line)
