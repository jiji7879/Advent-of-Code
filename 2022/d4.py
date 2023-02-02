file = open("d4.txt","r")
total=0
for line in file:
    line=line.replace(",","-").strip().split("-")
    for item in line:
        item = int(item)
    '''Part 1
    if int(line[0]) <= int(line[2]) and int(line[1]) >= int(line[3]):
        total+=1
    elif int(line[0]) >= int(line[2]) and int(line[1]) <= int(line[3]):
        total+=1
    '''
    total+=1
    if int(line[1]) < int(line[2]) or int(line[3]) < int(line[0]):
        total-=1
file.close()
print(total)