# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:30:03 2021

@author: varun
"""

class NeuralNetwork:
    inp = []
    out = [0, 0, 0]
    weights = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [0, 0, 0], [0, 0, 0]]
    biases = [[1, 1, 1], [1, 1, 1], [2, 3, 4], [0, 0, 0], [0, 0, 0]]
    def __init__(self, i, x):
        self.inp = i
        
    #def update_weights(self):
        # random calculus stuff
    
    #def update_biases(self):
        # random calculus stuff
    
    def run(self):
        for i in range(0, len(self.inp)):
            for j in range(0, len(self.out)):
                self.out[j] += self.weights[i][j]*self.inp[i] + self.biases[i][j]
        return self.out
        
n = NeuralNetwork([3, 3, 4, 5, 1], 3)
print(n.run())