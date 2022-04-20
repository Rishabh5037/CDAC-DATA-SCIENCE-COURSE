a = input("Enter a string:")
vowels=0
consonants=0
a.lower()
for i in a:
    if(i =='a' or i =='e' or i =='o' or i =='u'):
        vowels = vowels+1
    else:
        consonants = consonants+1
print("Total number of vowels in a string =",vowels)
print("Total number of consonants in a string =",consonants)
print()