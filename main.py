class Person:
    def __init__(self, my_name, my_age):
        self.name = my_name
        self.age = my_age

    def det_details(self):
        print(f"Name: {self.name} , Age: {self.age}")


class Student(Person):
    def __init__(self, my_name, my_age, my_roll_num):
        super().__init__(my_name, my_age)
        self.roll_num = my_roll_num
        self.course = []

    def registered_for_course(self, course):
        self.course.append(course)

class Instructor(Person):
    def __init__(self, my_name, my_age, my_emp_id, my_salary):
        super().__init__(my_name, my_age)
        self.emp_id = my_emp_id
        self.salary = my_salary
        self.course = []

    def assign_course(self, course):
        self.course.append(course)


class Course:
    def __init__(
        self,
        c_id,
        c_name,
    ):
        self.id = c_id
        self.name = c_name
        self.students = []
        self.instructors = []

    def add_student(self, student):
        self.students.append(student)

    def set_instructor(self, instructor):
        self.instructors.append(instructor)


class Department:
    def __init__(self, d_name):
        self.name = d_name
        self.course = []

    def add_course(self, course):
        self.course.append(course)


c1 = Course(101, "Python")
c2 = Course(102, "Java")
d1 = Department("Computer Science")
d1.add_course(c1.name)
d1.add_course(c2.name)
# --------------- Student  1 -----------------
s1 = Student("Sadaf", 22, "giaic121")
s1.registered_for_course(c1.name)
c1.add_student(s1.name)
i1 = Instructor("Ali", 30, "emp-101", 50000)
c1.set_instructor(i1.name)
# --------------- Student  2 -----------------
s2 = Student("Aleena", 23, "giaic122")
i2 = Instructor("Sir Hamzah", 23, "emp-102", 70000)
s2.registered_for_course(c2.name)
c2.add_student(s2.name)
c2.set_instructor(i2.name)
# --------------- Displaying Details -----------------
print(f"Department 1 : {d1.__dict__}")
print(f"Course 1: {c1.__dict__} ")
print(f"Course 2: {c2.__dict__} ")
print(f"Student 1: {s1.__dict__} ")
print(f"Student 2: {s2.__dict__} ")
