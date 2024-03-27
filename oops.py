"""
Object Oriented Programming
"""

class Student:

    number_of_students = 0
    school = 'Online School'

    def __init__(self,first_name,last_name,major):
        self.first_name=first_name
        self.last_name=last_name
        self.major=major
        
        Student.number_of_students += 1

    def full_name_with_major(self):
        return f'{self.first_name} {self.last_name} is a' \
            f' {self.major} major !'

    @classmethod
    def split_students(cls,student_str):
        first_name,last_name,major=student_str.split('.')
        return cls(first_name,last_name,major)

print(f'Number of Students = {Student.number_of_students}')
student_1=Student('Vipul','Gaur','ECE')
student_2=Student('Kuber','Gaur','Computers')
print(f'Number of Students = {Student.number_of_students}')
new_student = 'Vidhu.Gaur.QuantumOwner'
student_3 = Student.split_students(new_student)


print(student_1.first_name)
print(student_2.first_name)
print(student_3.full_name_with_major())
print(student_1.school)
print(student_1.full_name_with_major())
print(student_2.full_name_with_major())
print(Student.full_name_with_major(student_1))