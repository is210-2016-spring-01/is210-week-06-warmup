#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Function to calculate sum and average of a list of numbers."""


def flip_keys(to_flip):
    """A function to reverse order of sequence to show mutability.

    Args:
        to_flip (list): Input list of values to flip.

    Returns:
        list: Original list in reverse order.

    Examples:
        >>> flip_keys(['monkey]', [1, 2, 3], 'banana'])
        [']yeknom', [3, 2, 1], 'ananab']

        >>>>>> flip_keys(['baba', 'booey'])
        ['abab', 'yeoob']
    """
    counter = 0
    for list_item in to_flip:
        to_flip[counter] = list_item[::-1]
        counter += 1

    return to_flip
