#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:37:52 2022

@author: w.yang-leeyoung
"""

import os, subprocess

my_env = os.environ.copy()
my_env['PATH'] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

print(my_env['PATH'])
result = subprocess.run(['myapp'], env=my_env)