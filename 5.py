#write a python script to calculate sum of first N even natural numbers.


n=int(input("enter a numbers:"))
sum=0
for i in range(2,(2*n+2),2):
    sum=sum+i
print("sum of first even natural number is:",sum,end=' ')
print()
