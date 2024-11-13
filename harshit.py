number = int(input("Enter a number: "))
count = 0

while number > 0:
    number //= 10  # Reduce the number by removing the last digit
    count += 1  # Increase the digit count

print(f"The number of digits is {count}.")
