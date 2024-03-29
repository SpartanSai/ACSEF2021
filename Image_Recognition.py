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
        self.network = [0]*L
        self.error = [0]*L
        self.delta = [0]*L
        self.weights = [0]*L
        self.biases = [0]*L
        for i in range(0, L-1):
            self.weights[i] = [[0]*sizes[i+1]]*sizes[i]
            self.biases[i] = [0]*sizes[i+1]
            self.network[i] = [0]*sizes[i]
            self.error[i] = [0]*sizes[i]
            self.delta[i] = [0]*sizes[i]
        self.error[L-1] = [0]*sizes[L-1]
        self.delta[L-1] = [0]*sizes[L-1]
        self.network[L-1] = [0]*sizes[L-1]

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

    def derivative(self, output):
        return (output) * (1 - output)

    def backward(self, expected_out):
        for l in reversed(range(1, self.L)):
            if (l == self.L - 1):
                for i in range(0, self.sizes[l]):
                    self.error[l][i] += (expected_out[i] - self.network[l][i])
            else:
                for i in range(0, self.sizes[l]):
                    for j in range (0, self.sizes[l+1]):
                        self.error[l][i] += self.weights[l][i][j] * self.delta[l+1][j]
                    self.error[l][i] += self.biases[l-1][i]
            for i in range(0, self.sizes[l]):
                print(self.error[l][i])
                print(self.derivative(self.network[l][i]))
                print(self.delta[l][i])
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
            for j in range(0, len(train)):
                inp = train[j]
                out = self.forward(inp)
                expected_out = expected[j]
                cost_sum = sum([(expected_out[i]-out[i])**2 for i in range(0, len(expected_out))])
                self.backward(expected_out)
                self.update_weights(learning_rate)
                print(cost_sum)

data = []
for i in range(0, 400):
    image = Image.open("C:/Users/varun/Python/ACSEF_2021/CroppedImages/dutmc_09_1_cropped.png")
    #image = Image.open("/Users/saimonish/IntelliJ_workspace/ACSEF2021/CroppedImages/dutmc_09_1_cropped.png")
    pixel_values = list(image.getdata())
    real_pixel_values = []*(412368)
    for value in pixel_values:
        real_pixel_values.append(value[0])
    data.append(real_pixel_values)
    
L = 4
sizes = [412368, 10, 20, 10]
nn = NeuralNetwork(L, sizes)

learning_rate = 0.1
epochs = 1
file = open("C:/Users/varun/Python/ACSEF_2021/cars_in_pictures.txt", "r")
#file = open("/Users/saimonish/IntelliJ_workspace/ACSEF2021/cars_in_pictures.txt", "r")
expected = [[0]*10]*400
for i in range(0, 400):
    x =  int(file.readline())
    expected[i][x-1] = 1
nn.train_network(data, learning_rate, epochs, expected)
