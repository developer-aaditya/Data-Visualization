import math
from math import pi

# Making a cylinder class
class Cylinder:

    # Constructor for the cylinder class
    def __init__(self):
        self.radius = float(input("Enter the radius of the cylinder: "))
        self.height = float(input("Enter the height of the cylinder: "))

    # Calculating Curved Surface Area for the cylinder
    def calculate_csa(self):
        csa = round(2 * pi * self.radius * self.height, 2)
        print("The Curved Surface Area of the cylinder is:", csa)

    # Calculating Total Surface Area for the cylinder
    def calculate_tsa(self):
        tsa = round(2 * pi * self.radius * (self.height + self.radius), 2)
        print("The Total Surface Area of the cylinder is:", tsa)

    # Calculating Volume of the cylinder
    def calculate_volume(self):
        vol = round(pi * self.radius * self.radius * self.height, 2)
        print("The Volume of the cylinder is:", vol)

# Making a Cone class
class Cone:

    # Constructor for the Cone class
    def __init__(self):
        self.radius = float(input("Enter the radius of the cone: "))
        self.height = float(input("Enter the height of the cone: "))
        self.slant_height = math.sqrt((self.radius ** 2) + (self.height ** 2))

    # Calculating Curved Surface Area for cone
    def calculate_csa(self):
        csa = round(pi * self.radius * self.slant_height, 2)
        print("The Curved Surface Area of the cone is:", csa)

    # Calculating Total Surface Area for cone
    def calculate_tsa(self):
        tsa = round(pi * self.radius * (self.slant_height + self.radius), 2)
        print("The Total Surface Area of the cone is:", tsa)

    # Calculating Volume of the cone
    def calculate_volume(self):
        volume = round((pi * (self.radius ** 2) * self.height) / 3, 2)
        print("The Volume of the cone is:", volume)

# Making a sphere class
class Sphere:

    # Constructor for the sphere class
    def __init__(self):
        self.radius = float(input("Enter the radius of the sphere: "))

    # Calculating Curved Surface Area for the sphere
    def calculate_csa(self):
        csa = round(4 * pi * (self.radius ** 2), 2)
        print("The Curved Surface Area of the sphere is:", csa)

    # Calculating Total Surface Area for the sphere
    def calculate_tsa(self):
        tsa = round(4 * pi * (self.radius ** 2), 2)
        print("The Total Surface Area of the sphere is:", tsa)

    # Calculating Volume of the sphere
    def calculate_volume(self):
        vol = round(4 * pi * (self.radius ** 3) / 3, 2)
        print("The Volume of the sphere is:", vol)

# Making a cube class
class Cube:

    # Constructor for the cube class
    def __init__(self):
        self.side = float(input("Enter the side of the cube: "))

    # Calculating Curved Surface Area for the cube
    def calculate_csa(self):
        csa = round(4 * (self.side ** 2), 2)
        print("The Curved Surface Area of the cube is:", csa)

    # Calculating Total Surface Area for the cube
    def calculate_tsa(self):
        tsa = round(6 * (self.side ** 2), 2)
        print("The Total Surface Area of the cube is:", tsa)

    # Calculating Volume of the cube
    def calculate_volume(self):
        vol = round(self.side ** 3, 2)
        print("The Volume of the cube is:", vol)

# Making a cuboid class
class Cuboid:

    # Constructor for the cuboid class
    def __init__(self):
        self.length = float(input("Enter the length of the cuboid: "))
        self.height = float(input("Enter the height of the cuboid: "))
        self.breadth = float(input("Enter the breadth of the cuboid: "))

    # Calculating Curved Surface Area for the cuboid
    def calculate_csa(self):
        csa = round(2 * self.height * (self.length + self.breadth), 2)
        print("The Curved Surface Area of the cuboid is:", csa)

    # Calculating Total Surface Area for the cuboid
    def calculate_tsa(self):
        tsa = round(2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length), 2)
        print("The Total Surface Area of the cuboid is:", tsa)

    # Calculating Volume of the cuboid
    def calculate_volume(self):
        vol = round(self.length * self.breadth * self.height, 2)
        print("The Volume of the cuboid is:", vol)
