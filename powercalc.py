# Get inputs from the user
try:
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the power (exponent): "))
    
    # Calculate the power
    result = base ** exponent
    
    # Print the result
    print(f"{base} raised to the power of {exponent} is: {result}")
    
except ValueError:
    print("Please enter valid numbers for the base and exponent.")
