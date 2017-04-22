
import data_set
import copy
import setcover
import math

def div(a,b):
    return setcover.div(a,b)

def f_cost1(v_elements, weight_set, h_element_in_the_set, verbose):
    value_set = 0
    for element in h_element_in_the_set:
        value_set += v_elements[element]
    ratio = div(weight_set, value_set) 
    return ratio

# def f_cost2(v_elements, weight_set, h_element_in_the_set, verbose):
#     value_set = 0
#     for element in h_element_in_the_set:
#         value_set += v_elements[element]
#     ratio = div(weight_set, value_set*len(h_element_in_the_set)) 
#     return ratio

# def f_cost3(v_elements, weight_set, h_element_in_the_set, verbose):
#     return []

def heuristic_valuation_skeleton(h_elements, v_elements, l_sets, f_ratio, verbose):
    total_weight = 0
    k=0
    while h_elements:
        k += 1
        if verbose:
            print "turn", k
        best_ratio = float("Inf")
        best_index = 0

        # Compute value (average cost) of every element 
        for i_set, sett in enumerate(l_sets):
            weight_set, h_element_in_the_set = sett
            for element in h_element_in_the_set:
                v_elements[element] += div(weight_set, len(h_element_in_the_set))

        for element in h_elements:
            v_elements[element] = div(v_elements[element], h_elements[element])

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
    setcover.preprocess_frequency(h_elements, l_sets, verbose)
    return heuristic_valuation_skeleton(h_elements, v_elements, l_sets, f_ratio, verbose)

def heuristic_valuation1(h_elements, l_sets, verbose):
    return heuristic_valuation_general(h_elements, l_sets, f_cost1, verbose)

# def heuristic_valuation2(h_elements, l_sets, verbose):
#     return heuristic_valuation_general(h_elements, l_sets, f_cost2, verbose)

# def heuristic_valuation3(h_elements, l_sets, verbose):
#     return heuristic_valuation_general(h_elements, l_sets, f_cost3, verbose)
