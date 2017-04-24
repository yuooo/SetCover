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

def print_matrix(mat, legend):
    df = pd.DataFrame(mat)
    plot_matrix = df.plot(colormap = 'rainbow')
    plot_matrix.legend(legend, loc='center left', bbox_to_anchor=(1, 0.5))

#%% General functions
def setcover_value1(path, verbose):

    total_weights = []
    
#    element1, sets1 = create_data_set(path)
#    total_weights.append(brute_force_not_smart(element1, sets1, verbose))

    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency1(element1, sets1, verbose))
	
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency2(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency3(element1, sets1, verbose))

    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency4(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency5(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency6(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency7(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency8(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency9(element1, sets1, verbose))

    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_valuation1(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_valuation2(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_valuation_mixed(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    greedy_value = setcover.usual_greedy(element1, sets1, verbose)
    total_weights.append(greedy_value)
    
    total_weights.append(greedy_value)
    total_weights[-2] = min(total_weights)
    
    names = ['heuristic_frequency_1', 'heuristic_mix_frequency', 'heuristic_frequency_3', \
    'heuristic_frequency_4','heuristic_frequency_5','heuristic_frequency_6', \
    'heuristic_frequency_7','heuristic_frequency_8','heuristic_frequency_9', \
    'heuristic_valuation_1', 'heuristic_valuation_2', 'heuristic_mix_valuation', \
    'best', 'greedy']
    
    return total_weights, names
    
    
def setcover_value2(path, verbose):

    total_weights = []
    
#    element1, sets1 = create_data_set(path)
#    total_weights.append(brute_force_not_smart(element1, sets1, verbose))

    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency1(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency5(element1, sets1, verbose))
	
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency6(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency7(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency8(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_frequency9(element1, sets1, verbose))
    
    element1, sets1 = create_data_set(path)
    greedy_value = setcover.usual_greedy(element1, sets1, verbose)
    total_weights.append(greedy_value)
#    
#    total_weights.append(greedy_value)
#    total_weights[-2] = min(total_weights)
    
    names = ['heuristic_frequency_1', \
    'heuristic_frequency_5','heuristic_frequency_6', \
    'heuristic_frequency_7','heuristic_frequency_8', \
    'heuristic_frequency_9', 'best', 'greedy']
    
    return total_weights, names

def run_benchmark():
    setcover_value_matrix = np.array([])
    datasets = range(41,50) + range(51,60) + range(61,66) + [410]
    for dataset in datasets:
        path = "data_sets/scp"+str(dataset)+".txt"
        total_weights, legend = setcover_value1(path, False)
        setcover_value_matrix = np.vstack((setcover_value_matrix, total_weights)) if len(setcover_value_matrix) else total_weights 
        with open("Output.txt", "w") as text_file:
            text_file.write(str(setcover_value_matrix))
        
    print_matrix(setcover_value_matrix, legend)
         
    return setcover_value_matrix, legend



b, legend = run_benchmark()

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

def compare_greedy_scoring(setcover_value_matrix):
    """ 
    scoring : sum_instance (algo(instance) - greedy(instance)) / greedy(instance) 
    """
    nrows, ncols = setcover_value_matrix.shape
    scores = np.zeros((1, ncols))
    for irow in range(nrows):
        greedy_value = setcover_value_matrix[irow][-1]
        for icol in range(ncols):
            scores[0][icol] += float(setcover_value_matrix[irow][icol])/greedy_value - 1
    return scores/nrows * 100
    
def compare_greedy_matrix(setcover_value_matrix):
    nrows, ncols = setcover_value_matrix.shape
    scores = np.zeros((nrows, ncols))
    for irow in range(nrows):
        greedy_value = setcover_value_matrix[irow][-1]
        for icol in range(ncols):
            scores[irow][icol] = float(setcover_value_matrix[irow][icol])/greedy_value - 1
            
    return scores
    

    

    
#%%
    
c = compare_greedy_matrix(b)
print_matrix(c, legend)

#%%
print compare_greedy_scoring(b)



