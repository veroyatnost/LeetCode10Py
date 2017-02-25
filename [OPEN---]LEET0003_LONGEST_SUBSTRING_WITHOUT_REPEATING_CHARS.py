#coding=utf-8

# Longest Substring Without Repeating Characters

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question.
'''


def longestsubstring(string):
    lword = {}
    n = ''
    for i in string:
        if i not in n:
            n += i
        else:
            lword[len(n)] = n
            n = i
    return lword[max(lword.keys())]