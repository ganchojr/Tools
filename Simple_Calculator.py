print("-" * 50)
print(" ")
print("\t\tSimple Calculator by @var-log")
print(" ")
print("-" * 50)


# Add two numbers
def add(x, y):
    return x + y


# Subtract two numbers
def subtract(x, y):
    return x - y


# Multiplies two numbers
def multiply(x, y):
    return x * y


# Divides two numbers
def divide(x, y):
    return x / y


print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Quit")

while True:
    # User input
    choice = input("Enter choice(1/2/3/4/5): ")

    # Quit
    if choice in '5':
        print("Exiting program...")
        break

    # Check one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid input")



