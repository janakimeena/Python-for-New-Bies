#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 21:40:23 2021

@author: janaki
"""

money_in_hand = int(input('Enter money in hand'))
choc_price = int(input('Price of one chocolate'))
wrapper_free = int(input('Free chocolates wrapper'))
choc_bought = money_in_hand//choc_price
free_choc = choc_bought//wrapper_free
total_choc = choc_bought+free_choc
print('Choc bought is %d Free chocolates is %d Total number of chocolates %d' %(choc_bought,free_choc,total_choc))