# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Kevin Amaral,8-28-24, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

student_data:list[str] # list of strings/dictionary
students: list = []  # a table of student data


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        # Transform the data from the file
        student_data = row.strip().split(',')
        student_first_name=student_data[0]
        student_last_name=student_data[1]
        course_name=student_data[2]
        student_data={'first_name':student_first_name, 'last_name':student_last_name, 'course':course_name}
        students.append(student_data)
    file.close()
except FileNotFoundError as e1:
    print('File not found')
    print(e1, e1.__doc__,type(e1), sep='\n')

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('Nope. The first name must be alphabetic')
        except ValueError as e1:
            print (e1)
            print('Invalid input, please enter only alphabetical information')
            student_first_name = input("Re-enter the student's first name: ")
        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('Nope. The last name must be alphabetic')
        except ValueError as e1:
            print (e1)
            print ('Invalid input, please enter only alphabetical information')
            student_last_name = input("Re-enter the student's last name: ")
        
        finally:
            course_name = input("Please enter the name of the course: ")
            student_data = {'first_name':student_first_name,'last_name':student_last_name,'course':course_name}
            students.append(student_data)
            continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course']}")      
            print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student['first_name']},{student['last_name']},{student['course']}\n"
                file.write(csv_data)
            file.close()
        except TypeError as e1:
           print('Wrong File Type')
           print(e1, e1.__doc__,type(e1), sep='\n')
        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course']}") 
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
