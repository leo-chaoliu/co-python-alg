class Person:
    def __init__(self, nameParam, surnameParam, numberParam, idParam):
        self.name = nameParam
        self.surname = surnameParam
        self.number = numberParam
        self.id = idParam
    
    def __gt__(self, other):
        if self.number == other.number:
            return self.id > other.id

        return self.number > other.number

    def __str__(self):
        return self.name + self.surname + self.number

p1 = Person('leo', 'liu', '1', '9')
p2 = Person('a', 'ab', '1', '4')

print(p1>p2)
print(p2)
