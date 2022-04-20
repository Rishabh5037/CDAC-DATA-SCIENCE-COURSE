# program to demonstrate enumerate function
animals = ['deer','wolf','sloth','rabbit']
print(animals)
print(type(enumerate(animals)))

a = list(enumerate(animals))
print(a)

b = set(enumerate(animals))
print(b)

c = tuple(enumerate(animals))
print(c)

d = dict(enumerate(animals,5))
print(d)

for ele in a:
    print(ele)
for n,v in a:
    print(n,v)
print()