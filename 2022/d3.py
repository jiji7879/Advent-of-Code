'''Part 1
file = open("d3.txt","r")
total=0
for line in file:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    for char in firstpart:
        if char in secondpart:
            if char.isupper():
                total+=ord(char)-ord("A")+27
            else:
                total+=ord(char)-ord("a")+1
            break
file.close()
print(total)
'''
file = open("d3.txt","r")
total=0
li=file.readlines()
for i in range(len(li)//3):
    for char in li[3*i+1]:
        if char in li[3*i] and char in li[3*i+2]:
            if char.isupper():
                total+=ord(char)-ord("A")+27
            else:
                total+=ord(char)-ord("a")+1
            break
file.close()
print(total)