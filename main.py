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
