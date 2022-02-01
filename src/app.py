

def readFile(pathFile):
    file = open(pathFile, 'r')
    file_list = []
    for line in file:
        line = line.rstrip()
        file_list.append(line)
    file.close()
    return file_list


def viewMatrix(matrix):
    for l in range(9):
        for c in range(9):
            print(f'[{matrix[l][c]}]', end=' ')
        print()
    print()


def searchInGrid(row, column, n, matrix):
    for l in range(row[0], row[1]):
            for c in range(column[0], column[1]):
                if n == matrix[l][c]:
                    return False

def checkGrid(n, l, c, matrix):
    #grid 1
    if l < 3 and c < 3:
        return searchInGrid([0,3], [0,3], n, matrix)   
    #grid 2
    elif l < 3 and c in [3,4,5]:
        return searchInGrid([0,3], [3,6], n, matrix)  
    #grid 3
    elif l < 3 and c > 5:
        return searchInGrid([0,3], [6,9], n, matrix)
    #grid 4
    elif l in [3,4,5] and c < 3:
        return searchInGrid([3,6], [0,3], n, matrix)
    #grid 5
    elif l in [3,4,5] and c in [3,4,5]:
        return searchInGrid([3,6], [3,6], n, matrix)
    #grid 6
    elif l in [3,4,5] and c > 5:
        return searchInGrid([3,6], [6,9], n, matrix)
    #grid 7
    elif l > 5 and c < 3:
        return searchInGrid([6,9], [0,3], n, matrix)
    #grid 8
    elif l > 5 and c in [3,4,5]:
        return searchInGrid([6,9], [3,6], n, matrix)
    #grid 9
    elif l > 5 and c > 5:
        return searchInGrid([6,9], [6,9], n, matrix)


def checkPossibility(n, l, c, matrix):
    #row
    if n in matrix[l]:
        return False
    #column
    for l in range(9):
        if n == matrix[l][c]:
            return False
    #grid(3x3) 
    if checkGrid(n, l, c, matrix) == False:
        return False
    
    return True


def solveSudoku(matrix):
    for l in range(9):
        for c in range(9):
            if matrix[l][c] == 0:
                for num in range(1, 10):
                    if(checkPossibility(num, l, c, matrix)):
                        matrix[l][c] = num
                        solveSudoku(matrix)
                        matrix[l][c] = 0
                return
    viewMatrix(matrix)
    return


def loadingMatrix(fileList):
    size = len(fileList)
    matrix_game = []
    
    for i in range(size):
        if not i % 10 == 9:
            matrix_game.append(fileList[i].split(" "))
        if i % 10 == 9: # We will call the function solve in this if
            solveSudoku(matrix_game)
            matrix_game.clear()
    


file_list = readFile("files/tests.txt")
loadingMatrix(file_list)