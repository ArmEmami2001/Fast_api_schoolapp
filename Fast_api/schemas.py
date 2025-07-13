from pydantic import BaseModel
from typing import List, Optional

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    courses: List[Course] = []

    class Config:
        orm_mode = True