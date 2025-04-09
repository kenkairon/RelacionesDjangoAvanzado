from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name="courses")
    
course = Course.objects.get(id=1)

# Consultar todos los estudiantes de un curso
students = course.students.all()

for student in students:
    print(student.name)
    
student = Student.objects.get(id=1)

# Consultar todos los cursos de un estudiante
courses = student.courses.all()

for course in courses:
    print(course.name)
    
# Supongamos que tienes un estudiante con ID 1 y un curso con ID 2
course = Course.objects.get(id=1)
student = Student.objects.get(id=2)

# Agregar un estudiante a un curso
course.students.add(student)

course = Course.objects.get(id=1)
student = Student.objects.get(id=2)

# Eliminar un estudiante de un curso
course.students.remove(student)

course = Course.objects.get(id=1)

# Eliminar todos los estudiantes de un curso
course.students.clear()


course = Course.objects.get(id=1)
student1 = Student.objects.get(id=2)
student2 = Student.objects.get(id=3)

# Agregar múltiples estudiantes a un curso
course.students.add(student1, student2)

# O bien, utilizando IDs
course.students.add(2, 3)  # Usando los IDs de los estudiantes