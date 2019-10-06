import os

def PrintSudoku(array):
    for row in range(9):
        for col in range(9):
            print(array[row*9 + col], end =' ')
        print ()

def containsInRow(arr, num, row, col):
    rowElem = arr[row*9:row*9+9]
    return any(x == num for x in rowElem)

def containsInCol(arr, num, row, col):
    colElem = arr[col:82:9]
    return any(x == num for x in colElem)

def containsInBox(arr, num, row, col):
    box =[]
    boxrow = int(row/3)*3
    boxcol = int(col/3)*3
    for i in range(3):
        box += arr[boxrow*9 + boxcol:boxrow*9 + boxcol +3]
        boxrow+=1
    if any(x == num for x in box):
        return True
    else:
        return False

def isAllowed(arr, num, row, col):
    if (containsInCol(arr, num, row, col)):
        return False
    elif (containsInRow(arr, num, row, col)):
        return False
    elif (containsInBox(arr, num, row, col)):
        return False
    else:
        return True

def SolveSudoku(arr):
    for row in range(9):
        for col in range(9):
            if(not arr[row*9+col]):
                for num in range(1,10):
                    if (isAllowed(arr, num, row, col)):
                        arr[row*9+col] = num
                        if (SolveSudoku(arr)):
                            return True
                        else:
                            arr[row*9+col] = 0
                return False
    return True

#sudoku_Arr = [0,0,0,  0,0,0,  0,0,0,
#              0,0,0,  0,0,0,  0,0,0,
#              0,0,0,  0,0,0,  0,0,0,

#              0,0,0,  0,0,0,  0,0,0,
#              0,0,0,  0,0,0,  0,0,0,
#              0,0,0,  0,0,0,  0,0,0,

#              0,0,0,  0,0,0,  0,0,0,
#              0,0,0,  0,0,0,  0,0,0,
#              0,0,0,  0,0,0,  0,0,0]

sudoku_Arr = [6,0,0,  7,1,0,  0,0,2,
              3,0,0,  0,0,0,  0,9,6,
              8,0,0,  0,0,0,  0,0,5,

              0,0,9,  0,0,0,  0,0,0,
              0,0,0,  0,0,0,  4,2,9,
              0,7,0,  8,0,0,  0,0,0,

              0,0,0,  0,0,3,  0,5,0,
              1,3,0,  0,0,7,  0,0,0,
              0,2,0,  0,5,4,  0,0,0]

sudoku_Arr_Exp1 =  [0,0,0,  0,1,7,  0,0,0,
                    2,0,8,  0,0,0,  0,0,4,
                    0,0,3,  0,2,0,  1,0,0,

                    9,6,0,  0,0,0,  3,0,0,
                    0,0,0,  6,0,0,  0,9,0,
                    0,0,0,  0,0,8,  5,0,0,

                    6,0,0,  3,0,1,  2,0,0,
                    0,3,1,  7,0,0,  0,0,8,
                    0,0,0,  0,0,0,  0,0,0]

SolveSudoku(sudoku_Arr)

PrintSudoku(sudoku_Arr)