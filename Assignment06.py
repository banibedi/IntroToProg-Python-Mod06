# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Bani Bedi,03/10/2024,Created Homework Assignment
# ------------------------------------------------------------------------------------------ #
import json

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
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


class FileProcessor:
    """
    A collection of functions to save and read file data

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file into a list of dictionary rows

        Notes:
        - Data sent to the student_data parameter will be overwritten.

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param file_name: string with the name of the file we are reading
        :param student_data: list of dictionary rows we are adding data to
        :return: list of dictionary rows filled with data
        """
        try:
            file = open(file_name, "r")

            # JSON Answer
            student_data = json.load(file)

            file.close()
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data into a json file from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param file_name: string with the name of the file we are writing
        :param student_data: list of dictionary rows we are saving to file
        """
        try:
            file = open(file_name, "w")

            # # JSON answer
            json.dump(student_data, file)

            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)


class IO:
    """
    A collection of functions for input and ouput

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays an error message

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param message: string of the error message
        :param error: error message to display
        """
        print(error)  # Prints the custom message
        print(message)
        print(error.__doc__)
        print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu message

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param menu: string of the menu message
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function inputs a menu option and chooses different functions depending on input

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function
        """
        menu_choice = input("What would you like to do: ")

        # Input user data
        if menu_choice == "1":  # This will not work if it is an integer!
            IO.input_student_data(students)
            return True

        # Present the current data
        elif menu_choice == "2":
            IO.output_student_courses(students)
            return True

        # Save the data to a file
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
            return True

        # Stop the loop
        elif menu_choice == "4":
            return False  # out of the loop
        else:
            print("Please only choose option 1, 2, or 3")
            return True

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays student courses

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param student_data: list of students to output
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function inputs a new student course

        ChangeLog: (Who, When, What)
        Bani Bedi,3.10.2024,Created function

        :param student_data: list of students to append new student data to
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            sd = {"FirstName": student_first_name,
                  "LastName": student_last_name,
                  "CourseName": course_name}
            student_data.append(sd)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("-- Technical Error Message -- ", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(FILE_NAME, students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(MENU)
    if IO.input_menu_choice() == False:
        break

print("Program Ended")
