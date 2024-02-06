num = int(input("enter a number: "))

for i in range(1, 101):
    if i%num == 0:     # Check if the current number 'i' is divisible by the user-provided number 'num'
        print (f"{i} is divisible by {num}")


