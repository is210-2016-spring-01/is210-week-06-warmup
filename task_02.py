#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 6 warmup task to interact with existing lists"""

import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1] = 'Swan Lake'

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote', 'Sylvia'])
