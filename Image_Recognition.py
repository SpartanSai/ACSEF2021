# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:49:11 2021

@author: varun
"""

import numpy as np
import math
from PIL import Image

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


    def __init__(self, L, sizes):
        self.L = L
        self.sizes = sizes
        self.network = []*L
        self.error = []*L
        self.delta = []*L
        for i in range(0, L-1):
            self.weights[i] = [[]*sizes[i+1]]*sizes[i]
            self.biases[i] = []*sizes[i+1]
            self.network[i] = []*sizes[i]
        self.network[L-1] = []*sizes[L-1]

    def forward(self, inp):
        self.network[0] = inp
        for l in range(1, self.L):
            for i in range(0, self.sizes[l]):
                self.network[l][i] = self.biases[l-1][i];
                for j in range(0, self.sizes[l-1]):
                    self.network[l][i] += self.weights[l-1][j][i] * self.network[l-1][j]
                    for i in range(0, self.sizes[l]):
                        self.network[l][i] = (1/(1 + np.exp(-self.network[l][i])))
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
    
    def train_network(self, train, learning_rate, epochs, expected):
        for epoch in range(0, epochs):
            cost_sum = 0
            for inp in train:
                out = self.forward(inp)
                expected_out = [0 for i in range(expected)]
                expected_out[inp[-1]] = 1
                cost_sum += sum([(expected_out[i]-out[i])**2 for i in range(len(expected))])
                self.backward(expected_out)
                self.update_weights(learning_rate)

data = []*148

for i in range(1, 183):
    image = Image.open("C:/Users/varun/Python/ACSEF_2021/CroppedImages/dutmc_09_1_cropped.png")
    pixel_values = list(image.getdata())
    real_pixel_values = []*(870*484)

    for value in pixel_values:
        real_pixel_values.append(value[0])

    data.append(real_pixel_values)
    
L = 4
sizes = [870 * 484, 10, 20, 10]
nn = NeuralNetwork(L, sizes)

learning_rate = 0.25
epochs = 1
expected = 
nn.train_network(data, learning_rate, epochs, expected)
