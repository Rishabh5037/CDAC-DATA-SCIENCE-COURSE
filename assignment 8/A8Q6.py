# Temperature conversion for given temperature in celsius and fahrenheit.

temp_celsius = (36.5,37,37.5,39)
# usage of lambda for conversion
b = list(map(lambda i:(i*9/5) + 32,temp_celsius))
# printing(b)
print(b)
# using list as fahrenheit
temp_fahrenheit = (36.5,37,37.5,39)
#usage of lambda for conversion
c = list(map(lambda j:(j-32) * 5/9,temp_fahrenheit))
# printing(c)
print(c)