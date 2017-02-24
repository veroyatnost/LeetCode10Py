#coding=utf-8

import numpy as np

def RemoveDupInPlace(arr):
    if not type(arr)!=np.array or len(arr.shape)>1:
        return None
    i, j, running = 0,0, arr[0]
    for i in range(1,len(arr)):
        if arr[i]!=running:
            j+=1
            arr[j] , running = arr[i], arr[i]
    return j+1

# arr = np.array([1,1,2,2,3,3,5,5,5,5,7])
# pos = RemoveDupInPlace(arr)
# arr, arr[:pos]