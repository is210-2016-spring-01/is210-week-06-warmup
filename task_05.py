#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05 Module"""


def flip_keys(to_flip):
    """Defines a function that

    Args:
        to_flip (list): A list containing nested, immutable sequences

    Return:
        list: the original list containing the inner sequence in reverse order

    Examples:
    >>> LIST = [(1, 2, 3), 'abc'}
    >>> NEW = flip_keys(LIST)
    >>> LIST is NEW
    True
    >>>print LIST
    [(3, 2, 1), 'cba']

    >>> LIST = [(2, 5, 8), 'hello'}
    >>> NEW = flip_keys(LIST)
    >>> LIST is NEW
    True
    >>>print LIST
    [(8, 5, 2), 'olleh']
    """

    counter = 0

    for value in to_flip:
        to_flip[counter] = value[::-1]
        counter += 1

    return to_flip
