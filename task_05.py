#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 5 docstring."""


def flip_keys(to_flip):
    """Returning the original list with its inner elements reversed.

    Args:
        to_flip = tuple with list to be reversed

    Returns:
        integer: reversed
        string:  reversed

    Examples:

       >>> LIST = [(1, 2, 3), 'abc']
       >>> NEW = flip_keys(LIST)
       >>> LIST is NEW
       True
       >>> print LIST
       [(3, 2, 1), 'cba']
    """
    counter = 0
    for items in to_flip:
        to_flip[counter] = items[::-1]
        counter += 1
    return to_flip
