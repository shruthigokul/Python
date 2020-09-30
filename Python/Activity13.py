#Write a function sum() such that it can accept a list of elements and print the sum of all elements


def getSumAndListOfNum(n):
    sum=0
    for i in n:
        sum+=i
    str="the sum is {}".format(sum)
    print(str)



numList=[1,2,3,4,5]
getSumAndListOfNum(numList)