# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:00:38 2021

@author: varun
"""

def squish(arr):
    # tanh function, sigmoid function
    return arr;

# inp = []*n (layer x)
# out = []*m (layer x+1)
# weights = [[]*n]*m (weights[i][j] = weight between inp[i] and out[j])
# biases = []*m (biases[i] = bias for out[i])

def forward(n, m, inp, weights, biases):
    out = []*m
    for i in range(0, m):
        out[i] = biases[i];
        for j in range(0, n):
            out[i] += weights[i][j] * inp[j]
    return squish(out);

# out[i] = squish(sum(weights[i][j]*inp[j]) + biases[i])
            
    