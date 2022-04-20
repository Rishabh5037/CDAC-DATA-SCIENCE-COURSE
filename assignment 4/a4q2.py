st1 = set(input('enter a number:'))
st2 = set(input('enter another number:'))
print(st1)
print(st2)

# len
print(len(st1))
print(len(st2))

# min() max()
print(min(st1))
print(max(st1))
print(min(st2))
print(max(st2))

# union
st3 = st1|st2
print(st3)

# difference
st4 = st1.difference(st2)
print(st4)

st5 = st2.difference(st1)
print(st5)

# intersection
st6 = st1&st2
print(st6)

# symmetric_difference
st7 = st1.symmetric_difference(st2)
print(st7)

# issuperset
st8 = st3.issuperset(st1)
print(st8)

st9 = st3.issuperset(st2)
print(st9)

# issubset
st10 = st1.issubset(st3)
print(st10)

st11 = st2.issubset(st3)
print(st11)


