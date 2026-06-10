# Student Course Registration System

## Overview
A Python command-line application that manages students, courses, and registrations using OOP.

---

## Features
- Add New students
- View Registered students
- Search for students
- Add new courses
- View  Available courses
- Register students to courses
- Prevent duplicate registrations
- Enforce course capacity
- Save and load data using JSON files

---

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- JSON File Handling

---

## Project Structure
student-course-registration/
student-course-registration/
│
├── main.py
├── models/
│   ├── person.py
│   ├── student.py
│   └── course.py
│
├── services/
│   └── school_system.py
│
├── data/
│   ├── students.json
│   ├── courses.json
│   └── registrations.json
│
└── README.md

---

##  How to Run testfile and the main menu
```bash
python3 main.py

---

```bash
python3 test_file.py

How It Works
Students and courses are stored as objects
Registrations are stored using a dictionary mapping student IDs to course IDs
Data is saved in JSON files for persistence
Learning Outcomes
Object-Oriented Programming
Inheritance
System design
File handling
Data validation

Author
      CHARITY JEPKOECH
