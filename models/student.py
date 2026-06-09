from models.person import Person

class Student(Person):
    def __init__(self, student_id: str, name: str, age: int, email: str, phone: str):
        super().__init__(name, age, email, phone)
        self.student_id = student_id

    def __str__(self):
        return (
            f"Student Reg.no : {self.student_id}\n"
            f"Student Name :{self.name}\n"
            f"Student Age :{self.age}\n"
            f"Student Email :{self.email}\n"
            f"Student Phone : {self.phone}"
        )
 
    
    