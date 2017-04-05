# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:23:15 2017

@author: jessicahoffmann
"""

#%%
import setcover
import unittest
import random

#%%
#
#class RandomTest(unittest.TestCase):
#
#    """Test case utilisé pour tester les fonctions du module 'random'."""
#
#    def setUp(self):
#        """Initialisation des tests."""
#        self.liste = list(range(10))
#
#    def test_choice(self):
#        """Test le fonctionnement de la fonction 'random.choice'."""
#        elt = random.choice(self.liste)
#        self.assertIn(elt, self.liste)
#
#    def test_shuffle(self):
#        """Test le fonctionnement de la fonction 'random.shuffle'."""
#        random.shuffle(self.liste)
#        self.liste.sort()
#        self.assertEqual(self.liste, list(range(10)))
#
#    def test_sample(self):
#        """Test le fonctionnement de la fonction 'random.sample'."""
#        extrait = random.sample(self.liste, 5)
#        for element in extrait:
#            self.assertIn(element, self.liste)
#
#        with self.assertRaises(ValueError):
#            random.sample(self.liste, 20)
            
#%%

class Greedy_T(unittest.TestCase):
    
    
    def test_greedy1(self):
        element1 = {'a': 0, 'b': 0, 'c': 0}
        sets1 = [(2, {'a':0}), \
        (10, {'b':0, 'c':0}), \
        (3, {'a':0, 'c':0}), \
        (8, {'b':0}), \
        (8, {'b':0, 'c':0})]
        
        self.assertEqual (11, setcover.greedy(element1, sets1))
        

    
    
    
unittest.main()