class Monkey:
    def __init__(self,start,operation,test,trueTest,falseTest) -> None:
        self.items=start
        self.operation=operation
        self.test=test
        self.trueTest=trueTest
        self.falseTest=falseTest
        self.inspected=0
    
    def __str__(self) -> str:
        return str(self.items)
    
def monkeyOperation(monkeyList,monkey,bigDivis=1):
    while len(monkeyList[monkey].items)!=0:
        monkeyList[monkey].inspected += 1
        item=monkeyList[monkey].items.pop(0)
        newItem=executeOperation(monkeyList[monkey].operation, item)
        #newItem=newItem//3 #Part 1
        newItem=newItem%bigDivis
        if newItem % (monkeyList[monkey].test)==0:
            monkeyList[monkeyList[monkey].trueTest].items.append(newItem)
        else:
            monkeyList[monkeyList[monkey].falseTest].items.append(newItem)

def executeOperation(string,old):
    stringList=string.split()
    i=0
    while i < len(stringList):
        if stringList[i]=="old":
            stringList[i]=old
        i+=1
    if stringList[3]=="+":
        return int(stringList[2])+int(stringList[4])
    elif stringList[3]=="*":
        return int(stringList[2])*int(stringList[4])
    else:
        return 0


monkeyList=[]
bigDivis=1
file = open("d11.txt","r")
f=file.readlines()
i=0
while i<len(f):

    startItems=(f[i+1].strip().split(": "))[1].split(", ")
    startItemsList=[]
    for j in startItems:
        startItemsList.append(int(j))
    
    operation=(f[i+2].strip().split(": "))[1]

    test=(f[i+3].strip().split(": "))[1]
    test=int(test.split()[2])
    bigDivis*=test

    testTrue=(f[i+4].strip().split(": "))[1]
    testTrue=int(testTrue.split()[3])

    testFalse=(f[i+5].strip().split(": "))[1]
    testFalse=int(testFalse.split()[3])

    monkey=Monkey(startItemsList,operation,test,testTrue,testFalse)
    monkeyList.append(monkey)
    i+=7
file.close()

for j in range(10000):
    for i in range(len(monkeyList)):
        #monkeyOperation(monkeyList,i) #Part 1
        monkeyOperation(monkeyList,i,bigDivis) #Part 2
inspectedList=[]
for monkey in monkeyList:
    inspectedList.append(monkey.inspected)
inspectedList.sort()
print(inspectedList[-1]*inspectedList[-2])