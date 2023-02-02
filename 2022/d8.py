import numpy as np

def makeArray(lines):
    array=[]
    for line in lines:
        a2=[int(x) for x in line.strip()]
        array.append(a2)
    return array
'''Part 1
def checkUp(treeBoard, checkBoard, rows, columns):
    for i in range(columns):
        current=-1
        for j in range(rows):
            if treeBoard[rows-1-j][i]<=current:
                continue
            current=treeBoard[rows-1-j][i]
            checkBoard[rows-1-j][i]=1
    return checkBoard
def checkDown(treeBoard, checkBoard, rows, columns):
    for i in range(columns):
        current=-1
        for j in range(rows):
            if treeBoard[j][i]<=current:
                continue
            current=treeBoard[j][i]
            checkBoard[j][i]=1
    return checkBoard
def checkLeft(treeBoard, checkBoard, rows, columns):
    for i in range(rows):
        current=-1
        for j in range(columns):
            if treeBoard[i][j]<=current:
                continue
            current=treeBoard[i][j]
            checkBoard[i][j]=1
    return checkBoard
def checkRight(treeBoard, checkBoard, rows, columns):
    for i in range(rows):
        current=-1
        for j in range(columns):
            if treeBoard[i][columns-1-j]<=current:
                continue
            current=treeBoard[i][columns-1-j]
            checkBoard[i][columns-1-j]=1
    return checkBoard
file = open("d8.txt","r")
treeBoard=makeArray(file.readlines())
rows=len(treeBoard)
columns=len(treeBoard[0])
checkBoard=[[0 for x in range(columns)] for x in range(rows)]
checkBoard=checkUp(treeBoard, checkBoard, rows, columns)
checkBoard=checkDown(treeBoard, checkBoard, rows, columns)
checkBoard=checkLeft(treeBoard, checkBoard, rows, columns)
checkBoard=checkRight(treeBoard, checkBoard, rows, columns)
total=0
for lines in checkBoard:
    total+=sum(lines)
print(total)
file.close()
'''
def checkUp(treeBoard, checkBoard, rows, columns, rowNum, colNum):
    current=treeBoard[rowNum][colNum]
    r=rowNum-1
    total=0
    while r>=0:
        if treeBoard[r][colNum]>=current:
            total+=1
            break
        total+=1
        r-=1
    checkBoard[rowNum][colNum]*=total
    return checkBoard
def checkDown(treeBoard, checkBoard, rows, columns, rowNum, colNum):
    current=treeBoard[rowNum][colNum]
    r=rowNum+1
    total=0
    while r<rows:
        if treeBoard[r][colNum]>=current:
            total+=1
            break
        total+=1
        r+=1
    checkBoard[rowNum][colNum]*=total
    return checkBoard
def checkLeft(treeBoard, checkBoard, rows, columns, rowNum, colNum):
    current=treeBoard[rowNum][colNum]
    c=colNum-1
    total=0
    while c>=0:
        if treeBoard[rowNum][c]>=current:
            total+=1
            break
        total+=1
        c-=1
    checkBoard[rowNum][colNum]*=total
    return checkBoard
def checkRight(treeBoard, checkBoard, rows, columns, rowNum, colNum):
    current=treeBoard[rowNum][colNum]
    c=colNum+1
    total=0
    while c<columns:
        if treeBoard[rowNum][c]>=current:
            total+=1
            break
        total+=1
        c+=1
    checkBoard[rowNum][colNum]*=total
    return checkBoard
file = open("d8.txt","r")
treeBoard=makeArray(file.readlines())
rows=len(treeBoard)
columns=len(treeBoard[0])
checkBoard=[[1 for x in range(columns)] for x in range(rows)]
for r in range(rows):
    for c in range(columns):
        checkBoard=checkUp(treeBoard, checkBoard, rows, columns,r,c)
        checkBoard=checkDown(treeBoard, checkBoard, rows, columns,r,c)
        checkBoard=checkLeft(treeBoard, checkBoard, rows, columns,r,c)
        checkBoard=checkRight(treeBoard, checkBoard, rows, columns,r,c)
print(np.max(checkBoard))
file.close()