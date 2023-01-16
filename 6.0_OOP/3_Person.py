'''3. Создайте класс Person, подкласс Student, у студентов есть средний балл по успеваемости.
Создайте несколько объектов этого класса. Выведите на экран информацию о них с указанием получат
ли они стипендию в следующем семестре (если средний балл >=4)'''
import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, average_score):
        super().__init__(name, age)
        self.average_score = average_score

    def check_scholarship(self):
        if (self.average_score >= 4):
            print(f'Студент {self.name} получит стипендию. Средний бал: {self.average_score}')
        else:
            print(f'Студент {self.name} НЕ получит стипендию. Средний бал: {self.average_score}')


names = ['Алексей', 'Иван', 'Максим', 'Вячеслав', 'Сергей', 'Михаил', 'Антон', 'Пётр']
surnames = ['Иванов', 'Петров', 'Сидоров']
group = []
while group.__len__() < 15:
    student = f"{random.choice(names)} {random.choice(surnames)}"
    age = random.randint(18,35)
    average_score = round(random.uniform(2.0, 5.0), 2)
    group.append(Student(student, age, average_score))

for student in group:
    student.check_scholarship()
