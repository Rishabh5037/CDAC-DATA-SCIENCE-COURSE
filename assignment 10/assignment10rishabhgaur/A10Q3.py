# taking Fruits list Adding to file
import os
a=["Papaya","Orange","waterMelon","Litchi","banana"]
F=open("docs3.txt","w")
for i in a:
    F.write(i)
    F.write(" ")
F.close()
print()