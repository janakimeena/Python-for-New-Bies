#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:17:37 2021

@author: janaki
"""

principal = int(input('Principal '))
rate = float(input('Rate '))
years = int(input('Years '))
times = int(input('times '))
amount = principal*(1+rate/(100*times))**(years*times)
print(amount)
