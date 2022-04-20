a=(1,2,3,4)
b=(3,5,2,1)
c=(2,2,3,1)
sumli=[]
for x in range(len(a)):
    sumli.append(a[x]+b[x]+c[x])

print(tuple(sumli))
