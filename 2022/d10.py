def makeString(positionCounter):
    answer=""
    for i in range(40):
        if i-1 <= positionCounter[i] <= i+1:
            answer+="#"
        else:
            answer+="."
    print(answer)

cycle=0
x=1
positionCounter=[]
#total=0 #Part 1
file = open("d10.txt","r")
'''Part 1
for line in file:
    parsedLine=line.strip().split()
    match parsedLine[0]:
        case "addx":
            cycle+=2
            if cycle%40==21:
                total+=(cycle-1)*x Part 1
            elif cycle%40==20:
                total+=cycle*x
            x+=int(parsedLine[1])
        case "noop":
            positionCounter.append(x)
            cycle+=1
            if cycle%40==20:
                total+=cycle*x
print(positionCounter)
file.close()
'''
file = open("d10.txt","r")
for line in file:
    parsedLine=line.strip().split()
    match parsedLine[0]:
        case "addx":
            positionCounter.append(x)
            positionCounter.append(x)
            cycle+=2
            if cycle%40==1:
                makeString(positionCounter)
                positionCounter=[positionCounter[-1]]
            elif cycle%40==0:
                makeString(positionCounter)
                positionCounter=[]
            x+=int(parsedLine[1])
        case "noop":
            positionCounter.append(x)
            cycle+=1
            if cycle%40==0:
                makeString(positionCounter)
                positionCounter=[]
file.close()