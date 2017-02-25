#coding=utf-8

#LEET0022 #BinarySearchTree #CatalanNumber 

#Checkout Definition: Catalan Number.
#https://en.wikipedia.org/wiki/Catalan_number

def RootTrees(n):
    if n<0:
        raise StopIteration
    elif n==0 or n==1:
        yield "()"*n
    else:
        for i in range(0,n):
            for prefix in RootTrees(i):
                for suffix in RootTrees(n-1-i):
                    yield "("+prefix+")"+suffix
