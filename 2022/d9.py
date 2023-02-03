def checkTail(headCor,tailCor):
    if headCor[0] == tailCor[0]+2:
        tailCor[0]=tailCor[0]+1
        # Diagonal cases
        if headCor[1]<tailCor[1]:
            tailCor[1]=tailCor[1]-1
        elif headCor[1]>tailCor[1]:
            tailCor[1]=tailCor[1]+1
        return tailCor
    elif headCor[0] == tailCor[0]-2:
        tailCor[0]=tailCor[0]-1
        #Diagonal cases
        if headCor[1]<tailCor[1]:
            tailCor[1]=tailCor[1]-1
        elif headCor[1]>tailCor[1]:
            tailCor[1]=tailCor[1]+1
    elif headCor[1] == tailCor[1]-2:
        tailCor[1]=tailCor[1]-1
        #Diagonal cases
        if headCor[0]<tailCor[0]:
            tailCor[0]=tailCor[0]-1
        elif headCor[0]>tailCor[0]:
            tailCor[0]=tailCor[0]+1
    elif headCor[1] == tailCor[1]+2:
        tailCor[1]=tailCor[1]+1
        #Diagonal cases
        if headCor[0]<tailCor[0]:
            tailCor[0]=tailCor[0]-1
        elif headCor[0]>tailCor[0]:
            tailCor[0]=tailCor[0]+1
    return tailCor

def part2Snake(h,t1,t2,t3,t4,t5,t6,t7,t8,t9):
    t1=checkTail(h,t1)
    t2=checkTail(t1,t2)
    t3=checkTail(t2,t3)
    t4=checkTail(t3,t4)
    t5=checkTail(t4,t5)
    t6=checkTail(t5,t6)
    t7=checkTail(t6,t7)
    t8=checkTail(t7,t8)
    t9=checkTail(t8,t9)
    return t1,t2,t3,t4,t5,t6,t7,t8,t9


headPosition=[0,0]
t1=[0,0] #Part 2
t2=[0,0] #Part 2
t3=[0,0] #Part 2
t4=[0,0] #Part 2
t5=[0,0] #Part 2
t6=[0,0] #Part 2
t7=[0,0] #Part 2
t8=[0,0] #Part 2
tailPosition=[0,0]
tailVisitSet=set()

file = open("d9.txt","r")
for line in file:
    parsedLine=line.strip().split()
    match parsedLine[0]:
        case "R":
            for i in range(int(parsedLine[1])):
                headPosition[0]+=1
                #tailPosition=checkTail(headPosition,tailPosition) #Part 1
                t1,t2,t3,t4,t5,t6,t7,t8,tailPosition=part2Snake(headPosition,t1,t2,t3,t4,t5,t6,t7,t8,tailPosition) #Part 2
                tailVisitSet.add(tuple(tailPosition))
        case "L":
            for i in range(int(parsedLine[1])):
                headPosition[0]-=1

                #tailPosition=checkTail(headPosition,tailPosition) #Part 1
                t1,t2,t3,t4,t5,t6,t7,t8,tailPosition=part2Snake(headPosition,t1,t2,t3,t4,t5,t6,t7,t8,tailPosition) #Part 2
                tailVisitSet.add(tuple(tailPosition))
        case "U":
            for i in range(int(parsedLine[1])):
                headPosition[1]+=1

                #tailPosition=checkTail(headPosition,tailPosition) #Part 1
                t1,t2,t3,t4,t5,t6,t7,t8,tailPosition=part2Snake(headPosition,t1,t2,t3,t4,t5,t6,t7,t8,tailPosition) #Part 2
                tailVisitSet.add(tuple(tailPosition))
        case "D":
            for i in range(int(parsedLine[1])):
                headPosition[1]-=1

                #tailPosition=checkTail(headPosition,tailPosition) #Part 1
                t1,t2,t3,t4,t5,t6,t7,t8,tailPosition=part2Snake(headPosition,t1,t2,t3,t4,t5,t6,t7,t8,tailPosition) #Part 2
                tailVisitSet.add(tuple(tailPosition))
print(tailVisitSet)
print(len(tailVisitSet))
file.close()