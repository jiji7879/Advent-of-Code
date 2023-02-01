import numpy as np

'''Part 1
file = open("d1.txt","r")
sum=0
max=0
for line in file:
    try:
        sum += int(line)
    except:
        if sum > max:
            max=sum
        sum=0
file.close()
print(max, sum)
'''

file = open("d1.txt","r")
sum=0
li=[]
for line in file:
    try:
        sum += int(line)
    except:
        li.append(sum)
        sum=0
file.close()
li.append(sum)
li.sort()
print(li[-1]+li[-2]+li[-3])