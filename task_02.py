#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02 Warmup for Lists and Tuples"""

import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1] = 'Swan Lake'

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote', 'Sylvia'])
