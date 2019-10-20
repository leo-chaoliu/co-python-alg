# abstract
from abc import ABC

class Person(ABC):
    def __init__(self, nameParam):
        self.name = nameParam
    
    def __str__(self):
        return self.name

class Student(Person):
    def __init__(self, nameParam, studentNumber):
        super().__init__(nameParam)
        # self.name = nameParam
        self.studentNumber = studentNumber

    def __str__(self):
        return self.name + ' ' + self.studentNumber    

class Professor(Person):
    def __init__(self, nameParam, classes):
        super().__init__(nameParam)
        self.classes = classes

    def __str__(self):
        classes = ''
        for class_ in self.classes:
            classes += class_
            pass
        
        return self.name + ' ' + classes
pp1 = Person('PP')
s1 = Student('leo', '001')
p1 = Professor('Molly', ['CS DSA', 'CS dsdd'])

print(type(ABC))
print(type(pp1))
print(type(s1))
print(p1)

