from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Paul",
        "age": "17",
        "class": "Year 12",
    }
}

class Student(BaseModel):
    name:str
    age:int
    year:int

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
def create_student(student_id : int, student:Student):
    if student_id in students:
        return {"Student already exists"}
    students[student_id] = student
    return students[student_id]
