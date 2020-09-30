list1=[1,2,3,4,5,6,7]
list2=[9,8,7,6,5,4,3,2,4]

newlist=[]


for l1 in list1:
    if (l1%2)!=0:
        newlist.append(l1)
    else:
        continue

for l2 in list2:
    if (l2%2)==0:
        newlist.append(l2)
    else:
        continue

print(newlist)

