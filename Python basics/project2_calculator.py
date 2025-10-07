# A calculator application
while True:
    # check the validity of user input
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operator. Please use one of +, -, *, /.")
            continue
        
        print(f"The result of {num1} {operator} {num2} = {result}")
        
        # Ask user if they want to perform another calculation
        choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thank you for using the calculator.")
            print("Exiting the calculator.")
            break
            
    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")
        continue