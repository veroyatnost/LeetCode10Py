#coding=utf-8

import numpy, itertools

checker = lambda arr: np.all(np.array([abs(arr[i]-arr[j])!=j-i \
        for i,j in itertools.combinations(range(len(arr)),2)]))

def NQueenSolution(N):
    d = {}
    for arr in itertools.permutations(range(N),N):
        if checker(arr):
            NQueenSolution[''.join([str(item) for item in arr])] = 1
    return d