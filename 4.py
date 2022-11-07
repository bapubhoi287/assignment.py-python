#write a python script to calculate sum of first N odd natural numbers
n=int(input("enter a numbers:"))
sum=0
for i in range(1,(2*n+1),2):
    sum=sum+i
print("sum of first odd natural number is:",sum,end=' ')
print()

