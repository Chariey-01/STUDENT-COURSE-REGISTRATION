# # This is a test file to test the functionality of the school system

# # to test student management in the school system.
# from models.course import Course
# from models.student import Student
# from services.school_system import SchoolSystem

# system = SchoolSystem()

# # Create students FIRST
# student1 = Student("SFDTH17", "Stephanie", 20, "stephie09@gmail.com", "+254756456788")
# system.add_student(student1)

# #  Create courses
# course1 = Course("PY101", "Python Fundamentals", "Mr Joseph", 5)
# course2 = Course("PY220", "Advanced Python", "Mr Titus", 10)

# system.add_course(course1)
# system.add_course(course2)

# #  Debug prints
# for course in system.courses:
#     print(course.course_id, course.course_name)

# #  Now register work only if student + course exist)
# system.register_student_to_course("SFDTH17", "PY101")
# # system.register_student_to_course("SFDTH17", "PY220")

# # # Verify result 
# system.view_students()
# # # to test course management in the school system.
# # from models.course import Course
# # from services.school_system import SchoolSystem

# system = SchoolSystem()

# course1 = Course(
#     "PY101",
#     "Python Fundamentals",
#     "Mr Joseph",
#     5
# )

# course2 = Course(
#     "PY220",
#     "Advanced Python",
#     "Mr Titus",
#     10
# )

# system.add_course(course1)
# system.add_course(course2)

# for course in system.courses:
#     print(course.course_id, course.course_name)

# from services.school_system import SchoolSystem
# from models.student import Student

# system = SchoolSystem() 
# student1 = Student("SFDTH17", 
#                    "Stephanie", 
#                    20,
#                    "stephie09@gmail.com",
#                    "+254756456788")
# student2 = Student(
#     "SFDTH17",
#     "Justine",
#     22,
#     "justine07@gmail.com",
#     "0712345678"
# )
# system.add_student(student1)
# system.add_student(student2)

# system.view_students()

# # // testing for student search
# found = system.search_student("SFDTH18")
# found = system.search_student("stephanie")

# if found:
#     print(found)
# else:
#     print("Student not found")
# print(system.students)=> [<models.student.Student object at 0x7dbe5a014230>]
# print(system.students.student_id)=> AttributeError: 'list' object has no attribute 'student_id'
# for student in system.students:
# #     print(student)
# system.view_students()

# from models.course import Course

# course = Course("COMP131", "Computer Applications", "MR.Biwott", 37)

# print(course.course_id)
# print(course.course_name)
# print(course.trainer_name)
# print(course.capacity)

# from models.student import Student

# student = Student("SFDTH17", 
#                   "Chariey", 
#                   23,
#                   "chariey007@gmail.com",
#                   "0723456786")

# print(student.student_id)
# print(student.name)
# print(student.age)
# print(student.email)
# print(student.phone)