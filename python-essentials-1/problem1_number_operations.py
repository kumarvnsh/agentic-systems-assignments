try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Print sum
    print(f"Sum: {num1 + num2}")

    # Print division result
    try:
        print(f"Division: {num1 / num2}")
    except ZeroDivisionError:
        print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
