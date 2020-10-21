import time

def valid(bord, num, pos):
    row = pos[0]
    col = pos[1]

    #box
    x = row // 3
    y = col // 3
    for i in range((x * 3), (x * 3) + 3):
        for k in range((y * 3), (y * 3) + 3):
            if bord[i][k] == num:
                return False

    #row
    if num in bord[row]:
        return False

    # column
    for i in range(len(bord)):
        if bord[i][col] == num:
            return False

    return True

def Solve(bord):
    empty = FindEmpty(bord)
    if not empty:
        return bord
    else:
        row, col = empty

    for i in range(1, 10):
        if valid(bord, i, (row, col)):
            bord[row][col] = i

            if Solve(bord):
                return True

            bord[row][col] = 0

    return False

def FindEmpty(bord):
    for i in range(len(bord)):
        for k in range(len(bord[i])):
            if bord[i][k] == 0:
                return (i, k) #row, column
