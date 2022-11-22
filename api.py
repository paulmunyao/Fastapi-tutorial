from fastapi import FastAPI

app = FastAPI()

students = {
    1:{
        "name":"Paul",
        "age":"17",
        "class":"Year 12",
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return students[student_id]

