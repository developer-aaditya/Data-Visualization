# Create a program to calculate simple interest by creating a function

# Creating function to calculate si
def calculate_si(principle, roi, time):
    si = (principle * roi * time) / 100
    return si

# Main function
def main():
    print("-----------------------------------------")
    principle = float(input("Enter the principle(in rupees):"))
    roi = float(input("Enter rate of interest:"))
    time = int(input("Enter time period(in years):"))

    # Calling calculate_si function
    si = calculate_si(principle, roi, time)
    print("-------------------------------------------")
    print("The simple interest for the given data is :", si)

# Entry point
if __name__ == "__main__":
    main()
