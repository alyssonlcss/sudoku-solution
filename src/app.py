

def readFile(pathFile):
    file = open(pathFile, 'r')
    fileList = []
    for line in file:
        line = line.rstrip()
        fileList.append(line)
    file.close()
    return fileList


def addMatrix(fileList):
    size = len(fileList)
    sudokuMatrix = []
    
    for i in range(size):
        if not i % 10 == 9:
            sudokuMatrix.append(fileList[i].split(" "))
        if i % 10 == 9: # We will call the function solve in this if
            for l in range(9):
                for c in range(9):
                    print(f'[{sudokuMatrix[l][c]}]', end=' ')
                print()
            sudokuMatrix.clear()
            print()


fileList = readFile("files/tests.txt")
addMatrix(fileList)