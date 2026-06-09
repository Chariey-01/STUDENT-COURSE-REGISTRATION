import json
import os

class DataManager:
    def __init__(self):
        self.student_file = "data/students.json"
        self.course_file = "data/courses.json"
        self.registration_file = "data/registrations.json"  

    def load_data(self, file_path):
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r") as file:
            return json.load(file)  

          #  save students
    def save_students(self, students):
      data = []

      for student in students:
          data.append({
              "student_id": student.student_id,
              "name": student.name,
              "age": student.age,
              "email": student.email,
              "phone": student.phone
          })
      with open(self.student_file, "w") as file:
          json.dump(data, file, indent=4)

          #load students
    def load_students(self):
        return self.load_data(self.student_file)
          # save courses
    def save_courses(self, courses):
        data = []
        for course in courses:
            data.append({
                "course_id": course.course_id,
                "course_name": course.course_name,
                "trainer_name": course.trainer_name,
                "capacity": course.capacity
            })
        with open(self.course_file, "w") as file:
            json.dump(data, file, indent=4)

          # load courses
    def load_courses(self):
        return self.load_data(self.course_file)

          # save registrations
    def save_registrations(self, registrations):
        with open(self.registration_file, "w") as file:
            json.dump(registrations, file, indent=4)

          # load registrations
    def load_registrations(self):
        return self.load_data(self.registration_file)