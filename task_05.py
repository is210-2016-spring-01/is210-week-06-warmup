#!use/bin/env python
# -*- coding: utf-8 -*-
"""Week Six Lists And Tuples."""


def flip_keys(to_flip):
    """Does flip the list as return.

    Args:
        LIST (tuple): Argument to be reversed.

    Returns:
        tuple: the result of the argument reversion.

    Examples:

        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']
    """
    for i in enumerate(to_flip):
        to_flip[i] = to_flip[i][::-1]
    return to_flip
