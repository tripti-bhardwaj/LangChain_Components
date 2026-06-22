from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Anonymous"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt = 0, lt = 10, default = 5, description = "A decimal value representing the CGPA of the student.")

new_student = {"name": "Tripti", "age": 23, "email": "tripti@gmail.com", "cgpa": "9.08"}

student = Student(**new_student)

# print(student)
# print(type(student))

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()