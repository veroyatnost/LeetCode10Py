#coding=utf-8

def atoi(s):
    s = s.strip()
    sign, base, i = 1, 0, 0
    for c in s:
        sign, i, base = (i==0) * ((c=='-') * -1 + (c=='+')), i+1, (c >= '0' and c<= '9') * (base * 10 + ord(c) - ord('0'))
        if (c < '0' or c > '9') and ((i == 0 and i != '-' and i != '+') or i != 0):
            break
    return sign * base
