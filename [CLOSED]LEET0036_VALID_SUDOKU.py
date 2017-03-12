#coding=utf-8

# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

# Check 3*3/Row/Column Contradiction is sufficient.

import numpy, itertools

def checker(subboard):
    l = np.array([item for item in subboard.flatten() if item>=0 and item<=9])
    return True if (len(l)==9 and np.all(np.bincount(np.array([ item for item in l if item>0 ]))==1)) else False

def SudokuValidator(board):
    for i,j in itertools.product(range(3),range(3)):
        if not(checker(board[i*3+j,:]) and checker(board[:,i*3+j]) and checker(board[i*3:(i+1)*3,j*3:(j+1)*3])):
            return False
    return True