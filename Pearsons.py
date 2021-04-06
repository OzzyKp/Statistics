#!/usr/bin/env python
# coding: utf-8

# Function built to calculate Pearson's R, function designed to breakdown each step required to calculate R
def pearsons(x,y):
    # import neccessary library - numpy
    import numpy as np
    # ensure that the len of x is the same as y and ensure that x,y is not empty
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    # Convert x,y into numpy arrays unless already an array
    x = np.asarray(x)
    y = np.asarray(y)
    # Create neccessary variables to calculate Pearson's R
    x_total = sum(x)
    y_total = sum(y) 
    xy = sum(x * y)
    x_sq = sum(x**2)
    y_sq = sum(y**2)   
    # Calculate Pearson's R
    r = ((n * xy) - (x_total* y_total)) / np.sqrt((((n * x_sq) - (x_total**2)) * ((n * y_sq) - (y_total**2))))
    
    return r
    







