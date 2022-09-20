#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:57:23 2022

@author: w.yang-leeyoung
"""

import re
import sys

logfile = sys.argv[1]
pattern = r'USER \((\w+)\)$'
usernames={}

with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        result = re.search(pattern, line)
        name = result[1]
        if name == None:
            continue
        usernames[name] = usernames.get(name, 0) + 1
    f.close()       
print(usernames)
        


            