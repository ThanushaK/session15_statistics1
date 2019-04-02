# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:56:08 2019

@author: thanusha
"""
import numpy as np                 #importing numpy library
#import scipy.stats
#import matplotlib.pyplot as plt
# 1
x= [1550,1700,900,850,1000,950]      #given list of numbers
std=np.std(x)                        #standard deviation from numpy library
print("Standard deviation is {:.2f}" .format(std))     #print the standard deviation result with two decimals after point

#2
x = [3,21,98,203,17,9]    #given list of numbers
variance = np.var(x)           #variance from numpy library
print("variance is {:.2f}" .format(variance))         

