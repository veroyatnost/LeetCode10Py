#coding=utf-8

def LargestPalindrome(n):
    bestlatter = (1,9,9) if n==1 else (0,0,0)
    for i in range(int('9'*n),0,-1):
        for j in range(int(int('9'*n)/11)*11,i,-11):
            k =  i*j
            if str(i*j)[::-1] == str(i*j) and bestlatter[2]<i*j:
                bestlatter = (i,j,k)
                break
        if i* int('9'*n) < bestlatter[2]:
            return bestlatter[2]