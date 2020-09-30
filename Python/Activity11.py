fruits=dict(Apple="100",Orange="200",Banana="300")


checkFruit=input("Enter the fruit whose price has to be checked")

for f in fruits:
    if checkFruit==f:
        print("The fruit is available")
    else:
        continue

