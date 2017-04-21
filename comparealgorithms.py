# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:05:27 2017

@author: jessicahoffmann
"""

import setcover
import data_set
import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
from preprocessing import *
import matplotlib.cm as cm
import pandas as pd
=======

>>>>>>> 87eb61b9997392769918bbb89f863b692dfe6864
# DATA SETS: http://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html


#%% General functions
def setcover_value(path, verbose):

    total_weights = []

    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency1(element1, sets1, verbose))
	
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency2(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency3(element1, sets1, verbose))

    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency4(element1, sets1, verbose))

    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.usual_greedy(element1, sets1, verbose))

    return total_weights

def run_benchmark():
    results = np.array([])
    datasets = range(41,50) + range(51,60) + range(61,66) + [410]
    for dataset in datasets:
        path = "data_sets/scp"+str(dataset)+".txt"
        total_weights = setcover_value(path, False)
        results = np.vstack((results, total_weights)) if len(results) else total_weights 
        with open("Output.txt", "w") as text_file:
            text_file.write(str(results))
        
    df = pd.DataFrame(results)
    df.plot(colormap = 'rainbow')
         
    return results



b = run_benchmark()






