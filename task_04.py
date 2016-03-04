#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 4 file."""


def process_data(data):
    """ To calculate the sum & the average of the data set.

    Args:
        data(mixed): to calculate the sum of the data set.

    Returns:
        mixed: the sum & the average of the data set.

    Examples:

        >>> process_data([1, 2, 3])
        '(6, 2.0)'

        >>> process_data([2, 4, 6])
        '(12, 4.0)'
    """
    for x in data:
        x += x
        return (sum(data), sum(data)/float(len(data)))
