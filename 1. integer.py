number = int(input("Enter an integer to check weather it is positive, negative or zero: "))

if number > 0:
    print(f"{number} is a positive Integer")
elif number < 0:
    print(f"{number} is a negative Integer")
else:
    print(f"{number} is a zero integer")
