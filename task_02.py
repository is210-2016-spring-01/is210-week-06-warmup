#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Standard List Functions"""

import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1:3] = ['Swan Lake']

BALLETS.append('Herman Scherman')

BALLETS.extend(['Don Quixote', 'Sylvia'])
