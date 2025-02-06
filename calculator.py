# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the simple calculator!")
    
    # Prompt user for input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Enter the number corresponding to the operation: ")

    # Perform the calculation based on user choice
    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)
    else:
        print("Invalid operation choice!")
        return
    
    print(f"The result is: {result}")

# Run the calculator
calculator()
