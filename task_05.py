#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mutability differences"""

def flip_keys(to_flip = []):
    """Reverses lists.

    Args:
        list

    Returns:
        reversed list

    Examples:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> print LIST
        [(3, 2, 1), 'cba']

    """

    return to_flip.reverse()
