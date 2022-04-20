x = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
print("Initial list:",x)
num=int(input("Enter the number:"))
new_list=[]
i=3
while i>0:
    i-=1
    list_temp=list(x.pop(0))
    list_temp.pop()
    list_temp.append(num)
    x.append(tuple(list_temp))

print(x)
