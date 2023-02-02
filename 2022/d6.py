file = open("d6.txt","r")
total=0
string=file.readline()
charli=[]
total=0
for char in string:
    total+=1
    #if len(charli)<3: #Part 1
    if len(charli)<13:
        charli.append(char)
        continue
    if char in charli or (len(set(charli)) != len(charli)):
        charli.pop(0)
        charli.append(char)
    else:
        break
print(total)
file.close()