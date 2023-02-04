def parseLists(listOfChars):
    starting=[]
    charString=""
    while len(listOfChars)>0:
        char=listOfChars.pop(0)
        if char=="[":
            (aList, listOfChars)=parseLists(listOfChars)
            starting.append(aList)
        elif char=="]":
            if charString!="":
                starting.append(int(charString))
            return (starting, listOfChars)
        elif char==",":
            if charString!="":
                starting.append(int(charString))
            charString=""
        else:
            charString+=char
    return starting[0]

def comparitor(left, right): #returns 1 if correct, -1 if incorrect, 0 if tie
    if type(left)==type(right):
        if type(left)==type(4):
            if left==right:
                return 0
            elif left<right:
                return 1
            else:
                return -1
        elif type(left)==type([]):
            i=0
            while i<min(len(left), len(right)):
                result=comparitor(left[i], right[i])
                if result!=0:
                    return result
                i+=1
            if len(left)==len(right):
                return 0
            elif len(left)<len(right):
                return 1
            else:
                return -1
    else:
        if type(left)==type(4):
            return comparitor([left], right)
        return comparitor(left, [right])

'''Part 1
total=0
counter=0
file=open("d13.txt","r")
allLines=file.readlines()
i=0
while i < len(allLines):
    counter=counter+1
    first=allLines[i].strip()
    a = parseLists([i for i in first])
    second=allLines[i+1].strip()
    b = parseLists([i for i in second])
    if comparitor(a,b)==1:
        total+=counter
    i+=3
file.close()
print(total)
'''

arrayOfArrays=[[[2]], [[6]]]
counter=0
file=open("d13.txt","r")
allLines=file.readlines()
i=0
while i < len(allLines):
    counter=counter+1
    first=allLines[i].strip()
    a = parseLists([i for i in first])
    arrayOfArrays.append(a)
    second=allLines[i+1].strip()
    b = parseLists([i for i in second])
    arrayOfArrays.append(b)
    i+=3
file.close()

for i in range(len(arrayOfArrays)):
    for j in range(len(arrayOfArrays)-1):
        if comparitor(arrayOfArrays[j], arrayOfArrays[j+1])==-1:
            temp=arrayOfArrays[j+1]
            arrayOfArrays[j+1]=arrayOfArrays[j]
            arrayOfArrays[j]=temp
print((arrayOfArrays.index([[2]])+1)*(arrayOfArrays.index([[6]])+1))