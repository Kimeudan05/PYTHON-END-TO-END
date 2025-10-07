# multiplication table of a given number
while True:
    try:
        num = int(input("Enter a number to generate its multiplication table: "))
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue
    # Print multiplication table
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    
    # Ask user if they want to try again with a different number
    choice = input("Do you want to try another number? (y/n): ").strip().lower()
    if choice != 'y':
        print("Exiting the program.")
        break# exit()

# multiplication table for numbers 1 to 10
print("Multiplication tables from 1 to 10:")
for n in range(1, 11):  
    print(f"\nMultiplication table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        
# multiplication table in a grid format
print("\nMultiplication table in grid format (1 to 10):")
for row in range(1, 11):
    for col in range(1, 11):
        print(f"{row * col:4}", end=" ")
    print()