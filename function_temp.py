# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:25:10 2021

@author: Manish Kumar Goswami
"""

def temp_conv(x):
    f = 9/5*x +32
    print("Temprature in F is",f)
def time_conv(y):
    minu = y*60
    sec = y*60*60
    print("Time in min is",minu)
    print("Time in sec is",sec)
    
temp_conv(37)
time_conv(34)

