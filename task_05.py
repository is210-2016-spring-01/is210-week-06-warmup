#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 6 warmup task with a function to flip values in a list"""


def flip_keys(to_flip):
    """Processes a list of data and returns the same list with inverted values.

    Args:
        data (list): list of data elements to process

    Returns:
        list: the same list with each element reversed.

    Examples:
        >>> process_data[(1, 2, 3), 'spam', 'eggs']
        [(3, 2, 1), 'maps', 'sgge']
    """

    count = 0

    for value in to_flip:

        to_flip[count] = value[::-1]      # replace item with revrsed value

        count += 1                        # keep track of number of elements

    return to_flip
