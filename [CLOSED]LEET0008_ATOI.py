#coding=utf-8

#math #string

"""
Given a string, implement atoi to convert a string to an integer.
int atoi(int);

"""
#Solution 1 by Chuanzhen Wu
def atoi_v1(s):
    s = s.strip()
    sign, base, i = 1, 0, 0
    for c in s:
        sign, i, base = (i==0) * ((c=='-') * -1 + (c=='+')), i+1, (c >= '0' and c<= '9') * (base * 10 + ord(c) - ord('0'))
        if (c < '0' or c > '9') and ((i == 0 and i != '-' and i != '+') or i != 0):
            break
    return sign * base

#Modified
def atoi_v2(num_s):
	num_s = num_s.strip()
  sign, base = 1, 0
  for i,c in enumerate(num_s):
      if (not c in "0123456789") and not (i == 0 and c in "-+"):
          break
      sign = -1 if num_s[0] == '-' else 1
      base = (base * 10 + ord(c) - ord('0')) if not c in "-+" else 0
  return max(-(1<<31), min(sign * base, (1<<31)-1))