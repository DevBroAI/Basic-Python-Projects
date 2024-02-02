# Get user input for temperature in Celsius
celcius = int(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32
farenheit = (celcius * 9/5) + 32

# Display the converted temperature
print(f"The {celcius} Celsius is equal to {farenheit} Fahrenheit")
