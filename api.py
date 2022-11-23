from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "Paul",
        "age": "17",
        "class": "Year 2",
    },

    2: {
        "name": "Paul",
        "age": "17",
        "class": "Year 12",
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: int


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None


@app.get("/")
def index():
    return {"name": "First Data"}

# Use a path parameter to get the student by ID


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student that you want to get")):
    return students[student_id]

# Use a query parameter to get the student by name
# A feature that combines query parameter and search parameter


@app.get("/get-by-name{student_id}")
def get_student(name: str, student_id: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return{"Data not found"}


# add a new student using an ID
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Student already exists"}
    students[student_id] = student
    return students[student_id]


# update a student
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return{"Error  Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    # students[student_id] = student    
    return students[student_id]
