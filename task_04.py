#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04 Module"""


def process_data(data):
    """Defines a function that uses a loop to return a tuple

    Args:
        data (mixed): a list or tuple of numbers

    Returns:
        tuple: a tuple with the values for the sum and average of the data

    Examples:
        >>> process_data([1, 2, 3])
        (6, 2.0)

        >>> process_data([2, 4, 6])
        (12, 4.0)
    """

    data_sum = 0
    data_items = 0.0

    for number in data:
        data_sum += number
        data_items += 1.0

    return (data_sum, (data_sum / data_items))
