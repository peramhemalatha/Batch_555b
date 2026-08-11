from fastapi import FastAPI
from pydantic import BaseModel

app = FasttAPI(title="Student Details Management API")

#in memory database
students_db={
    1:{"name":"hemalatha","age":20,"course":"Data Analyst"},
    2:{"name":"manju","age":21,"course":"Data Science"},
    3:{"name":"mokshitha","age":22,"course":"AI&ML"},
}

#Data validation model
class Student(BaseModel):
    name: str
    age: int
    course: str


==========================================
READ (GET) - View All or Filter by Course
==========================================
@app.get("/students/")
def get_students(course: str = None):
    if course:
        filtered = {
            s_id: s
            for s_id, s in students_db.items()
            if s["course"].lower() == course.lower()
        }
        return filtered

    return students_db
