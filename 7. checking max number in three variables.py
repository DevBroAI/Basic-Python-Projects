"""
in order to find the maximum number we will compare each number with the other numbers
we will use "and" operator for comparing one variable with multiple variables
"""
#taking input of 3 integers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

#now checking each variable
if num1 > num2 and num1 > num3: 
    print(f"{num1} is greater than all numbers.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is is greater than all numbers.")
else:
    print(f"{num3} is greater than all numbers.")