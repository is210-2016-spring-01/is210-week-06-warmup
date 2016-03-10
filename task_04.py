#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 6 warmup task to interact with existing lists"""


def process_data(data):
    """Processes a collection of numeric data and return the sum and average.

    Args:
        data (list): list of numbers to be processed

    Returns:
        tuple: A tuple consisting of the sum of the numbers and their average.

    Examples:
        >>> process_data([2, 3, 4, 5])
        (14, 3.5)
    """

    count = 0
    current_total = 0

    for num in data:

        count += 1                          # keep track of number of elements
        current_total += num                # revise total for number set

    return (current_total, current_total / (0.0 + count))
