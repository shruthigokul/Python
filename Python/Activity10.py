getTuple=input("Enter the numbers to be inside Tuple in comma seperated format").split(",")

(12,23,55,5,65,78,60)

for gt in getTuple:
    if (int(gt)%5)==0:
        print(gt)
    else:
        continue