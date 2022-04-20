import os
f=open("doc5.txt","r")
d=f.read()
f.close()
r=open("doc5.txt","w")
r.writelines(str(d.upper()))
print(d.upper())