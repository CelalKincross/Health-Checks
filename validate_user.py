#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:05:33 2022

@author: w.yang-leeyoung
"""

def validate_user(username, minlen):
    assert type(username) == str, 'username must be a string'
    if minlen < 1:
        raise ValueError("minlen must be at least one")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
