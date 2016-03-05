#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1:2] = ['Swan Lake']

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote', 'Sylvia'])
