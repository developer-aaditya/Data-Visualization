# Taking input from the user
half = int(input("Enter no of rows:"))

n = 2 * half - 1

for i in range(1, half):
    print("* " * i + "  " * (n - 2 * i) + "* " * i)
print("* " * n)
