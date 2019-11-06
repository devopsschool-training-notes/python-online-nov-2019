"""
# 2 class object instance is at 2 diff location of memory
class Student:
    pass
student = Student()

print (student)

new_student = Student()

print (new_student)
"""
# EVOLUTION
"""
students = []
class Student:
 def add_student(self, name, student_id=332):
  student = {"name": name, "student_id": student_id}
  students.append(student)

student = Student()
student.add_student("Mark")
print (students)
"""
# Construtors and Special Methos
# EVOLUTION - Construtors method would be automatically get called when you instantiate a class in backgroup
# We can customize a class instantiate behaviour by modifying Construtors method.

"""
students = []
class Student:
 def __init__(self, name, student_id=332):
  student = {"name": name, "student_id": student_id}
  students.append(student)

mark = Student("Mark")
print (students)

# How to fix this?
print (mark)
"""
# Construtors and Special Methos
# EVOLUTION - 
"""
students = []
class Student:
 def __init__(self, name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

 def __str__(self):
    return "Student"

mark = Student("Mark")
print (students)
print (mark)
"""

# EVOLUTION - Instance and Class Attributes
# Instance Attribute This one.
students = []
class Student:
 school_name = "DevOps School"
 def __init__(self, name, student_id=332):
    self.name = name
    self.student_id = student_id
    students.append(self)

 def __str__(self):
    return "Student"

 def get_name_capitaize(self):
    return self.name.get_name_capitaize()

 def get_school_name(self):
    return self.school_name

mark = Student("Mark")
print (students)
print (mark)
print(Student.school_name)
 