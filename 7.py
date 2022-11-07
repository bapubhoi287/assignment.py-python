#write a python script to count digits in a given number
n=int(input("enter a number:"))
count=0
while n>0:
    #m=n%10
    n=n//10
    count=count+1
print("count digit is:",count)
print()

