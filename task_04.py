#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Function to calculate sum and average of a list of numbers."""


def process_data(data):
    """Uses a for loop to return tuple in order.

    Args:
        data (mixed): List or tuple of data.

    Returns:
        tuple: Containing sum and average with float precision of data input.

    Examples:
        >>> process_data([1,2,3])
        (6, 2.0)

        >>> process_data([25, 125])
        (150, 75.0)
    """
    sum_var = 0
    counter = 0.0

    for values in data:
        sum_var += values
        counter += 1.0

    average_var = sum_var / counter
    data = (sum_var, average_var)
    return data
