a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=input("enter operator +,-,*,/")
result=0
if(c=="+"):
    result=a+b
elif (c=="-"):
    result=a-b
elif (c=="*"):
    result = a*b
else:
    result=a/b
print(result)
  