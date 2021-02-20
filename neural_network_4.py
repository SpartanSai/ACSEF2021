#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:29:33 2021

@author: saimonish
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:47:40 2021

@author: varun
"""

import numpy as np
import math

class NeuralNetwork:


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
        #for i in range(0, len(output)):
        #    output[i] = (1/(1 + np.exp(-output[i]))) OR sigmoid(output[i])
        return output
        
    
    def run(self):
        self.hide = self.forward(self.n_1, self.n_2, self.inp, self.w_1, self.b_1)
        print(self.hide)
        self.out = self.forward(self.n_2, self.n_3, self.hide, self.w_2, self.b_2)
        print(self.out)
        
        
    def cost(self, arr):
        costsum =0
        for i in range(0, n_3):
            costsum += (arr[i]-self.out[i])**2
        return costsum
    
    
    def backpropogation(self):
        
        
        
        
        
        ## application of the chain rule to find derivative(slope) of the loss function with respect to weight2(w_2_ and weight1(w_1)
        #d_w_2 = np.dot(self.layer1.T, (2*(self.y - self.output) * (1 / (1 + math.exp(-self.output))*(1-(1 / (1 + math.exp(-self.output)))))))
        #d_w_1 = np.dot(self.inp.T,  (np.dot(2*(self.y - self.output) * (1 / (1 + math.exp(-self.output))*(1-(1 / (1 + math.exp(-self.output))))), self.w_2.T) * (1 / (1 + math.exp(-self.layer1))*(1-(1 / (1 + math.exp(-self.layer1)))))))
        #self.w_1 += d_w_1
        #self.w_2 += d_w_2
        
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

        
        
        
        