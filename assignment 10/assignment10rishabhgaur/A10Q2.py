# reading file
import os
F=open("docs2.txt")
a=[]
c=0
l=0

b=F.read()
print(b)

for i in b:
    if i=="" or i=="\n":
        pass
    else:
        a.append(i)

for j in b:
    if j=="" or j=="\n":
        c+=1

for k in b:
    if k=="\n":
        l+=1
print("The numbers of Characters :",len(a))
print("The numbers of Characters :",c)
print("The number of lines",len(i))