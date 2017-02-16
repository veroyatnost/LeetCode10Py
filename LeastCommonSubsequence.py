#coding=utf-8

def LCS(p,l):
    if len(p)==0 or len(l)==0:
        return 0
    # P = np.array(list(p)).reshape((1,len(p)))
    # L = np.array(list(l)).reshape((len(l),1))
    # M = np.int32(P==L)
    M = np.int32( np.array(list(p)).reshape((1,len(p)))==np.array(list(l)).reshape((len(l),1)) )
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            up = 0 if i==0 else M[i-1,j]
            left = 0 if j==0 else M[i,j-1]
            M[i,j] = max(up,left, M[i,j] if (i==0 or j==0) else M[i,j]+M[i-1,j-1])
    return M.max()
