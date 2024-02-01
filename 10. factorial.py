# Get user input for a number
num = int(input("Enter a number to find factorial: "))

# Initialize the factorial variable to 1
factorial = 1

# Check if the number is negative
if num < 0:
    print(f"The factorial of {num} does not exist.")

# Check if the number is zero
elif num == 0:
    print("The factorial of zero is 1.")

# Calculate factorial for positive numbers
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
