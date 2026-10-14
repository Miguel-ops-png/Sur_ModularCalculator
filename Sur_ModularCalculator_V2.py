# Modular Calculator Mini-Program
# Version 2: Improved comments, output formatting, and division by zero handling

def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2



print("=== MODULAR CALCULATOR ===")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("\nChoose an operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter your choice: ")



if choice == "1":
    result = add_numbers(num1, num2)
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == "2":
    result = subtract_numbers(num1, num2)
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == "3":
    result = multiply_numbers(num1, num2)
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == "4":
    result = divide_numbers(num1, num2)

    if result is None:
        print("\nError: Cannot divide by zero.")
    else:
        print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid choice. Please select an operation from 1 to 4.")