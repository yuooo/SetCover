# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:05:27 2017

@author: jessicahoffmann
"""

import setcover
import data_set
import numpy as np

# DATA SETS: http://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html


#%% General functions
def run_experiment(path, verbose):

	total_weights = []

	element1, sets1 = create_data_set(path)
	total_weights.append(setcover.usual_greedy(element1, sets1, verbose))

	element1, sets1 = create_data_set(path)
	total_weights.append(setcover.heuristic_frequency1(element1, sets1, verbose))
	
	element1, sets1 = create_data_set(path)
	total_weights.append(setcover.heuristic_frequency2(element1, sets1, verbose))
	
	element1, sets1 = create_data_set(path)
	total_weights.append(setcover.heuristic_frequency3(element1, sets1, verbose))
	
	element1, sets1 = create_data_set(path)
	total_weights.append(setcover.heuristic_frequency4(element1, sets1, verbose))

	return total_weights



results = np.array([])
datasets = range(41,50) + range(51,60) + range(61,66) + [410]
for dataset in datasets:
	path = "data_sets/scp"+str(dataset)+".txt"
	total_weights = data_set.run_experiment(path, False)
	results = np.vstack((results, total_weights)) if len(results) else total_weights 
print results



