a = ["Mobile","Laptop",100,"Camera",310.28,"Speakers",27.00,"Television",1000,"Laptop case","Camera lens"]
st=[]
num=[]
for i in a:
    if type(i)==str:
        st.append(i)
    elif type(i)== int or float:
        num.append(i)
    else:
        print("no")
print(st)
print(num)

#sort strings in ascending order:
st.sort(reverse=True)
print(st)

#sort string list in descending order:
num.sort()
print(st)

#lowest to highest
num.sort()
print(num)

#highest to lowest
num.sort(reverse=True)
print(num)
