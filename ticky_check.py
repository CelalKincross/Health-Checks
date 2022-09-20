#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#scp -i .\qwikLABS-LXXXX-1XXXXXXX.pem .\ticky_check.py student-XX-xxxxxxxxxxxx@XX.XXX.XX.XXX:/home/student-XX-xxxxxxxxxxxx
"""
Created on Sun May  1 13:27:38 2022

@author: w.yang-leeyoung
"""

import re, sys, operator, csv

# create a report for error messages, and per user usage. Per user usage returns 
# a report sorted by user name with number of info tickets and error tickets. Error
# message report returns error type sorted by highest to lowest frequency
file = sys.argv[1]
pattern = r"ticky: (ERROR|INFO) ([\w' ]*)\[?#?\d*\]? \((\w*\.?\w*)\)"

# Dictionaries to populate
errors = {}
user_usage = {}
thisDict = {}



# function to get user name, message type, and message in each line of log
def get_data(line):   
        result = re.search(pattern, line)
                
        mtype = result.group(1)
        msg = result.group(2)
        user = result.group(3)
        return mtype, msg, user

# function to populate errors
def get_error(line, msg):
    if "ERROR" in line:
        errors[msg] = errors.get(msg, 0) + 1

# function to populate user stats
def get_user_usage(user, mtype):
    if user not in user_usage:
        user_usage[user] = {"INFO": 0,"ERROR": 0} 
    user_usage[user][mtype] += 1

# function to create errors csv file
def error_stats_csv(csv_file):
    # create csv file
    error_header = ['Error', 'Count']
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(error_header)
        writer.writerows(errors)

# function to create user stats csv file
def user_stats_csv(csv_file):

    # create csv file
    user_header = ['Username', 'INFO', 'ERROR']
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(user_header)
        for line in user_usage:
            writer.writerow([line[0], line[1]["INFO"], line[1]['ERROR']])
  

if __name__ == "__main__":
    with open(file, 'r') as f:

        for log in f.readlines():
            line = log.strip()
            mtype, msg, user = get_data(line)

        
            #organize data into an errors dict and a per user usage dict
            get_error(line, msg)
            
            #user usage dictionary
            get_user_usage(user, mtype)

    f.close()
    
    #sort errors by quantity- most to least and create csv error file
    errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
    #create csv
    error_stats_csv("error_message.csv")
    
    # sort user stats by name and create csv stats file
    user_usage=sorted(user_usage.items())
    # create csv
    user_stats_csv("user_statistics.csv")
    
