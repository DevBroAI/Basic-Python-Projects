# Define a recursive function to calculate the factorial of a number 'a'
def fact(a):
    # Base case: If 'a' is 0, the factorial is 1
    if a == 0:
        return 1
    else:
        # Recursive case: Calculate 'a' times the factorial of 'a-1'
        return (a * fact(a - 1))

# Take user input for the number to find factorial
num = int(input("Enter a number to find factorial: "))

# Call the 'fact' function and print the result
print(f"The factorial of {num} is {fact(num)}")
