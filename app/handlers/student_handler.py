from fastapi import APIRouter, HTTPException, Depends
from core.entities.student import Student
from app.services.student_service import StudentService
from infrastructure.repositories.in_memory_student_repository 
import InMemoryStudentRepository

router = APIRouter()

def get_student_service():
    repository = InMemoryStudentRepository()
    return StudentService(repository)

@router.post("/students", response_model=Student)
def add_student(student: Student, student_service: StudentService = Depends(get_student_service)):
    return student_service.add_student(student)

@router.get("/students", response_model=List[Student])
def get_students(student_service: StudentService = Depends(get_student_service)):
    return student_service.get_students()

@router.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int, student_service: StudentService = Depends(get_student_service)):
    student = student_service.get_student_by_id(student_id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")
