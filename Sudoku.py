
def valid(bo, num, row,column):
    # Check row
    for i in range(len(bo[0])):
        if bo[row][i] == num and column != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][column] == num and row != i:
            return False

    # Check box
    x = row // 3
    y = column // 3

    for i in range(x*3, x*3 + 3):
        for j in range(y * 3, y*3 + 3):
            if bo[i][j] == num and (i!=row and j!=column):
                return False

    return True



def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
