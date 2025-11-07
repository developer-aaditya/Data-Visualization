# To Calculate the simple interest
# We need to take input principle, time and rate of interest

principle = float(input("Enter the principle of amount : "))
time = float(input("Enter the time period in year : "))
rate_of_interest = float(input("Enter the rate of interest : "))

# Calculating the simple interest

simple_interest = (principle * time * rate_of_interest)/100

total_amount = principle + simple_interest

print("-------------------------------------------------")
print("Simple Interest is : ",simple_interest)
print("Total Amount is : ", total_amount)
