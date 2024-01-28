while True:
    user_in=input("Type 'bye' to quit the program OR write the year to find. ").lower() # lower() is used to convert user input to lower case alphabets
    if user_in == 'bye':
        break

    year=int(user_in) 
    if year % 4 == 0: # as we know every year perfectly divisible by 4 is a leap year
        print(f"{year} is a leaf year")
        break
    else:
        print(f"{year} is not a leaf year")
        break