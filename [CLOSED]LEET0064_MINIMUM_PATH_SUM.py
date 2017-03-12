#coding=utf-8

def FindPath(M):
    m,n = M.shape
    MValue, MPath , Path = np.zeros((m,n)),np.zeros((m,n)), []
    for i in range(m):
        for j in range(n):
            #MValue[i,j] = max( (0 if i==0 else MValue[i-1,j]), (0 if j==0 else MValue[i,j-1]) ) + M[i,j]
            #MPath[i,j] = 0 if i==0 else 1 if j==0 else 0 if MValue[i-1,j]<MValue[i,j-1] else 1 # 0 Means From Left
            MValue[i,j],MPath[i,j] = max( (0 if i==0 else MValue[i-1,j]), (0 if j==0 else MValue[i,j-1]) ) + M[i,j],\
                        0 if i==0 else 1 if j==0 else 0 if MValue[i-1,j]<MValue[i,j-1] else 1 # 0 Means From Left
    while m>0 and n>0:
        Path.append((m-1,n-1))
        m,n = (m-1,n) if MPath[m-1,n-1]==1 else (m,n-1)
    return MValue, MPath, Path[::-1]
