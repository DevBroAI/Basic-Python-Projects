"""
the filter function is used to filter out specific variable in a sequence
syntax --> variable=list(filter(function, sequence))
"""

numbers = [13, 18, 20, 12, 8, 30]
divider= int(input("enter a number: ")) # Get input from the user, specifying the number for which we want to filter multiples
result = list(filter(lambda x: x%divider == 0, numbers))
print(result)