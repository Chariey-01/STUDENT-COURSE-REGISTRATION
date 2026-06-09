class Course:
    def __init__(self, course_id: str, course_name: str, instructor: str, credits: int, students: list):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.credits = credits
        self.students = students