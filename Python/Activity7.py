#get input from user as comma seperated list

my_list = input("Enter the value of sting in comma seperate format").split(",")

sum=0
print(my_list)

#iterate each num to get the sum
for num in my_list:
    sum+=int(num)
print(sum)





