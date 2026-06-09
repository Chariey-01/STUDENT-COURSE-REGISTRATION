from services.data_manager import DataManager

class SchoolSystem:
    # initialize the school system with empty lists for students and courses, and an empty dictionary for registrations thus allowing us to manage students, courses, and their registrations in the school system
    def __init__(self):
      # class attributes to store students, courses, and registrations in memory thus allowing us to manage the data within the system
        self.students = []
        self.courses = []
        self.registrations = {}

# add a method to add students to the system thus allowing us to manage students in the school system
    def add_student(self, student):
        # to check if the student ID already exists in the system thus preventing duplicate entries
      for existing_student in self.students:

        if existing_student.student_id == student.student_id:
            print("Student ID already exists.")
            return
      self.students.append(student)  
      print(f"Student {student.name} added successfully.")

# add a method to view all students in the system thus allowing us to easily see all the students registered in the system
    def view_students(self):
        # handle the case where there are no students in the system(handle empty list thus preventing errors when trying to view students)
        if not self.students:
            print("No students in the system.")
            return
        
        # to check if there are students in the system before trying to view them
        for student in self.students:
            print(student)
            print("-" * 30)

# add a method to search for students by their ID or name thus allowing us to easily find students in the system
    def search_student(self, search_term):
        # to check if there are students in the system before trying to search for them
        for student in self.students:
           if (
            student.student_id == search_term
            or student.name.lower() == search_term.lower()
        ):
            return student

        return None  
          
        # add a method to add courses to the system thus allowing us to manage courses in the school system
    def add_course(self, course):
        # to check if the course ID already exists in the system thus preventing duplicate entries
        for existing_course in self.courses:
            if existing_course.course_id == course.course_id:
                print("Course ID already exists.")
                return
            
            # validate course capacity to ensure it's a positive integer thus preventing invalid course entries
        if course.capacity <= 0:
            print("Course capacity must be a positive integer.")
            return
        self.courses.append(course)
        print(f"Course {course.course_name} by {course.trainer_name} and capacity of {course.capacity} added to the system successfully.")
        
        # to register students for courses in the system thus allowing us to manage course registrations
    def register_student_to_course(self, student_id, course_id):
        student = None

        for s in self.students:
         if s.student_id == student_id:
           student = s
           break

        if student is None:
         print("Student not found.")
         return 
        # find the course by course_id
        course = None

        for c in self.courses:
         if c.course_id == course_id:
          course = c
          break

         if course is None:
          print("Course not found.")
          return
         
        #  check if the student is already registered for the course thus preventing duplicate registrations
        if student_id not in self.registrations:
         self.registrations[student_id] = []
        # prevent duplicate registrations by checking if the student is already registered for the course 
         if course_id in self.registrations[student_id]:
          print(f"{student.name} is already registered for this course.")
         return
        # check if the course has reached its capacity thus preventing overbooking of courses
        if len(self.registrations[student_id]) >= course.capacity:
         print(f"Course {course.course_name} has reached its capacity.Try registering for another course.")
         return
        # register the student for the course by adding the course_id to the student's registration list in the registrations dictionary
        self.registrations[student_id].append(course_id)
        print(f"{student.name} whose ID is {student_id} registered for {course.course_name} successfully.")

   