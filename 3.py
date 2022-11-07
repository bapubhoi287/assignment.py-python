#write a python script to calculate sum of cubes of first N natural numbers
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1,1):
    cb=i*i*i
    sum=sum+cb
print("sum of first natural number cubes is:",sum,end=' ')
print()