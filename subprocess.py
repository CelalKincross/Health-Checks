#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:18:46 2022

@author: w.yang-leeyoung
"""

import subprocess

print(subprocess.run(['date']))

# print(subprocess.run(['ls', '-a']))
#result = subprocess.run(['ls', '-a'])
result1 = subprocess.run(['cat', 'toseconds.py'])
print(subprocess.run(['sleep', '1']))
# print(result1.returncode)


result3 = subprocess.run(['host', '8.8.8.8'], capture_output=True)

print(result3.stdout.decode().split()) #decode for the b' bitcode to utf-8 string, split to separete the output 

result4 = subprocess.run(['rm', 'does_not_exist'], capture_output=True)

print(result4.stderr)




