#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""


def process_data(*data):
    """takes one arg: data. a list or tuple of numbers"""
    total = ()
    avg = ()
    for total in data:
        total = sum(*data)
    for avg in data:
        avg = total/float(len(*data))
    return (total, avg)
