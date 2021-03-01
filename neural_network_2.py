# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:00:38 2021

@author: varun
"""

import numpy as np

def squish(arr):
    # sigmoid function
    for i in range(0, len(arr)):
        arr[i] = (1/(1 + np.exp(-arr[i])))
    return arr;

# inp = []*n (layer x)
# out = []*m (layer x+1)
# weights = [[]*n]*m (weights[i][j] = weight between inp[i] and out[j])
# biases = []*m (biases[i] = bias for out[i])

def forward(n, m, inp, weights, biases):
    out = [0]*m
    for i in range(0, m):
        out[i] = biases[i];
        for j in range(0, n):
            out[i] += weights[i][j] * inp[j]
    return squish(out);

# out[i] = squish(sum(weights[i][j]*inp[j]) + biases[i])

n = 4
m = 3
w = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1]]
b = [0, 0, 3]
inp = [1, 1, 1, 1]
print(forward(n, m, inp, w, b))
            
    