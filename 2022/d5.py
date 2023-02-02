import re
'''Test Stacks
li1=["Z","N"]
li2=["M","C","D"]
li3=["P"]
stack=[li1,li2,li3]
'''
li1=["B","V","S","N","T","C","H","Q"]
li2=["W","D","B","G"]
li3=["F","W","R","T","S","Q","B"]
li4=["L","G","W","S","Z","J","D","N"]
li5=["M","P","D","V","F"]
li6=["F","W","J"]
li7=["L","N","Q","B","J","V"]
li8=["G","T","R","C","J","Q","S","N"]
li9=["J","S","Q","C","W","D","M"]
stack=[li1,li2,li3,li4,li5,li6,li7,li8,li9]


file = open("d5.txt","r")
for line in file:
    ins=re.findall("\d+", line)
    for i in range(int(ins[0])):
        #char=stack[int(ins[1])-1].pop() #Part 1
        char=stack[int(ins[1])-1].pop(len(stack[int(ins[1])-1])-int(ins[0])+i) #Part 2
        stack[int(ins[2])-1].append(char)
file.close()


print(stack)
string=""
for l in stack:
    if len(l)>0:
        string += l[-1]
print(string)