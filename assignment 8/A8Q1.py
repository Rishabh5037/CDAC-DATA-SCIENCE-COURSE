# Adding two numbers
def add(a, b):
    sum = a + b
    print(a, "+", b, "=", sum)


# Subtract two numbers
def subtract(a, b):
    difference = a - b
    print(a, "-", b, "=", difference)


# Divide two numbers
def divide(a, b):
    division = a / b
    print(a, "/", b, "=", division)

# Modulus of two numbers
def modulus(a, b):
    modulus = a % b
    print(a, "%",b, "=",modulus)


# Menu Driven Heading
print("WELCOME TO CALCULATOR\n")

# using the while loop to print menu list
while True:
    print("MENU")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Modulus")
    print("5. Exit")
    users_choice = int(input("\nEnter your Choice: "))

    # based on the users choice the relevant method is called
    if users_choice == 1:
        print("\nPERFORMING ADDITION\n")
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        add(a, b)

    elif users_choice == 2:
        print("\nPERFORMING SUBTRACTION\n")
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        subtract(a, b)

    elif users_choice == 3:
        print("\nPERFORMING DIVISION\n")
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        divide(a, b)


    elif users_choice == 4:
        print("\nPERFORMING MODULUS\n")
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        modulus(a, b)


        # exit the while loop
    elif users_choice == 5:
        break

    else:
        print("Please enter a valid Input from the list")