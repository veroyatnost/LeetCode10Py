#coding=utf-8

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''
import itertools

def add_two_numbers(number1,number2):
    list1 = number1.split("->")
    list2 = number2.split("->")
    newlist = []
    carry = 0
    for n,m in list(itertools.zip_longest(list1,list2)):
        if int(n or 0) + int(m or 0) + carry < 10:
            newlist.append(str(int(n or 0) + int(m or 0) + carry))
            carry = 0
        else:
            newlist.append(str(int(n or 0) + int(m or 0) + carry - 10))
            carry = 1
    return "->".join(newlist)


