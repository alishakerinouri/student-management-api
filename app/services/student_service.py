from typing import List, Optional
from core.entities.student import Student
from core.repositories.student_repository import StudentRepository

class StudentService:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def add_student(self, student: Student) -> Student:
        return self.student_repository.add_student(student)

    def get_students(self) -> List[Student]:
        return self.student_repository.get_students()

    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        return self.student_repository.get_student_by_id(student_id)
