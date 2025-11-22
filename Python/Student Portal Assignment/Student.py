# Student Management System

def main():
    """
    Main function to run the Student Management System
    This function displays the menu and handles user choices
    """
    # List to store all student records - each student is a dictionary
    students = []  
    
    while True:
        # Display the main menu options
        print("\n--- Student Portal ---")
        print("1. Registration of New Student")
        print("2. Student Profile")
        print("3. Delete Student")
        print("4. List of all Student sorted as per standard")
        print("5. List of Students of Particular Standard")
        print("6. List of students with attendance greater than 50% standard wise")
        print("0. Exit")
        
        # Get user's choice with error handling for non-numeric input
        try:
            choice = int(input("\nSelect any one operation: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue  # Go back to menu if input is not a number
        
        # Process user's choice based on input
        if choice == 0:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and end program
        elif choice == 1:
            register_student(students)  # Call function to add new student
        elif choice == 2:
            view_student_profile(students)  # Call function to view student details
        elif choice == 3:
            delete_student(students)  # Call function to remove student
        elif choice == 4:
            list_all_students_sorted(students)  # Call function to show all students sorted
        elif choice == 5:
            show_class_students(students)  # Call function to show students by class
        elif choice == 6:
            list_students_high_attendance(students)  # Call function to show good attendance
        else:
            print("Invalid choice! Please select a valid option.")


def register_student(students):
    """
    Register a new student with all required details
    This function collects student information and adds to the list
    """
    print("\n--- Student Registration ---")
    
    # Get student details from user
    student_id = input("Student id: ")
    
    # Check if student ID already exists to avoid duplicates
    for student in students:
        if student['id'] == student_id:
            print("Error: Student ID already exists!")
            return  # Exit function if ID exists
    
    # Collect other student information
    name = input("Name: ")
    standard = input("Standard: ")
    roll_no = input("Roll No.: ")
    
    # Validate attendance input - must be a number between 0-100
    # Note: There's a logical error in this validation - it will always show error
    # This needs to be fixed
    attendance = float(input("Attendance: "))
    if attendance < 0 or attendance > 100:
        print("Error: Attendance must be between 0 and 100!")
        return  # Exit if attendance is invalid
    else:
        print("Error: Attendance must be a number!")
        return  # This else part is incorrect and needs fixing
    
    # Create student dictionary to store all information
    student = {
        'id': student_id,        # Student ID
        'name': name,            # Student name
        'standard': standard,    # Class/standard
        'roll_no': roll_no,      # Roll number
        'attendance': attendance # Attendance percentage
    }
    
    # Add student to the main students list
    students.append(student)
    print("\nStudent Registered successfully.")


def view_student_profile(students):
    """
    Display profile of a specific student by ID
    This function searches for a student and shows their details
    """
    print("\n--- Student Profile ---")
    
    # Check if there are any students registered
    if not students:
        print("No students registered yet!")
        return  # Exit if no students
    
    # Get student ID to search for
    student_id = input("Enter Student ID to view profile: ")
    
    # Search for student by ID in the list
    for student in students:
        if student['id'] == student_id:
            # Display all details of found student
            print("\n--- Student Details ---")
            print(f"Student ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Standard: {student['standard']}")
            print(f"Roll No.: {student['roll_no']}")
            print(f"Attendance: {student['attendance']}%")
            return  # Exit after showing student details
    
    # This runs only if student not found
    print("Student not found!")


def delete_student(students):
    """
    Delete a student record by ID
    This function removes a student from the system
    """
    print("\n--- Delete Student ---")
    
    # Check if there are any students
    if not students:
        print("No students registered yet!")
        return
    
    # Get student ID to delete
    student_id = input("Enter Student ID to delete: ")
    
    # Search for student by ID and remove using index
    for i, student in enumerate(students):
        if student['id'] == student_id:
            students.pop(i)  # Remove student from list
            print("Student deleted successfully!")
            return  # Exit after deletion
    
    # This runs if student ID not found
    print("Student not found!")


def list_all_students_sorted(students):
    """
    Display all students sorted by their standard
    This function shows all students organized by class
    """
    print("\n--- List of all Students sorted as per standard ---")
    
    # Check if there are any students
    if not students:
        print("No students registered yet!")
        return
    
    # Sort students by standard (class) using lambda function
    # Lambda creates a temporary function that returns the standard value for each student
    sorted_students = sorted(students, key=lambda x: x['standard'])
    
    # Display sorted students with all their details
    for student in sorted_students:
        print(f"ID: {student['id']}, Name: {student['name']}, Standard: {student['standard']}, "
              f"Roll No: {student['roll_no']}, Attendance: {student['attendance']}%")


def show_class_students(students):
    """
    Display students of a particular standard/class
    This function filters and shows students from a specific class
    """
    print("\n--- Show Students by Class ---")
    
    # Check if students list is empty
    if not students:
        print("No students!")
        return
    
    # Get the class name to filter by
    class_name = input("Enter class: ")
    
    # Counter to track if we found any students
    count = 0
    
    # Loop through all students
    for student in students:
        # Check if student belongs to the requested class
        if student['standard'] == class_name:
            # Print header only when first student is found
            if count == 0:
                print(f"\nStudents in class {class_name}:")
            # Display student information
            print(f"{student['name']} (ID: {student['id']}) - Roll: {student['roll_no']}, Att: {student['attendance']}%")
            count += 1  # Increment counter
    
    # If no students found in that class
    if count == 0:
        print(f"No students in class {class_name}")


def list_students_high_attendance(students):
    """
    Display students with attendance greater than 50%, grouped by standard
    This function organizes students by class and filters by good attendance
    """
    print("\n--- List of students with attendance greater than 50% standard wise ---")
    
    # Check if there are any students
    if not students:
        print("No students registered yet!")
        return
    
    # Dictionary to group students by standard
    # Key: standard name, Value: list of students in that standard
    standards = {}
    
    # Loop through all students
    for student in students:
        # Check if student has attendance > 50%
        if student['attendance'] > 50:
            std = student['standard']  # Get student's standard
            
            # If this standard not in dictionary yet, add it with empty list
            if std not in standards:
                standards[std] = []
            
            # Add student to the list for their standard
            standards[std].append(student)
    
    # Check if we found any students with good attendance
    if not standards:
        print("No students with attendance greater than 50%!")
        return
    
    # Display students organized by standard
    # sorted(standards.keys()) sorts the class names alphabetically
    for standard in sorted(standards.keys()):
        print(f"\nStandard {standard}:")
        # Loop through students in this standard
        for student in standards[standard]:
            print(f"  ID: {student['id']}, Name: {student['name']}, Roll No: {student['roll_no']}, "
                  f"Attendance: {student['attendance']}%")


# Run the program only if this file is executed directly
# This prevents running if the file is imported as a module
if __name__ == "__main__":
    main()
