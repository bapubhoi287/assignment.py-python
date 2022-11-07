#write a python script to calculate sum of first N natural numbers.
n=int(input("ente a number:"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print("sum of first natural numbers is:",sum,end=' ')
print()
    
    