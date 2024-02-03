"""
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1
"""

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

num = int(input("Enter the number of terms for Fibonacci sequence to generate: ")) # Get user input for the number of terms in the Fibonacci sequence to generate

if num == 1: # Check if the user wants only the first term
    print(a)
# elif num == 2: # Check if the user wants only the first two terms
#     print(a)
#     print(b)
else:
    # Generate the Fibonacci sequence up to the specified number of terms
    print(a)
    print(b)
    for i in range(3, num+1):
        c = a + b  # Calculate the next term in the sequence
        a, b = b, c  # Update 'a' to the previous 'b', and 'b' to the newly calculated term 'c'
        print(c)   # Print the current term of the Fibonacci sequence

