#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_04 Warmup for Lists and Tuples"""

def process_data(data):
    """Returns a tuple containing the total sum of the data and the average
       of the data

    Args:
        data (mixed): A list or tuple of numbers

    Returns:
        tuple: a tuple containing the total sum of the data and the average
               of the data with floating point precision
    Example:
        >>> process_data([1, 2, 3])
             (6, 2.0)
    """
    mysum = 0
    for mynum in data:
        mysum += mynum
    myavg = (mysum / float(len(data)))
    return (mysum, myavg)

