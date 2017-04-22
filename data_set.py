import numpy as np
import setcover
import heuristic_valuation
import matplotlib.pyplot as plt
"""
@author: ea26425
"""

"""
This function reads a data set from a txt file and returns
- a dictionary of the elements, "list_of_elements" and
- a list of tuples, "list_of_sets", where every tuple contains the cost and the dictionary of a set

The format of the txt data files is:
number of elements, number of sets
the cost of each set c(j),j=1,...,n
for each element i (i=1,...,m): the number of sets which cover
element i followed by a list of the sets which cover element i

The data sets can be found here: http://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html
"""


def create_data_set(path_dir):

    f = open(path_dir, "r")
    num_of_el, num_of_sets = map(int, f.readline().split())
    #print 'elements: ', num_of_el, ' sets: ', num_of_sets

    # read weights
    weights = []
    while(len(weights) < num_of_sets):
        for w in map(int, f.readline().split()):
            weights.append(w)

    list_of_elements = {}
    for el in xrange(num_of_el):
        list_of_elements.update({str(el):0})

    list_of_sets = []
    for s in xrange(num_of_sets):
        list_of_sets.append((weights[s], {}))


    frequency = np.zeros((num_of_el,))

    for element in xrange(num_of_el):
        frequency[element] = map(int, f.readline().split())[0]

        # list of sets that include the element
        sets_of_element = []
        while(len(sets_of_element)<frequency[element]):
            for s in map(int, f.readline().split()):
                sets_of_element.append(s-1)

        # update every set with the current element
        for s in sets_of_element:
            list_of_sets[s][1].update({str(element):0})

    return list_of_elements, list_of_sets

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

    element1, sets1 = create_data_set(path)
    total_weights.append(setcover.heuristic_valuation1(element1, sets1, verbose))

    return total_weights

