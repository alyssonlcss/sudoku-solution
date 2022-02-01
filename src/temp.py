list = [[0,0,3,0,0,8,0,2,7],
        [6,8,7,0,4,2,0,1,0],
        [2,5,0,0,0,7,6,0,3],
        [0,4,0,0,0,6,0,0,0],
        [7,0,0,0,0,0,3,0,9],
        [0,0,0,4,0,3,2,0,6],
        [0,7,9,6,0,0,0,0,0],
        [5,0,8,2,0,9,7,6,0],
        [0,6,0,0,3,4,5,9,0]]


def loadingMatrix(fileList):
    size = len(fileList)
    matrix_game, list = [], []
    for i in range(size):
        if not i % 10 == 9:
            temp = fileList[i].split(" ")
            for j in range(9):
                list.append(int(temp[j]))
            matrix_game.append(list)
            list = []
        if i % 10 == 9: # We will call the function solve in this if
            solveSudoku(matrix_game)
            matrix_game.clear()