# Get user input for the number to generate the table
number = int(input("Enter a number to generate the table: "))

# Use a for loop to iterate from 1 to 10 and print the multiplication table
for i in range(1, 11):
    # Display the multiplication expression and result
    print(f"{number} x {i} = {number * i}")
