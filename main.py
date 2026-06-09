from services.school_system import SchoolSystem
from models.student import Student
from models.course import Course

system = SchoolSystem()
while True:
    print("\nStudent Course Registration System Menu:")
    print("1. Add New Student")
    print("2. View Registered Students")
    print("3. Search For Student")
    print("4. Add a New Course")
    print("5. View Available Courses")
    print("6. Register Student to A Course")
    print("0. Exit")

    option = input("Choose an option: ")
    if option == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        email = input("Enter student email: ")
        phone = input("Enter student phone: ")
        student = Student(student_id, name, age, email, phone)
        system.add_student(student)

    elif option == "2":
        system.view_students()

    elif option == "3":
        search_term = input("Enter student ID or name to search: ")
        student = system.search_student(search_term)
        if student:
            print(student)
        else:
            print("Student not found, please try again(check name or ID).")

    elif option == "4":
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        trainer_name = input("Enter trainer name: ")
        capacity = int(input("Enter course capacity: "))
        course = Course(course_id, course_name, trainer_name, capacity)
        system.add_course(course)

    elif option == "5":
        for course in system.courses:
            print(f"Course ID: {course.course_id}, Name: {course.course_name}, Trainer: {course.trainer_name}, Capacity: {course.capacity}")

    elif option == "6":
        student_id = input("Enter student ID to register: ")
        course_id = input("Enter course ID to register for: ")
        system.register_student_to_course(student_id, course_id)

    elif option == "0":
        print("Exiting the system. See you next time!")
        break

    else:
        print("Invalid option,Retry.")
