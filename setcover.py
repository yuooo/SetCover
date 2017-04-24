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

import math
import copy
from preprocessing import *

#class Set:
#    elementList = []
#    weight = 0
#

#%% Utils
inf = float('Inf')

def div(a,b):
    if b == 0:
        return inf
    if b == inf:
        return 0
    else:
        return float(a) / b

#%% Brute force
def get_index_from_binary(bin_number, n_sets):
    index = bin_number[2:].zfill(n_sets)
    return index
    
def is_set_cover(h_elements):
    is_set_cover = True
    for key in h_elements:
        if h_elements[key] == 0:
            is_set_cover = False
        else :
            h_elements[key] = 0
    return is_set_cover
    
#%%
    

def brute_force_not_smart(h_elements, l_sets, verbose):
    print "Usual greedy"
    n_sets = len(l_sets)
    min_weight = inf
    
    n = 0
    while(n<2**n_sets):
        index = get_index_from_binary(bin(n), n_sets)
        
        current_weight = 0
        
        
        # pick a set of sets
        for i_set, (w_set, h_set) in enumerate(l_sets):
            if index[i_set] == '1':
                current_weight += w_set
                for elt in h_set:
                    h_elements[elt] += 1
        
        # check if set cover and update weight accordingly
        if is_set_cover(h_elements):
            min_weight = min(min_weight, current_weight)
    print 'total:', min_weight
    
    return min_weight
        
    


#def bruteForce(h_elements, l_sets):
#    n_sets = len(l_sets)
#    i_min = 0
#    i_max = 0
#    i_set = 0
#    set_used = [0]*n_sets
#    min_value = inf
#    current_cover_value = 0
#    while (i_set > n_sets):
#        set_used[i_set] = 1
#        weight_newset, h_elt_newset = l_sets[i_set]
#        
#        #check if new coverage is worth it
#        if current_cover_value + weight_newset < min_value:
#            current_cover_value += weight_newset
#            
#            # update coverage
#            for elt in h_elt_newset:
#                h_elements[elt] += 1
#        else:
#            
#return []
    
#%% Greedy heuristic functions
    
def f_normal_greedy(h_elements, weight_set, h_element_in_the_set, verbose):
    return div(weight_set, len(h_element_in_the_set))
    
def preprocess_frequency(h_elements, l_sets, verbose):
    for _ , h_element_in_the_set in l_sets:
        for element in h_element_in_the_set:
            h_elements[element] += 1
    if verbose:
        print h_elements


def f_heuristic_frequency_general(f, h_elements, weight_set, \
h_element_in_the_set, verbose):
    weight_heuristic = 0
    for element in h_element_in_the_set:
        weight_heuristic += f(h_elements[element])
    if verbose:
        print h_element_in_the_set, div(weight_set, weight_heuristic)
    return div(weight_set, weight_heuristic)
    
def f_heuristic_frequency1(h_elements, weight_set, h_element_in_the_set, \
verbose):
    f = lambda x: div(1, x-1)
    return f_heuristic_frequency_general(f, h_elements, weight_set, \
    h_element_in_the_set, verbose)
    
def f_heuristic_frequency2(h_elements, weight_set, h_element_in_the_set, \
verbose):
    f = lambda x: 1 + div(1,(x-1))
    return f_heuristic_frequency_general(f, h_elements, weight_set, \
    h_element_in_the_set, verbose)
    
def f_heuristic_frequency3(h_elements, weight_set, h_element_in_the_set, \
verbose):
    f = lambda x: inf if x == 0 else math.exp(-x)
    return f_heuristic_frequency_general(f, h_elements, weight_set, \
    h_element_in_the_set, verbose)

def f_heuristic_frequency4(h_elements, weight_set, h_element_in_the_set, \
verbose):
    f = lambda x: div(len(h_element_in_the_set), (x-1))
    return f_heuristic_frequency_general(f, h_elements, weight_set, \
    h_element_in_the_set, verbose)

def f_heuristic_frequency7(h_elements, weight_set, h_element_in_the_set, \
verbose):
    f = lambda x: div(1, (x-1)**2)
    return f_heuristic_frequency_general(f, h_elements, weight_set, \
    h_element_in_the_set, verbose)
    
def f_heuristic_frequency8(h_elements, weight_set, h_element_in_the_set, \
verbose):
    f = lambda x: div(1, (x-1)**3)
    return f_heuristic_frequency_general(f, h_elements, weight_set, \
    h_element_in_the_set, verbose)
    
def f_heuristic_frequency9(h_elements, weight_set, h_element_in_the_set, \
verbose):
    f = lambda x: div(1, math.sqrt(x-1))
    return f_heuristic_frequency_general(f, h_elements, weight_set, \
    h_element_in_the_set, verbose)






    

#%% Greedy code

def greedy_skeleton(h_elements, l_sets, f, verbose):
    total_weight = 0
    k=0
    while h_elements:
        k += 1
        if verbose:
            print "turn", k
        best_ratio = inf
        best_index = 0

        # find argmin
        for i_set, sett in enumerate(l_sets):
            weight_set, h_element_in_the_set = sett
            new_ratio = f(h_elements, weight_set, h_element_in_the_set, verbose)
            if new_ratio < best_ratio:
                best_ratio = new_ratio
                best_index = i_set
        best_weight, best_set = l_sets[best_index]
        if verbose:
            print "best", best_weight, best_set

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
        if verbose:             
            print 
    print "total", total_weight
    print 
    print
    return total_weight
    
    
def usual_greedy(h_elements, l_sets, verbose):
    print "Usual greedy"
    return greedy_skeleton(h_elements, l_sets, f_normal_greedy, verbose)

def heuristic_frequency1(h_elements, l_sets, verbose):
    print "heuristic frequency 1"
    preprocess_frequency(h_elements, l_sets, verbose)
    return greedy_skeleton(h_elements, l_sets, f_heuristic_frequency1, verbose)
    
def heuristic_frequency2(h_elements, l_sets, verbose):
    print "heuristic frequency 2"
    preprocess_frequency(h_elements, l_sets, verbose)
    return greedy_skeleton(h_elements, l_sets, f_heuristic_frequency2, verbose)
    
def heuristic_frequency3(h_elements, l_sets, verbose):
    print "heuristic frequency 3"
    preprocess_frequency(h_elements, l_sets, verbose)
    return greedy_skeleton(h_elements, l_sets, f_heuristic_frequency3, verbose)
    
def heuristic_frequency4(h_elements, l_sets, verbose):
    print "heuristic frequency 4"
    preprocess_frequency(h_elements, l_sets, verbose)
    return greedy_skeleton(h_elements, l_sets, f_heuristic_frequency4, verbose)  
    
def heuristic_frequency5(h_elements, l_sets, verbose):
    print "heuristic frequency 5"
    l_sets1 = remove_useless(l_sets)
    preprocess_frequency(h_elements, l_sets1, verbose)
    return greedy_skeleton(h_elements, l_sets1, f_heuristic_frequency1, verbose)
    
def heuristic_frequency6(h_elements, l_sets, verbose):
    print "heuristic frequency 6"
    l_sets1 = remove_useless(l_sets)
    preprocess_frequency(h_elements, l_sets1, verbose)
    return greedy_skeleton(h_elements, l_sets1, f_heuristic_frequency2, verbose)
    
def heuristic_frequency7(h_elements, l_sets, verbose):
    print "heuristic frequency 7"
    l_sets1 = remove_useless(l_sets)
    preprocess_frequency(h_elements, l_sets1, verbose)
    return greedy_skeleton(h_elements, l_sets1, f_heuristic_frequency7, verbose)
    
def heuristic_frequency8(h_elements, l_sets, verbose):
    print "heuristic frequency 8"
    l_sets1 = remove_useless(l_sets)
    preprocess_frequency(h_elements, l_sets1, verbose)
    return greedy_skeleton(h_elements, l_sets1, f_heuristic_frequency8, verbose)
    
def heuristic_frequency9(h_elements, l_sets, verbose):
    print "heuristic frequency 9"
    l_sets1 = remove_useless(l_sets)
    preprocess_frequency(h_elements, l_sets1, verbose)
    return greedy_skeleton(h_elements, l_sets1, f_heuristic_frequency9, verbose)

def heuristic_valuation1(h_elements, l_sets, verbose):
    print "heuristic valuation 1"
    return heuristic_valuation_general(h_elements, l_sets, f_cost1, verbose)
    
def heuristic_valuation2(h_elements, l_sets, verbose):
    print "heuristic valuation 2"
    l_sets1 = remove_useless(l_sets)
    return heuristic_valuation_general(h_elements, l_sets1, f_cost1, verbose)    
    
def heuristic_valuation_mixed(h_elements, l_sets, verbose):
    print "heuristic valuation mixed"
    return heuristic_valuation_general(h_elements, l_sets, f_cost_mixed, verbose)

    

def f_cost1(v_elements, weight_set, h_element_in_the_set, verbose):
    value_set = 0
    for element in h_element_in_the_set:
        value_set += v_elements[element]
    ratio = div(weight_set, value_set) 
    return ratio
    
def f_cost_mixed(v_elements, weight_set, h_element_in_the_set, verbose):
    value_set = 0
    for element in h_element_in_the_set:
        value_set += 100 + v_elements[element]
    ratio = div(weight_set, value_set) 
    return ratio

def heuristic_valuation_skeleton(h_elements, v_elements, l_sets, f_ratio, verbose):
    total_weight = 0
    k=0
    while h_elements:
        k += 1
        if verbose:
            print "turn", k
        best_ratio = inf
        best_index = 0

        # Compute value (average cost) of every element 
        for i_set, sett in enumerate(l_sets):
            weight_set, h_element_in_the_set = sett
            for element in h_element_in_the_set:
                v_elements[element] += div(weight_set, len(h_element_in_the_set))

        for element in h_elements:
            v_elements[element] = div(v_elements[element], h_elements[element]-1)

        for i_set, sett in enumerate(l_sets):
            weight_set, h_element_in_the_set = sett
            new_ratio = f_ratio(v_elements, weight_set, h_element_in_the_set, verbose)
            if new_ratio < best_ratio:
                best_ratio = new_ratio
                best_index = i_set
        best_weight, best_set = l_sets[best_index]
        if verbose:
            print "best", best_weight, best_set

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
        if verbose:             
            print 
    print "total", total_weight
    print 
    print
    return total_weight

def heuristic_valuation_general(h_elements, l_sets, f_ratio, verbose):
    v_elements = copy.deepcopy(h_elements)
    preprocess_frequency(h_elements, l_sets, verbose)
    return heuristic_valuation_skeleton(h_elements, v_elements, l_sets, f_ratio, verbose)



       
                
                