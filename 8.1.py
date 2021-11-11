#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 21:56:51 2021

@author: janaki
"""

runs1 = int(input('Enter runs1'))
runs2 = int(input('Enter runs2'))
runs3 = int(input('Enter runs3'))
runs4 = int(input('Enter runs4'))
total_runs=0
total_runs = runs1+runs2+runs3+runs4
average = total_runs/4
print('Average is %f' %(total_runs))
#print('Average is %s' %(format(average,'0.2f')))