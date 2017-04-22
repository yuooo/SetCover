# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:05:27 2017

@author: jessicahoffmann
"""

import setcover
import data_set
import numpy as np
import matplotlib.pyplot as plt
from preprocessing import *
import matplotlib.cm as cm
import pandas as pd

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
    setcover_value_matrix = np.array([])
    datasets = range(41,50) + range(51,60) + range(61,66) + [410]
    for dataset in datasets:
        path = "data_sets/scp"+str(dataset)+".txt"
        total_weights = setcover_value(path, False)
        setcover_value_matrix = np.vstack((setcover_value_matrix, total_weights)) if len(setcover_value_matrix) else total_weights 
        with open("Output.txt", "w") as text_file:
            text_file.write(str(setcover_value_matrix))
        
    df = pd.DataFrame(setcover_value_matrix)
    df.plot(colormap = 'rainbow')
         
    return setcover_value_matrix



b = run_benchmark()

#%%

def which_is_best(setcover_value_matrix):
    order = np.zeros(setcover_value_matrix.shape)
    nrows, ncol = order.shape
    for row in range(nrows):
        arg = np.argsort(setcover_value_matrix[row])
        raange = range(ncol)
        for icol in raange:
            order[row][arg[icol]] = raange[icol]
    return order

#TODO -> move to test
#a = np.array([[1, 2, 4],[2, 4, 1], [9, 2, 1], [1,5,2], [3,1,2]])
#
#print which_is_best(a)
#print a



def compare_algo(setcover_value_matrix):
    ranks = which_is_best(setcover_value_matrix)*10
    nrows, ncols = ranks.shape
    plt.figure()
    bins = np.linspace(-5, 45, 6)
    
    for icol in range(ncols):
        plt.hist(ranks[:,icol] , width = float(5) / ncols , bins = (float(5) / ncols + 0.1)*icol + bins)
        
        
compare_algo(b)




