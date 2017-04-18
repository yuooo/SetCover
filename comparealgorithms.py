# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:05:27 2017

@author: jessicahoffmann
"""

import setcover
import data_set
import numpy as np

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
#setcover.heuristic_frequency1(element1, sets1, False)

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

# DATA SETS: http://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html

results = np.array([])
datasets = range(41,50) + range(51,60) + range(61,66) + [410]
for dataset in datasets:
	path = "data_sets/scp"+str(dataset)+".txt"
	total_weights = data_set.run_experiment(path, False)
	results = np.vstack((results, total_weights)) if len(results) else total_weights 
print results


