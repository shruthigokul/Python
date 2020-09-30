num=input("Enter a list of numbers in comma seperated format").split(",")

if int(num[0])==int(num[-1]):
    print("Frist number is equal to the last number")
else:
    print("First number is not equal to the last number")


print(num[1:2])
