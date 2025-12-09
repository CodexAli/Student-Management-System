from sqladmin import Admin, ModelView
from database import Student, engine
from main import app

admin = Admin(app, engine)

class StudentAdmin(ModelView, model=Student):
    column_list = [
        Student.id,
        Student.name,
        Student.age,
        Student.department,
        Student.semester,
        Student.email
    ]

admin.add_view(StudentAdmin)
