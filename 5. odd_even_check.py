number= int(input("Enter a number: "))

if number % 2 == 0: #as we know even number are perfectly divisible by 2 and have 0 as reminder
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")