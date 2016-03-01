#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mutability differences between strings and tuples."""


def flip_keys(to_flip):
    """Function to flip order of sequence.

    Args:
        to_flip (list): A list of mixed data types.

    Returns:
        list: A reversed list of data.

    Examples:
        >>> flip_keys([(6, 7), 'ab', 'olleh', (3, 2, 1)])
        [(1, 2, 3), 'hello', 'ba', (7, 6)]
        >>> flip_keys(['ab', 'yup', (3, 23, 1)])
        [(1, 23, 3), 'puy', 'ba']
    """
    counter = 0
    for item in to_flip:
        item = item[::-1]
        to_flip[counter] = item
        counter += 1
    return to_flip
