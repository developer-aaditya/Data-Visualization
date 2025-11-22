##Taking input no of rows
n = int(input("Enter no of rows(greater than 0):"))

half = n//2
for i in range(1, half+1):
    if(i == 1):
        print("* " * n)
    else:
        print("* " + "  " * (i-2) + "* " + "  " * (n-2*i) + "* " + "  " * (i-2) + "* ")

print("* " + "  " * (half-1) + "* " + "  " * (half-1) + "* ")

for i in range(1, half+1):
    if i == half:
        print("* " * n)
    else:
        print("* " + "  " * (half-i-1) + "* " + "  " * (2*i-1) + "* " + "  " * (half-i-1) + "* ")
