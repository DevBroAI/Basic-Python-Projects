"""
prime number will be greater than 1
prime number is not divisible by any other integer
"""

num = int(input("Enter a number: "))

if num == 1: # check if the num == 1 
    print(f"{num} is not a prime number")
else:
    for i in range(2, num): #now we will check from 2 to num-1 to find prime number 
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
