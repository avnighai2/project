number = int(input("Enter a decimal number: "))
binary = ""

while number > 0:
    remainder = number % 2  # Get the remainder (0 or 1)
    binary = str(remainder) + binary  # Add the remainder to the front of the binary string
    number //= 2  # Divide the number by 2

print(f"The binary representation is {binary}.")
