import os
F=open("docs.txt","r")
r=list(F.read())
s=str()
r.reverse()
for i in r:
    s+=i
print(s)

F.close()