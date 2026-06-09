from models.person import Person

class Student:
    def __init__(self, student_id: str, name: str, age: int, email: str, phone: str):
        super().__init__(name, age, email, phone)
        self.student_id = student_id
