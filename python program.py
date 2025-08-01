# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y
        
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = None
        num2 = None
        
        # while user input is not valid
        while type(num1) is not float:
            try:
                num1 = float(input("Enter first number: ")) 
            except Exception:
                print("Not a valid number, Please try again")        
        while type(num2) is not float:
            try:
                num2 = float(input("Enter second number:"))
            except Exception:
                print("Not a valid number")

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        options = ["yes","no"]
        next_calculation = None
        while next_calculation not in options:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                quit()
            else:
                print("Not a valid decision")
    
    else:
        print("Invalid Input")