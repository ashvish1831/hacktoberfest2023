def print_diamond_pattern(n):
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        
        # Print asterisks
        for j in range(2 * i + 1):
            print("*", end="")
        
        print()  # Move to the next line

    for i in range(n - 2, -1, -1):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        
        # Print asterisks
        for j in range(2 * i + 1):
            print("*", end="")
        
        print()  # Move to the next line

if __name__ == "__main__":
    n = int(input("Enter the number of rows for the diamond: "))
    if n % 2 == 0:
        print("Please enter an odd number for a symmetric diamond.")
    else:
        print_diamond_pattern(n)
