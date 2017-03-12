# coding=utf-8

def romantointeger(roman):
    dec,dig = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}, 0
    for n in range(0,len(roman)):
        if n < len(roman) -1 and dec[roman[n]] < dec[roman[n+1]]:
            dig += 0 - dec[roman[n]]
        else:
            dig += dec[roman[n]]
    return dig




