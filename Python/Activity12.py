#Write a recursive function to calculate the sum of numbers from 0 to 10

def sum(n):
    if(n<=0):
        return n
    else:
        return n+sum(n-1)
num=10
print("The sum of numbers from 0 to 10 is",sum(num))
