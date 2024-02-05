# Get input from the user, specifying the number of terms
term = int(input("Enter number of terms: "))

# Use the map() function with a lambda function to generate a list of powers of 2
# The range(term) generates values from 0 to term-1
result = list(map(lambda x: 2**x, range(term)))

# Iterate through the result and print each element
for i in range(term):
    print(result[i])