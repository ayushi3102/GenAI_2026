from fastapi import FastAPI,Query,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name:str
    age:int
    roll_no:int
    

students = []
current_id = 0

@app.post('/students',status_code = 201)
def create_student(student:Student):
    global current_id
    current_id+=1
    new_student = {
        'id':current_id,
        'name':student.name,
        'age':student.age,
        'roll_no':student.roll_no
    }
    students.append(new_student)
    return {'message':'student created successfully','id':new_student['id']}

@app.get('/students')
def get_students():
    return {'students':students}

@app.get('/students/{id}')
def get_students(id:int):
    for s in students:
        if s['id']==id:
            return {'student':s}
    raise  HTTPException(status_code = 404, detail = 'Student not found')
    

@app.put('/students/{id}')
def get_students(id:int,student:Student):
    for s in students:
        if s['id']==id:
            s['name'] = student.name
            s['age'] = student.age
            s['roll_no'] = student.roll_no
            return {'message':'User updated'}
    raise HTTPException(status_code = 404, detail = 'Student not found')

@app.delete('/students/{id}')
def delete_students(id:int):
    ls =[]
    found=0
    for i,s in enumerate(students):
        deleted  = students.pop(i)
        return {'message':'User deleted'}
    raise HTTPException(status_code = 404, detail = 'student not found')
    