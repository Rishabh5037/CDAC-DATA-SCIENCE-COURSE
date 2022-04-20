import os
f=open("num.txt",'r')
sum=0
z=f.readline()
for i in z.split():
    sum+=int(i)
print(sum)