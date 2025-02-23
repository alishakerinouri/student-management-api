from typing import List, Optional
from core.entities.student import Student

class StudentRepository:
    def add_student(self, student: Student) -> Student:
        raise NotImplementedError

    def get_students(self) -> List[Student]:
        raise NotImplementedError

    def get_student_by_id(self, student_id: int) -> 
Optional[Student]:
        raise NotImplementedError
