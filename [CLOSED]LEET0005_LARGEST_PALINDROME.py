#coding=utf-8
'''
We haven't a story to tell about why this algorithm is useful.
Wish someone could tell.
'''
import numpy as np

def LargestPalindrome(s):
    ss = '#'+'#'.join(list(s))+'#'
    p,cid,mx = np.zeros(len(ss),dtype=np.int32), 0, 0
    for idx, c in enumerate(ss):
        p[idx] = min(p[ 2*cid - idx],mx-idx) if mx > idx else 1
        while idx >= p[idx] and idx+p[idx]<len(p) and ss[idx + p[idx]] == ss[idx - p[idx]]:
            p[idx] = p[idx]+1
        mx, cid = (idx + p[idx], idx) if idx+p[idx] > mx else (mx,cid)
    return np.max(p)-1