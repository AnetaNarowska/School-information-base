
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def introduce(self):
        print(f'My name is {self.name} {self.surname}')

class Student(Person):
    def __init__(self,name,surname,grades):
        super().__init__(name,surname)
        self.grades=grades

    def grade_average(self):
        #return sum(self.grades)/len(self.grades)
        suma=0
        for i in self.grades:
            suma+=i
        return suma/len(self.grades)

    def distinction(self):
        #return self.grade_average()>4.75
        if self.grade_average()>4.75:
           return True
        else:
           return False
    def introduce(self):
        super().introduce()
        print(self.grades)

s1=Student("Aneta","Nowacka",[4,2,6])

s2=Student('Rafał',"Nowacki",[5,5,6])

class_of_students=[s1,s2]

s1.introduce()
print(f'This is my grade point average: {s1.grade_average()}')
print(f'Distinction: {s1.distinction()}')


class Teacher(Person):
    def __init__(self, name, surname, students_list):
        super().__init__(name, surname)
        self.students_list = students_list
    def introduce(self):
        print(f'I\'m a teacher. My name is {self.name} {self.surname}')    
    def list(self):
             print(f'My class of students: {self.students_list}')

teacher1=Teacher('Magdalena','Kowalska', [f'{s1.name}',f'{s2.name}'])

teacher1.introduce()
teacher1.list()





