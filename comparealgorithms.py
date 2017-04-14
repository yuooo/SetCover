# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:05:27 2017

@author: jessicahoffmann
"""

import setcover

#%%
element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]


usual_greedy(element1, sets1, False)

element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]
heuristic_frequency1(element1, sets1, True)

element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]
heuristic_frequency2(element1, sets1, True)

element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]
heuristic_frequency3(element1, sets1, True)