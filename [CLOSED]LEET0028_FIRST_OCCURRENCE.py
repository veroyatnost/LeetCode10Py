#coding=utf-8

#list


def firstoccurrence_v0(haystack, needle):
    try:
        a = haystack.index(needle)
    except:
        a = 0
    return a

def firstoccurrence_v1(haystack, needle):
    for idx,item in enumerate(haystack):
        if item==needle:
            return idx
    else:
        return -1