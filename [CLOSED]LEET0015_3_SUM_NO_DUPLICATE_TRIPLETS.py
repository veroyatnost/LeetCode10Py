#coding=utf-8

import numpy,itertools

def ThreeSumNoDup(L):
    
    ArrayList, FS, ResultSet = \
        numpy.array(L), {k:[idx for idx,val in enumerate(L) if val==-k] for k in frozenset(numpy.array(L)*-1)}, set()
    
    if numpy.sum(ArrayList==0)>3 and (0,0,0) not in ResultSet:
        ResultSet.add((0,0,0))
        yield (0,0,0)
    
    for i,j in itertools.combinations(range(len(L)),2):
        if L[i]+L[j] in FS and \
                (-2*L[i]!=L[j] or len(FS[-L[i]])>1 ) and \
                (-2*L[j]!=L[i] or len(FS[-L[j]])>1 ) and \
                len([(r,s,t) for r,s,t in itertools.permutations([L[i],L[j],-L[i]-L[j]]) if (r,s,t)in ResultSet])==0:
            ResultSet.add((L[i],L[j],-L[i]-L[j]))
            yield (L[i],L[j],-L[i]-L[j])
            
# L_example = [-1, 0, 1, 2, -1, -4]
# [(i,j,k) for i,j,k in  ThreeSumNoDup(L_example)]