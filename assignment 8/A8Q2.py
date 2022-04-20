#taking a input from user
import math
a=int(input("enter a number :"))
result=0
#cube by function
def cubs(a):
    result=a**3
    return result
print(cubs(a))
#cube by lambda
lam_=lambda a:a**3
print((lam_(a)))
#squareroot
def sqt(a):
    result=math.sqrt(a)
    return result
print(sqt(a))
# SQRT lambda
lam_=lambda a:math.sqrt(a)
print("sqrt by lambda",lam_(a))