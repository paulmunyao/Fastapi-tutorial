from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "Paul",
        "age": "17",
        "class": "Year 12",
    }
}


@app.get("/")
def index():
    return {"name": "First Data"}

#Use a path parameter to get the student by ID
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student that you want to get")):
    return students[student_id]

#Use a query parameter to get the student by name
@app.get("/get-by-name")
def get_student(name:str):
    for student_id in students:
        if students[student_id]["name"] ==name:
            return students[student_id]
    return{"Data not found"}        