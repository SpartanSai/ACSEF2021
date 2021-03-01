#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:29:33 2021

@author: saidivyesh, varun
"""
from PIL import Image
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
    # delta = []*L (basically error but with the derivatives of the errors)


    def __init__(self, L, sizes, inp, w_1, w_2, b_1, b_2):
        self.L = L
        self.sizes = sizes
        self.network = []*L
        self.error = []*L
        self.delta = []*L
        self.weights = [[], []]
        self.biases = [[], []]
        self.network = [[]*sizes[0], []*sizes[1], []*sizes[2]]
        #for i in range(0, L-1):
        #    self.network[i] = []*sizes[i]

        self.weights[0] = w_1
        self.weights[1] = w_2
        self.biases[0] = b_1
        self.biases[1] = b_2
        #self.network[L-1] = []*sizes[L-1]
        self.network[0] = inp

    def forward(self):
        for l in range(1, self.L):
            for i in range(0, self.sizes[l]):
                self.network[l][i] = self.biases[l-1][i];
                for j in range(0, self.sizes[l-1]):
                    self.network[l][i] += self.weights[l-1][j][i] * self.network[l-1][j]
    #                for i in range(0, self.sizes[l]):
    #                    self.network[l][i] = (1/(1 + np.exp(-self.network[l][i])))
        return self.network[self.L - 1]

    def derivative(output):
        return (output) * (1 - output)

    def backward(self, expected_out):
        for l in reversed(range(1, self.L)):
            if (l == self.L - 1):
                for i in range(0, self.sizes[l]):
                    self.error[l][i] = (self.expected_out[i] - self.network[l][i])
            else:
                for i in range(0, self.sizes[l]):
                    for j in range (0, self.sizes[l+1]):
                        self.error[l][i] += self.weights[l][i][j] * self.delta[l+1][j]
                    self.error[l][i] += self.biases[l-1][i]
            for i in range(0, self.sizes[l]):
                self.delta[l][i] = self.error[l][i] * self.derivative(self.network[l][i])

    # 0.25 = learning rate (we will run in batches)
    def update_weights(self, learning_rate):
        for l in range(1, self.L):
            for i in range(0, self.sizes[l]):
                for j in range(self.sizes[l-1]):
                    self.weights[l-1][j][i] += learning_rate * self.network[l-1][j] * self.delta[l][i]
                self.biases[l-1][i] += learning_rate * self.delta[l][i]
    
    # collect all the data, split into train and test
    # 
    def train_network(self, train, learning_rate, epochs, expected):
        for epoch in range(0, epochs):
            cost_sum = 0
            for inp in train:
                out = self.forward()
                expected_out = [0 for i in range(expected)]
                # expected_out[inp[-1]] = 1
                cost_sum += sum([(expected_out[i]-out[i])**2 for i in range(len(expected))])
                self.backward(expected_out)
                self.update_weights(learning_rate)

n_1 = 412368
n_2 = 10000
n_3 = 10

image = Image.open("/Users/saimonish/IntelliJ_workspace/ACSEF2021/CroppedImages/dutmc_09_1_cropped.png")
input_values = list(image.getdata())

w_1 = [[0.5]*10000]*412368
w_2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
b_1 = [0]*10000
b_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#nn = NeuralNetwork(n_1, n_2, n_3, inp, w_1, w_2, b_1, b_2)
nn = NeuralNetwork(3, [n_1, n_2, n_3], input_values, w_1, w_2, b_1, b_2)
nn.train_network([input_values], 0.1, 1, 1)




