#coding=utf-8

import numpy as np

def LongestCommonPrefix(L):
    M = np.array(map(None,*L))
    for i in range(M.shape[0]):
        if np.all(M[i,:]==M[i,0]):
            continue
        else:
            return i
        
# L = ['bad','badsdxx','baxadf','bads']
# map(None,*L)