# Modular Calculator - Version 1


# Addition function
def add_numbers(num1, num2):
    return num1 + num2

# Subtraction function
def subtract_numbers(num1, num2):
    return num1 - num2

# Multiplication function
def multiply_numbers(num1, num2):
    return num1 * num2

# Division function
def divide_numbers(num1, num2):
    return num1 / num2



# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))



# Display the operation menu
print("\nChoose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter choice: ")



# Select and perform the operation
if choice == "1":
    result = add_numbers(num1, num2)
elif choice == "2":
    result = subtract_numbers(num1, num2)
elif choice == "3":
    result = multiply_numbers(num1, num2)
elif choice == "4":
    result = divide_numbers(num1, num2)
else:
    result = None
    print("Invalid operation choice.")



# Display the answer
if result is not None:
    print("Result:", result)
