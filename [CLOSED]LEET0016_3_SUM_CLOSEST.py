#coding=utf-8
import numpy,itertools

def ThreeSumClosest(L, tar):
    LL = list(L)
    ArrayList, ResultSet, cur_max , cur_sum = \
        numpy.array(LL), {k:[idx for idx,val in enumerate(LL) if val==k] for k in LL}, None, None
        
    Dict_Sum = {(i,j):(LL[i]+LL[j]) for i,j in itertools.combinations(range(len(LL)),2)}
    
    for (i,j),v1 in Dict_Sum.iteritems():
        for v2 in ResultSet:
            if (cur_max==None or np.fabs(v1+v2-tar)<cur_max) and len(set(ResultSet[v2])-set([i,j]))>=1:
                cur_max, cur_sum = (np.fabs(v1+v2-tar), v2+v1)
    return cur_sum

# L_example = {-1,2,1,-4}
# t = 1
# ThreeSumClosest(L_example, t)