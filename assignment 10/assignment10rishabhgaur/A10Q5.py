f=open("pass.txt","r")
i=input("enter the user name & pass:")
i=i.split()
a=f.readlines()
#########
for q in a:
    x=q.split()
    if x[0] in i and x[1] in i:
        print("your login is Succesfull")
        break
    elif x[0] not in i and x[1] in i:
        print("username doesn't exist")
    elif x[0] in i and x[1] not in i:
        print("username exist but pass were incorrect")
    else:
        pass
print()