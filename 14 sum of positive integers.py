# num = int(input("Enter a positive integer: "))
# if num<0:
#     print("Please enter a positive integer")
# else:
#     sum=0
#     for i in range(1, num+1):
#         sum += i
# print(sum)

num = int(input("Enter a positive integer: "))
if num<0:
    print("Please enter a positive integer")
else:
    sum=0
    for i in range (num, 0, -1):
        sum += i
    print(sum)