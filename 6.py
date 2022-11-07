#write a python script to calculate factorial of a given number
n=int(input("enter a number:"))
fac=1
for i in range(1,n+1,1):
    fac=fac*i
print("factorial of a number is:",fac,end=' ')
print()
