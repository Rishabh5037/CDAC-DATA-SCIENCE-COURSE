# sum by defining a function
def cal_sum(a,b):
    return a+b
# sum by using lambda function
z = lambda x,y:x+y
# print using defined function
print(cal_sum(2,3))
# took two inputs
x =int(input("Input first number:"))
y = int(input("Input second number:"))
# stored result in z variable and called out the lambda function
result = z(x,y)
print(result)

#####################
# printing welcome message to names sent as an argument
a =['thor', 'boldour', 'kratos', 'freya']
print(type(a),a)
z=list(map(lambda x:print("hello",x),a))