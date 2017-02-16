#coding=utf-8

import itertools, collections

def FourSum(s,t):
    F_Collision = lambda x,y: False if (x[0] in y or x[1] in y) else True # Check tuple x and tuple y has collision
    sortedIdx, sortedVal = zip(*sorted(enumerate(s),key=lambda x:x[1])) # Sort: O(NlogN)

    PairOrderedDict  = collections.OrderedDict(\
                            { k: [v for v in list(itertools.combinations(sortedIdx,2)) if v[0]+v[1]==k ] \
                            for k in set([a + b for a,b in itertools.combinations(sortedVal,2)])})

    # Sort O(N^2) items and store in OrderedDict: O(N^2logN)
    start, end, ks = 0, len(PairOrderedDict)-1 , PairOrderedDict.keys()
    while start < end:
        if ks[start]+ks[end] == t:
            print [ (p1,p2) for p1,p2 in itertools.product(\
                    PairOrderedDict.values()[start],PairOrderedDict.values()[end]) if F_Collision(p1,p2)]
        # Short-cut Evaluation: O(N^2LogN)
        start,end = (start+1,end) if ks[start]+ks[end] <= t else (start,end-1)
