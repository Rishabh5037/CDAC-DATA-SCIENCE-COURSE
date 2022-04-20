listabc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']
listvow=['a','e','i','o','u']
# listnew=[]
z=list(map(lambda x,y:x if x in y,listvow,listabc))
print(z)
