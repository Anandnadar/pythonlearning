
#  Real-world scenario:

# You are developing a student management application. You need to create student objects and display their details.
# Requirements
# 1. Create a class called Student.
# 2. Create a method called get_details().
# 3. Store the following properties:
#    - Student name
#    - Student age
#    - Student course
# 4. Create three student objects.
# 5. Display each student's details.


# class student:
#   def __init__(self, name,age,course):
#     self.name = name
#     self.age = age
#     self.course = course
    
#   def get_details(self):
#       print(f"student: {self.name} ,age:{self.age}")
      

    

# student_data = student("Anand", 25, "Python")
# student_data2 = student("raja", 25, "Python")
# student_data2.get_details()

# Polymorphis
# class PythonStudent:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_details(self):
#         print(f"{self.name} is learning {self.course}")


# class JavaStudent:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_details(self):
#         print(f"{self.name} is learning {self.course}")

# class sqlStudent:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_details(self):
#         print(f"{self.name} is learning {self.course}")


# student1 = PythonStudent("Anand", 25, "Python")
# student2 = JavaStudent("Raja", 26, "Java")
# student3 = sqlStudent("Vinod", 26, "SQL")

# student1.get_details()
# student2.get_details()
# student3.get_details()


# inhertiance ana polymrisph
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


class PythonStudent(Student):
    def get_details(self):
        print(f"studentName {self.name} age{self.age} studentcourse:{self.course} ")


class JavaStudent(Student):
    def get_details(self):
        print(f"studentName {self.name} age{self.age} studentcourse:{self.course} ")


class SQLStudent(Student):
    def get_details(self):
        print(f"studentName {self.name} age{self.age} studentcourse:{self.course} ")


student1 = PythonStudent("Anand", 25, "Python")
student2 = JavaStudent("Raja", 26, "Java")
student3 = SQLStudent("Vinod", 27, "SQL")

student1.get_details()
student2.get_details()
student3.get_details()