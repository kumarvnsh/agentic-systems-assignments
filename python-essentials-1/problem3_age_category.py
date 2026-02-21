name = input("Enter your name: ")
print(f"Hello {name}")

try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative")
    else:
        # Determine age category
        if age < 13:
            print("You are a Child")
        elif age >= 13 and age <= 17:
            print("You are a Teenager")
        elif age >= 18 and age <= 59:
            print("You are an Adult")
        else:  # age >= 60
            print("You are a Senior Citizen")

        # Check voting eligibility
        if age >= 18:
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote")

except ValueError:
    print("Invalid age input")
