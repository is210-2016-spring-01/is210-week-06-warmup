#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Working with for loops"""

def process_data(data):
    """A lovely docstring is located here.
    
    Takes input number, calculates net and average. Returns tuple.
    
    Args:
        data (int): contains interger-related data.
    
    Returns:
        net (int): net of all the given numbers
        avg (float): average of all numbers 

    Example:
        >>> process_data([1, 2, 3])
        (6, 2.0)
    """
    net = 0
    for number in data:
        net += number
    equals = (net, net/float(len(data)))
    return equals