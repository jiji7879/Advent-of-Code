
gameboard=[]
queue=[]
end=[]
file = open("d12.txt","r")
for line in file:
    line=line.strip()
    lineChars=[i for i in line]
    j=0
    while j<len(line):
        #if line[j]=="S": #Part 1
        if line[j]=="a": #Part 2
            queue.append(['a', [len(gameboard), j], 0])
        elif line[j]=="E":
            end=[len(gameboard), j]
        j+=1
    gameboard.append(lineChars)
file.close()

def checking(X,Y,thing,checkboard,gameboard,scoreBoard,queue):
    if checkboard[X][Y]==0 and ((ord(gameboard[X][Y])-ord(thing[0]) <= 1 and gameboard[X][Y]!="E") or (gameboard[X][Y]=="E" and thing[0]=="z")):
        if gameboard[X][Y]=="E" and thing[0]=="z":
            print(thing[2]+1)
        checkboard[X][Y]=1
        scoreBoard[X][Y]=thing[2]+1
        queue.append([gameboard[X][Y], [X, Y], thing[2]+1])
    return checkboard,gameboard,scoreBoard,queue

checkboard=[[0 for i in gameboard[0]] for j in gameboard]
for item in queue:
    checkboard[item[1][0]][item[1][1]]=1
scoreBoard=[[0 for i in gameboard[0]] for j in gameboard]
while len(queue)>0:
    thing=queue.pop(0)
    coordX=thing[1][0]
    coordY=thing[1][1]
    if coordX-1>=0:
        checkboard,gameboard,scoreBoard,queue=checking(coordX-1,coordY,thing,checkboard,gameboard,scoreBoard,queue)
    if coordX+1<len(gameboard):
        checkboard,gameboard,scoreBoard,queue=checking(coordX+1,coordY,thing,checkboard,gameboard,scoreBoard,queue)
    if coordY+1<len(gameboard[0]):
        checkboard,gameboard,scoreBoard,queue=checking(coordX,coordY+1,thing,checkboard,gameboard,scoreBoard,queue)
    if coordY-1>=0:
        checkboard,gameboard,scoreBoard,queue=checking(coordX,coordY-1,thing,checkboard,gameboard,scoreBoard,queue)