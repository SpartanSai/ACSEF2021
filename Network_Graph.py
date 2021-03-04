# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 05:16:25 2021

@author: varun
"""

import matplotlib.pyplot as plt

file = open("C:/Users/varun/Python/ACSEF_2021/cost_sums.txt", "r")

x = []
y = []

for i in range(0, 125):
    x.append(i)
    y.append(float(file.readline()))
    
plt.plot(x, y)

plt.xlabel('Training Example')
plt.ylabel('Error (loss function)')
plt.title('Error of Neural Network Over Time')

plt.show()