fruits = (("mango", "grapes", "dragon fruit", "water melon"), ("kivi", "pomogrenade", "dates", "papaya", ""),
           ("apple", "banana", "orange", "lichi"))

name=input("Enter the name of fruit:")
fruit_available=False
for el in fruits:
    if name in el:
        fruit_available=True

if fruit_available:
    print("Fruit available")
else:
    print("Not available")

