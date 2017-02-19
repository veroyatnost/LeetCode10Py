#@tail_call_optimized
def neat_pow(x, binned_n , cachedx):
    if len(binned_n)==1:
        return x 
    else:
        return neat_pow(x**2 * (cachedx if binned_n[1]=='1' else 1), binned_n[1:], cachedx)
    
def neater_pow(x , n):
    return neat_pow(x , bin(n).split('b')[1] , x)

#@tail_call_optimized
def neat_pow_v2(x, binned_n):
    res = x
    for c in binned_n[1:]:
        res = res**2*(x if c=='1' else 1)
    return res

def neater_pow_v2(x , n):
    return neat_pow_v2(x , bin(n).split('b')[1])
def neater_pow_v3(x, n, extraprod=1):
    if 0 <= n <= 1:
        return extraprod * x**n
    else:
        return neater_pow_v3(x**2 ,n>>1, extraprod * x**(n%2) )
