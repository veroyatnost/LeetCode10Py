#coding=utf-8

IntegerBreak = lambda n: 3**((n-2)/3)*2 if n%3==2 else 3**((n-4)/3)*4 if n%3==1 else 3**(n/3)
