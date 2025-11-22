# Calculate the factorial of a number

# Function for calculating the factorial
def calculate_factorial(n):
    # Base condition for exiting the loop
    if n == 0:
        return 1
    # Else calculating the factorial
    else:
        return n * calculate_factorial(n-1)

# Main method
def main():
    print("-----------------------------------------")
    # Taking the input from the user
    n = int(input("Enter a number greater than zero: "))

    # Storing the factorial in a variable
    fact = calculate_factorial(n)

    # Printing the factorial
    print("Factorial of given number is:", fact)

# Entry point
if __name__ == "__main__":
    main()