# WAP to print the pattern

## Taking input from the user
n = int(input("Enter no of rows(greater than 0):"))

for i in range(1, n+1):
    print("  " * (i-1), "* " * (2 * (n - i) + 1))
