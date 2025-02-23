from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int
    average: float
