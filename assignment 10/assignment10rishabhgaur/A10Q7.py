import os
import random
f=open("num.txt","w+")
for i in range(0,5):
    ranum = random.randint(1, 500)
    f.write(str(ranum))
    f.write(" ")
print()
f.close()