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

inf = float('Inf')


def bruteForce():
    return []

def greedy(h_elements, l_sets):
    total_weight = 0
    while h_elements:
        best_ratio = inf
        best_index = 0
        for i_set, sett in enumerate(l_sets):
            weight_set, h_element_in_the_set = sett
            new_ratio = float(weight_set) / len(h_element_in_the_set)
            if new_ratio < best_ratio:
                best_ratio = new_ratio
                best_index = i_set
        best_weight, best_set = l_sets[best_index]
        del l_sets[best_index]
        total_weight += best_weight
        for element_now_covered in best_set:
            del h_elements[element_now_covered]
 


       
                