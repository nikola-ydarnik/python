# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, surname, name, father_name):
        self.name = name
        self.surname = surname
        self.father_name = father_name

    def get_full_name(self):
        return '{} {}. {}.'.format(self.surname, self.name[0], self.father_name[0])


class Student(Person):
    def __init__(self, surname, name, father_name, parent1, parent2, grade):
        Person.__init__(self, surname, name, father_name)
        self.parent1 = parent1
        self.parent2 = parent2
        self.grade = grade

    def get_class_room(self):
        return self.grade

    def get_parents(self):
        return self.parent1.get_full_name(), self.parent2.get_full_name()


class Teacher(Person):
    def __init__(self, surname, name, father_name, subject, grades):
        Person.__init__(self, surname, name, father_name)
        self.subject = subject
        self.grades = grades

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.grades


class_number = ['5А', '6Б', '7В']

parents = [Person('Иванова', 'Елена', 'Николаевна'),
           Person('Иванов', 'Иван', 'Алексеевич'),
           Person('Петров', 'Пётр', 'Фёдорович'),
           Person('Петрова', 'Александра', 'Владимировна'),
           Person('Сидоров', 'Василий', 'Александрович'),
           Person('Сидорова', 'Марина', 'Петровна'),
           ]

students = [Student('Иванов', 'Иван', 'Иванович', parents[0], parents[1], class_number[0]),
            Student('Петров', 'Петр', 'Петрович', parents[2], parents[3], class_number[1]),
            Student('Сидоров', 'Василий', 'Васильевич', parents[4], parents[5], class_number[2]),
            ]

teachers = [Teacher('Курашов', 'Анатолий', 'Васильевич', 'математика', class_number),
            Teacher('Барков', 'Валерий', 'Михайлович', 'русский', [class_number[0], class_number[2]]),
            Teacher('Снегирев', 'Валентин', 'Михайлович', 'рисование', [class_number[1], class_number[2]]),
            ]

print('список классов в школе: ')
for grade in class_number:
    print(grade)

for grade in class_number:
    print('Ученики в классе: ', grade)
    for student in students:
        if student.get_class_room() == grade:
            print(student.get_full_name())

for student in students:
    print('предметы ученика: ', student.get_full_name())
    print([x.subject for x in [teacher for teacher in teachers if student.get_class_room() in teacher.get_classes()]])

for student in students:
    print('4. Родители учеников :', student.get_full_name())
    print(student.get_parents())

for grade in class_number:
    print('5. Учителя, преподающие в классе:', grade)
    print([teacher.get_full_name() for teacher in teachers if grade in teacher.get_classes()])
