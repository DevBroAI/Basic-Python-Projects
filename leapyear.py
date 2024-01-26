while True:
    user_in=input("Type 'bye' to quit the program OR write the year to find. ").lower()
    if user_in == 'bye':
        break

    year=int(user_in)
    if year % 4 == 0:
        print(f"{year} is a leaf year")
        break
    else:
        print(f"{year} is not a leaf year")
        break