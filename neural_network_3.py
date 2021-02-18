# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:47:40 2021

@author: varun
"""

import numpy as np

class NeuralNetwork:
    # inp = []*n_1
    # hide = []
    # out = []
    # w_1 = [][]
    # w_2 = [][]
    # b_1 = []
    # b_2 = []
    
    
    def __init__(self, a, b, c, arr, weight1, weight2, bias1, bias2):
        self.n_1 = a
        self.n_2 = b
        self.n_3 = c
        
        self.inp = arr
        self.hide = []*b
        self.out = []*c
        
        self.w_1 = weight1
        self.w_2 = weight2
        
        self.b_1 = bias1
        self.b_2 = bias2
        
    def forward(self, n, m, arr, weights, biases):
        output = [0]*m
        for i in range(0, m):
            output[i] = biases[i];
            for j in range(0, n):
                output[i] += weights[i][j] * arr[j]
        for i in range(0, len(output)):
            output[i] = (1/(1 + np.exp(-output[i])))
        return output
        
    
    def run(self):
        self.hide = self.forward(self.n_1, self.n_2, self.inp, self.w_1, self.b_1)
        print(self.hide)
        self.out = self.forward(self.n_2, self.n_3, self.hide, self.w_2, self.b_2)
        print(self.out)
        
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

        
        
        
        