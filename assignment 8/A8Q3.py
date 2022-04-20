#list
list1=[1,4,6,3,43,7,8,5,5,8996,6,5,5,4,535,57,35,28,21]
print(list1)
x=list(filter(lambda x:x%7==0,list1))
print(list(x))