'''Part 1
def scoring(li):
    score=ord(li[1])-87 #Scoring for choosing
    if ord(li[1])-ord(li[0])==23:
        score += 3
    elif li==["A", "Y"] or li==["B","Z"] or li==["C","X"]:
        score += 6
    return score
'''
def scoring(li):
    score=3*(ord(li[1])-88) #Scoring for result
    if li[1]=="X":
        li2=[3,1,2]
    elif li[1]=="Y":
        li2=[1,2,3]
    else:
        li2=[2,3,1]
    score+=li2[ord(li[0])-ord("A")]
    return score


file = open("d2.txt","r")
total=0
for line in file:
    li=line.split()
    total += scoring(li)
file.close()
print(total)