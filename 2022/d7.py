dirDict={}
openDir=[]
dirDict["//"]=0
currentdir=""

file = open("d7.txt","r")
for line in file:
    parsedLine=line.strip().split()
    if parsedLine[0]=="$":
        if parsedLine[1]=="cd":
            if parsedLine[2]=="..":
                openDir.pop() # ($ cd ..)
                currentdir=openDir[-1]
            else:
                currentdir=currentdir+"/"+parsedLine[2]
                openDir.append(currentdir) # ($ cd dir)
    elif parsedLine[0]=="dir":
        newDir=currentdir+"/"+parsedLine[1]
        dirDict[newDir]=0
    elif int(parsedLine[0])!=0:
        for dir in openDir:
            dirDict[dir]+=int(parsedLine[0])
'''Part 1
total=0
for dir in dirDict:
    if dirDict[dir]<=100000:
        total+=dirDict[dir]
print(total)
'''
spaceNeeded=dirDict["//"]-40000000
spaceCreated=dirDict["//"]
for dir in dirDict:
    if spaceNeeded <= dirDict[dir] < spaceCreated:
        spaceCreated=dirDict[dir]
print(spaceCreated)
file.close()