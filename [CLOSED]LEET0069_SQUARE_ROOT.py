#coding=utf-8

#math

"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

# The Newton method, see wiki https://en.wikipedia.org/wiki/Integer_square_root
def sqrt(val):
  square_root = val
  while square_root ** 2 > val:
    square_root = (square_root + val/square_root) / 2
  return square_root
