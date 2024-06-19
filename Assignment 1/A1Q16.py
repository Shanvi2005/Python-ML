text=input("enter text")
count={}
for i in text:
    if i in count:
        count[i]+=1;
    else:
        count[i]=1;
print(count)
