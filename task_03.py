#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03"""


import copy
import data

DIRECTIONS = copy.copy(data.DIRECTIONS)

DIRECTIONS = DIRECTIONS[:-1] + ("West",)
