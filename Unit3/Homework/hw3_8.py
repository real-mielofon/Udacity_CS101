#THREE GOLD STARS

#Sudoku [http://en.wikipedia.org/wiki/Sudoku]
#is a logic puzzle where a game
#is defined by a partially filled
#9 x 9 square of digits where each square
#contains one of the digits 1,2,3,4,5,6,7,8,9.
#For this question we will generalize
#and simplify the game.


#Define a procedure, check_sudoku,
#that takes as input a square list
#of lists representing an n x n
#sudoku puzzle solution and returns
#True if the input is a valid
#sudoku square and returns False
#otherwise.

#A valid sudoku square satisfies these
#two properties:

#   1. Each column of the square contains
#       each of the numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the numbers from 1 to n exactly once.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

def check_line(l):
    for i in range(len(l)):
        if (i+1) not in l:
            return False
    return True

def check_sudoku(t):
    n = len(t)
    #check row
    for r in t:
        if not check_line(r):
            return False

    #check col
    for i in range(n):
        col = []
        for j in range(n):
            col.append(t[j][i])
        if not check_line(col):
            return False
    
    return True
    
print check_sudoku(correct)    
print check_sudoku(incorrect)
print check_sudoku([[1,3,2],
                    [2,3,1],
                    [3,1,2]])    
