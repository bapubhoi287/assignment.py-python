#write a python script to calculate sum of squares of first N natural numbers
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1,1):
    sq=i*i
    sum=sum+sq
print("sum of first natural numbers squars is:",sum,end=' ')
print()
