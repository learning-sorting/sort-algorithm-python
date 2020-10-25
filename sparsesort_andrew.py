#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 02:17:43 2020

@author: andrew
"""

'''
Like "Finding needles in a haystack"
This script creates x random values in large matrices 
filled with zeroes and then
sorts them with their coordinate location in the matrix '''

import sparse 
import random
import numpy as np
import collections


def sparsesort(numbers,coords):
    X,Y=coords
    
    matrix=np.zeros((X,Y))
    
    for i in range(numbers):
        rx,ry = random.randint(0,X-1), random.randint(0,Y-1)
        matrix[rx,ry] = random.random()
    
    print()
    print(r'Sorting {} random numbers in a sparse ("zero-filled") {} x {} matrix:'.\
          format(numbers,X,Y))
    print(matrix)
    print()
    
    sparse_matrix = sparse.COO(matrix)
    where = sparse.where(sparse_matrix)
    smd = sparse_matrix.data 
    
    matrix_dict = dict(zip(smd, zip(*where)))
    
    matrix_sorted = collections.OrderedDict(sorted(matrix_dict.items()))
    
    mitems = matrix_sorted.items()
    
    print('sorting results:')
    
    k=1
    for i, j in mitems:
        print('item #{}: {} @ coordinate {}'.format(k,i, j))
        k+=1
    print()
    
print('\nTINY MATRIX')
sparsesort(10,(5,5))

print('\nHUGE MATRIX')
sparsesort(100,(6000,6000))