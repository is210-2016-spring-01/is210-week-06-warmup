#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a module"""


def process_data(data):
    """Function returns the sum and average of a tuple data set

    Args:
        data(mixed): String or numbers in a tuple set

    Returns:
        mysum (int): Sum of the tuple data set
        myavg (int): Average of the tuple data set

    Example:

        >>> process_data([1, 2, 3])
        (6, 2.0)

    """
    mysum = 0
    for mynum in data:
        mysum += mynum

    myavg = (mysum / float(len(data)))
    return (mysum, myavg)
