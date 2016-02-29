#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exploring the for loop."""


def process_data(data):
    """A processing function.

    Args:
        data (list or tuple): Set of numbers.

    Returns:
        tuple: Total sum and average.

    Examples:
        >>> process_data([1, 2, 3])
        (6, 2.0)
        >>> process_data([20, 6, 3, 19])
        (48, 12.0)
    """
    total = 0
    count = 0
    for num in data:
        total += num
        count += 1
    return total, (float(total) / count)
