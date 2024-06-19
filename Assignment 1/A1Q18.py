a=input("enter first string")
b=input("enter second string")
a=a.lower().replace(" ","")
b=b.lower().replace(" ","")
sizeA=len(a)
SizeB=len(b)
i=0
j=SizeB-1
flag=0
while(i<sizeA and j>=0):
    if(a[i]!=b[j]):
        flag=1
        break
    i+=1
    j-=1
if(flag==0):
    print("is a anagram")
else:
    print("is not an anagram")