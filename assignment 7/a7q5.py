import math
import random
lst1 = []
lst2 = []
for i in range(0,1001,5):
    lst1.append(i)
print(lst1)
print(min(lst1))
print(max(lst1))
for i in range(5):
    lst2.append(random.choice(lst1))
print(lst2)
print(min(lst2))
print(max(lst2))

print(lst2[0]**4)
print(math.sqrt(lst2[1]))
print(math.factorial(lst2[2]))
print(lst2[3]*2)
print(sum(lst2))
