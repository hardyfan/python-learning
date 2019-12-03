class Student(object):
    __slots__ = ('name', 'age')

class GraduateStudent(Student):
    pass

s = Student()
s.name = 'Michael'
s.age = 25

try:
    s.score = 99
except AttributeError as e:
    print('AttrivuteError:', e)

g = GraduateStudent()
g.score = 99
print('g.score = ', g.score)