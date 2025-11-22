import mensuration

flag = True
while flag:
    print("-------------------------------------------------------------------")
    print("Select a shape:")
    print("1. Cylinder")
    print("2. Cone")
    print("3. Sphere")
    print("4. Cube")
    print("5. Cuboid")
    print("Enter 'q' to quit")
    choice = input("Enter your choice: ")
    print("-------------------------------------------------------------------")
    print("Select the mensuration:")
    print("1. Curved Surface Area")
    print("2. Total Surface Area")
    print("3. Volume")
    operation = input("Enter your choice: ")
    print("-------------------------------------------------------------------")

    if choice == "1":
        cylinder = mensuration.Cylinder()
        if operation == "1":
            cylinder.calculate_csa()
        elif operation == "2":
            cylinder.calculate_tsa()
        elif operation == "3":
            cylinder.calculate_volume()
        else:
            print("Invalid choice for mensuration.")
    elif choice == "2":
        cone = mensuration.Cone()
        if operation == "1":
            cone.calculate_csa()
        elif operation == "2":
            cone.calculate_tsa()
        elif operation == "3":
            cone.calculate_volume()
        else:
            print("Invalid choice for mensuration.")
    elif choice == "3":
        sphere = mensuration.Sphere()
        if operation == "1":
            sphere.calculate_csa()
        elif operation == "2":
            sphere.calculate_tsa()
        elif operation == "3":
            sphere.calculate_volume()
        else:
            print("Invalid choice for mensuration.")
    elif choice == "4":
        cube = mensuration.Cube()
        if operation == "1":
            cube.calculate_csa()
        elif operation == "2":
            cube.calculate_tsa()
        elif operation == "3":
            cube.calculate_volume()
        else:
            print("Invalid choice for mensuration.")
    elif choice == "5":
        cuboid = mensuration.Cuboid()
        if operation == "1":
            cuboid.calculate_csa()
        elif operation == "2":
            cuboid.calculate_tsa()
        elif operation == "3":
            cuboid.calculate_volume()
        else:
            print("Invalid choice for mensuration.")
    elif choice == "q":
        flag = False
    else:
        print("Invalid choice for shape.")



