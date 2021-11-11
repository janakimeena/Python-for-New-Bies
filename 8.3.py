#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:08:52 2021

@author: janaki
"""

cost_comp = int(input('Cost comp '))
cost_table = int(input('One Table '))
cost_chair = int(input('One chair '))
one_hour_wages = int(input('Wages one hour '))
num_comp = int(input('Number of comp'))
num_tables = int(input('Number of tables'))
num_chairs = int(input('Number of chairs'))
num_hours = int(input('Number of hours'))
comp_cost = cost_comp*num_comp
chair_cost = cost_chair*num_chairs
table_cost = cost_table*num_tables
total_wages = one_hour_wages*num_hours
budget = comp_cost+chair_cost+table_cost+total_wages
print('Budget is %d' %(budget))