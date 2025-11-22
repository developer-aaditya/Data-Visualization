# Create a program to print all the even factors of a given no using function

# Function to print even factors of a no
def print_even_factors(n):
    print("Even factors of the given no are :")
    # Entering in loop for 1 to n
    for i in range(1, n + 1):
        if i % 2 == 0 and n % i == 0:
            print(i)
        else:
            pass

n = int(input("Enter a number: "))
print_even_factors(n)