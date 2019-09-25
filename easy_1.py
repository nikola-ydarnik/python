
__author__ = 'Тихонов Николай Александрович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
# код пишем тут...

print('--------------------задание 1------------------------')

while True:
    number = input('Введите целое число: ')
    if number.isdigit():
        break
    else:
        print('Нужно было ввести целое число')

for n in number:
    print(n)

print('--------------------конец задания 1--------------------------')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

print('--------------------задание 2------------------------')

# так как НЕ написанно что нужны только числа, провекрку на числа не стал делать здесь

a = input('Введите значение 1ой переменной: ')
b = input('Введите значение 2ой переменной: ')
c = a
a = b
b = c
print('1ое значение стало', a)
print('2ое значение стало', b)

print('--------------------конец задания 2--------------------------')

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print('--------------------задание 3------------------------')

while True:
    age = input('Введите возраст')
    if age.isdigit():
        age = int(age)
        break
    else:
        print('нужно было ввести число')

if age >= 18:
    print('Доступ разрешён')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

print('--------------------конец задания 3--------------------------')
