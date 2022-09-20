#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:00:07 2022

@author: w.yang-leeyoung
"""


import csv

def read_employees(csv_file_location):
    with open(csv_file_location) as f:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        reader = csv.DictReader(f, dialect='empDialect')
        employee_list=[]
        for data in reader:
            employee_list.append(data)
    return employee_list

employee_list = read_employees("~/employee.csv")
print(employee_list)