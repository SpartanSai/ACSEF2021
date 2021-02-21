#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:29:33 2021

@author: saidivyesh, varun
"""

import numpy as np
import math

class NeuralNetwork:
    # L = # of layers
    # sizes = []*L (number of neurons in each layer)
    # network = []*L (network[i] is an array with all of the neuron 
    #                 values)
    # weights = []*(L-1) (weights[i] is a matrix with all of the
    #                     weights between each pair of neurons
    #                     in each layer)
    # biases = []*(L-1) (biases[i] is an array with all of the 
    #                    biases of the (i+1)th layer)
    # error = []*L (basically network but with all of the errors)
    # expected_out = [] (array with the expected output of the last layer)
    # delta = []*L (basically error but with the derivatives of the errors)
    

    def __init__(self, L, sizes, expected_out, inp):
        self.L = L
        self.sizes = sizes
        self.expected_out = expected_out
        self.network = []*L
        self.error = []*L
        self.delta = []*L
        for i in range(0, L-1):
            self.weights[i] = [[]*sizes[i+1]]*sizes[i]
            self.biases[i] = []*sizes[i+1]
            self.network[i] = []*sizes[i]
        self.network[L-1] = []*sizes[L-1]
        self.network[0] = inp
        
    def forward(self):
        for l in range(1, self.L):
            for i in range(0, self.sizes[l]):
                self.network[l][i] = self.biases[l-1][i];
                for j in range(0, self.sizes[l-1]):
                    self.network[l][i] += self.weights[l-1][j][i] * self.network[l-1][j]
#                for i in range(0, self.sizes[l]):
#                    self.network[l][i] = (1/(1 + np.exp(-self.network[l][i])))

    def derivative(output):
        return (output) * (1 - output)
    
    def backward(self):
        for l in reversed(range(0, self.L)):
            if (l == self.L - 1):
                for i in range(0, self.sizes[l]):
                    self.error[l][i] = (self.expected_out[i] - self.network[l][i])
            else:
                for i in range(0, self.sizes[l]):
                    for j in range (0, self.sizes[l+1]):
                        self.error[l][i] += self.weights[l][i][j] * self.delta[l+1][j]
            for i in range(0, self.sizes[l]):
                self.delta[l][i] = self.error[l][i] * self.derivative(self.network[l][i])
   
        
n_1 = 4
n_2 = 3
n_3 = 4

inp = [1, 1, 1, 1]

w_1 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
w_2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
b_1 = [0, 0, 0]
b_2 = [0, 0, 0, 0]

nn = NeuralNetwork(n_1, n_2, n_3, inp, w_1, w_2, b_1, b_2)       
nn.run()

        
        
        
        