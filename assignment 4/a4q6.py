x = [(10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 92, 56), (1, 2, 3, 4)]
maxl=[]
minl=[]
avl=[]
for el in x:
    maxl.append(max(el))
    minl.append(min(el))
    avl.append(sum(el)/4)

print("Maximum:",maxl)
print("Minimum:",minl)
print("Average:",avl)

