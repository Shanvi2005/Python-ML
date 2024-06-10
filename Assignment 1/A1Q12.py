n=int(input("enter number"))
x=n
sum=0
while(x!=0):
    a=x%10
    sum+=a
    x=x//10
print("The sum of digits of",n,"is ",sum)