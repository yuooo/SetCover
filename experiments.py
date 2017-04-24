# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:57:11 2017

@author: jhh2677
"""
import setcover

#%% A few examples to try stuff out

# instance 1
element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]
#setcover.usual_greedy(element1, sets1, False)

element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]
#setcover.heuristic_frequency1(element1, sets1, False)

element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]
#setcover.heuristic_frequency2(element1, sets1, False)

element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]
#setcover.heuristic_frequency3(element1, sets1, False)

element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]
#setcover.heuristic_frequency4(element1, sets1, False)

# instance 2
element1 = {'a': 0, 'b': 0, 'c': 0, 'd':0}
sets1 = [(8, {'a':0, 'b':0}), \
(7, {'c':0, 'd':0}), \
(9, {'b':0, 'c':0, 'd':0})]
#setcover.usual_greedy(element1, sets1, False)

element1 = {'a': 0, 'b': 0, 'c': 0, 'd':0}
sets1 = [(8, {'a':0, 'b':0}), \
(7, {'c':0, 'd':0}), \
(9, {'b':0, 'c':0, 'd':0})]
setcover.heuristic_frequency1(element1, sets1, True)

element1 = {'a': 0, 'b': 0, 'c': 0, 'd':0}
sets1 = [(8, {'a':0, 'b':0}), \
(7, {'c':0, 'd':0}), \
(9, {'b':0, 'c':0, 'd':0})]
#setcover.heuristic_frequency2(element1, sets1, False)

element1 = {'a': 0, 'b': 0, 'c': 0, 'd':0}
sets1 = [(7, {'a':0, 'b':0}), \
(7, {'c':0, 'd':0}), \
(9, {'b':0, 'c':0, 'd':0})]
#setcover.heuristic_frequency3(element1, sets1, False)

element1 = {'a': 0, 'b': 0, 'c': 0, 'd':0}
sets1 = [(8, {'a':0, 'b':0}), \
(7, {'c':0, 'd':0}), \
(9, {'b':0, 'c':0, 'd':0})]
#setcover.heuristic_frequency4(element1, sets1, False)

#%%

# instance 1
element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(9, {'b':0}), \
(8, {'b':0, 'c':0})]
setcover.brute_force_not_smart(element1, sets1)