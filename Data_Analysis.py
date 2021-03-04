# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:59:08 2021

@author: varun, sai divyesh
"""

#       |   *   |
#       |   *   |
#       |0 1*   |
#       |   *   |
#_______|F L*   |_______
#                F 2
#                L 3
#* * * *         * * * * 
#    7 L
#    6 F
#_______         _______
#       |   *L F|
#       |   *   |
#       |   *5 4|
#       |   *   |
#       |   *   |

file = open("C:/Users/varun/Python/ACSEF_2021/cars_in_pictures.txt", "r")
#file = open("/Users/saimonish/IntelliJ_workspace/ACSEF2021/cars_in_pictures.txt", "r")
f = open("C:/Users/varun/Python/ACSEF_2021/waiting_times.txt", "w")
#f = open("/Users/saimonish/IntelliJ_workspace/ACSEF2021/waiting_times.txt", "w")
sums = [-1]*8
print('       |   *   |\n       |   *   |\n       |0 1*   |\n       |   *   |\n_______|F L*   |_______\n                F 2\n                L 3\n* * * *         * * * * \n    7 L\n    6 F\n_______         _______\n       |   *L F|\n       |   *   |\n       |   *5 4|\n       |   *   |\n       |   *   |')
for i in range(0, 400, 8):
    A = []
    for j in range(0, 8):
        A.append(int(file.readline()))    
    sums[0] = A[0] + A[1]
    sums[1] = A[2] + A[3]
    sums[2] = A[4] + A[5]
    sums[3] = A[6] + A[7]
    sums[4] = A[0] + A[4]
    sums[5] = A[1] + A[5]
    sums[6] = A[2] + A[6]
    sums[7] = A[3] + A[7]
    
    for j in range(0, 8):
        m = -1
        ind = -1
        for k in range(0, 8):
            if m < sums[k]:
                ind = k
                m = sums[k]
        if ind == 0:
            print('The lights are green for the cars in lanes 0 and 1 (using the diagram above)')
        elif ind == 1:
            print('The lights are green for the cars in lanes 2 and 3 (using the diagram above)')
        elif ind == 2:
            print('The lights are green for the cars in lanes 4 and 5 (using the diagram above)')
        elif ind == 3:
            print('The lights are green for the cars in lanes 6 and 7 (using the diagram above)')
        elif ind == 4:
            print('The lights are green for the cars in lanes 0 and 4 (using the diagram above)')
        elif ind == 5:
            print('The lights are green for the cars in lanes 1 and 5 (using the diagram above)')
        elif ind == 6:
            print('The lights are green for the cars in lanes 2 and 6 (using the diagram above)')
        elif ind == 7:
            print('The lights are green for the cars in lanes 3 and 7 (using the diagram above)')
        
        for k in range(0, sums[ind]):
            f.write(str(j) + '/n')
        sums[ind] = -1
    f.write('==== /n')
