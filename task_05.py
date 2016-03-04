#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_05 Warmup for Lists and Tuples"""

def flip_keys(to_flip):
    """Reverse the order of the inner sequence
    Args:
        to_flip (list): List that has nested, immutable sequences inside
    Returns:
        list: The original list with its inner elements reversed
    Example:
    >>> LIST = [(1, 2, 3), 'abc']
    >>> NEW = flip_keys(LIST)
    >>> LIST is NEW
    True
    >>> print LIST
    [(3, 2, 1), 'cba']
    """
    num = 0
    for seq in to_flip:
        seq[::-1]
        num += 1
        return to_flip
