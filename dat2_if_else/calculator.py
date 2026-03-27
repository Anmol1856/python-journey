# calculator.py

print("\n Calculator ")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    op = input("Enter operation (+, -, *, /, %): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Cannot divide by zero")
    elif op == "%":
        if b != 0:
            print("Result:", a % b)
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid operation")

except:
    print("Invalid input! Please enter numbers only.")