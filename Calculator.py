def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error! Division by zero")

def calculator():
    print("Welcome to Calculator")
    num1 = float(input("Enter First Number:\n"))

    while True:
        operation = input("Enter operation(+,-,*,/) or 'exit' to end:\n")

        if operation == 'exit':
            print("Hope U like it !!")
            break

        num2 = float(input("Enter second number:\n"))

        if operation == '+':
            result = add(num1, num2)

        elif operation == '-':
            result = subtract(num1, num2)

        elif operation == '*':
            result = multiply(num1, num2)

        elif operation == '/':
            result = divide(num1, num2)

        else:
            print("Invalid operation")

        print("Your answer is", result)

calculator()