def calculator():
    num1 = float(input("first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("second number: "))
    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator")
calculator()
