

def readFile(pathFile):
    file = open(pathFile, 'r')
    fileList = []
    for line in file:
        line = line.rstrip()
        fileList.append(line)
    file.close()
    return fileList

def viewMatrix(matrix):
    for l in range(9):
        for c in range(9):
            print(f'[{matrix[l][c]}]', end=' ')
        print()
    matrix.clear()
    print()


def lesserSpace(matrix):
    countVoidC, countVoidL = 0, 0
    for c in range(9):
        for l in range(9):
            if matrix[c][l] == 0:
                countVoidL += 1


def loadingMatrix(fileList):
    size = len(fileList)
    sudokuMatrix = []
    
    for i in range(size):
        if not i % 10 == 9:
            sudokuMatrix.append(fileList[i].split(" "))
        if i % 10 == 9: # We will call the function solve in this if
            viewMatrix(sudokuMatrix)


fileList = readFile("files/tests.txt")
loadingMatrix(fileList)