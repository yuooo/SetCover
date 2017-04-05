# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 13:50:59 2017

@author: jhh2677
"""

"""
All algo take in input: 
- hashtable of elements to cover
- a list of tuples, i.e. the list of (weight, hash of the elements the set contains)
they return:
[total weight, indexes of the optimal set] """

#class Set:
#    elementList = []
#    weight = 0
#

#%% Utils
inf = float('Inf')

def div(a,b):
    if b == 0:
        return inf
    else:
        return float(a) / b

#%% Set cover algo

def bruteForce(h_elements, l_sets):
    return []
    
def f_normal_greedy(weight_set, h_element_in_the_set):
    return div(weight_set, len(h_element_in_the_set))

def greedy_skeleton(h_elements, l_sets, f):
    total_weight = 0
    while h_elements:
        best_ratio = inf
        best_index = 0

        # find argmin
        for i_set, sett in enumerate(l_sets):
            weight_set, h_element_in_the_set = sett
            new_ratio = f(weight_set, h_element_in_the_set)
            if new_ratio < best_ratio:
                best_ratio = new_ratio
                best_index = i_set
        best_weight, best_set = l_sets[best_index]
#        print best_weight, best_set

        # Remove best set from the list of possible sets
        del l_sets[best_index]
        total_weight += best_weight

        # Remove newly covered elements to the list of elements to cover
        for element_now_covered in best_set:
            del h_elements[element_now_covered]

        # Remove newly covered elements from the sets left
        for sett in l_sets:
            _ , h_set = sett 
            for element_now_covered in best_set:
                if element_now_covered in h_set:
                    del h_set[element_now_covered]
                
    return total_weight
    
    
def usual_greedy(h_elements, l_sets):
    return greedy_skeleton(h_elements, l_sets, f_normal_greedy)
#%%
 
element1 = {'a': 0, 'b': 0, 'c': 0}
sets1 = [(2, {'a':0}), \
(10, {'b':0, 'c':0}), \
(3, {'a':0, 'c':0}), \
(8, {'b':0}), \
(8, {'b':0, 'c':0})]
usual_greedy(element1, sets1)
       
                
                