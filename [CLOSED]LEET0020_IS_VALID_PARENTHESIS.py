# coding=utf-8


def isvalidparenthesis(a):
    dec = {")": "(", "]": "[", "}": "{","(":"(","[":"[","{":"{"}
    if len(a) % 2 != 0:
        return False
    else:
        for n, m in [a[n * 2:(n + 1) * 2] for n in range(0, len(a) / 2)]:
            if n != dec[m]:
                return False
    return True

