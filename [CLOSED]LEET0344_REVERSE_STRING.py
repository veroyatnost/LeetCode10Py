def reverseString(s):
    """
    Write a function that takes a string as input and returns the string reversed.
    """
    sList = list(s)
    for elements in range(int(len(s)/2)):
        sList[elements], sList[-(1+elements)] = sList[-(1+elements)], sList[elements]
    s = ''.join(sList)
    return s
