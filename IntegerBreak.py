def  IntegerBreak(number):
    F = lambda n: 3**((n-2)/3)*2 if n%3==2 else ( 3**((n-4)/3)*4 if n%3==1 else 3**(n/3))
    return int(F(number))
