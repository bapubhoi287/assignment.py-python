#write a python script to calculate sum of digits of a given numbers
n=int(input("enter a numbers:"))
s=0
while n>0:
    m=n%10
    s=m+s
    n=n//10
print("sum of digits is:",s)
print()
