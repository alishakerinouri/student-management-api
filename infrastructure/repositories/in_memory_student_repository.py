from typing import List, Optional
from core.entities.student import Student
from core.repositories.student_repository import StudentRepository

class InMemoryStudentRepository(StudentRepository):
    def __init__(self):
        self.students = []

    def add_student(self, student: Student) -> Student:
        self.students.append(student)
        return student

    def get_students(self) -> List[Student]:
        return self.students

    def get_student_by_id(self, student_id: int) -> 
Optional[Student]:
        for student in self.students:
            if student.id == student_id:
                return student
        return None
