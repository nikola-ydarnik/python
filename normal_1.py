import math

__author__ = 'Тихонов Николай Александрович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print('--------------------задание 1---------------------')

while True:
    number = input('Введите целое положительное число: ')
    if number.isdigit():
        number = list(number)
        break
    else:
        print('Нужно было ввести целое число')

i = 0
maxNumber = 0

while i < len(number):
    number[i] = int(number[i])
    if number[i] > maxNumber:
        maxNumber = number[i]
    else:
        i += 1

print('максимальная цифра в числе: ', maxNumber)

print('--------------------конец задания 1--------------------------')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print('--------------------задание 2------------------------')

while True:
    a = input('Введите число 1:')
    b = input('Введите число 2:')
    if a.isdigit() & b.isdigit():
        a = int(a)
        b = int(b)
        break
    else:
        print('нужно ввести числа')

b = a + b
a = b - a
b = b - a
print('Число 1 стало: ', a)
print('число 2 стало: ', b)

print('--------------------конец задания 2--------------------------')

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('--------------------задание 3------------------------')

a = int(input('Введите коэфицент a: '))
b = int(input('Введите коэфицент b: '))
c = int(input('Введите коэфицент c: '))

d = (b ** 2) - (4 * a * c)
print('Дискриминант: ', d)

if d == 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print('Дискриминант равен нулю. Есть один корень')
    print('Квадратный корень уровнения равен : ', x1)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('Дискриминант больше  нуля. Есть два корня')
    print('Квадратный корень уровнения равен :', x1)
    print('Квадратный корень уровнения равен :', x2)
else:
    print('Дискриминант меньше нуля.')
    print('У этого уравнения не будет квадратного корня')

print('--------------------конец задания 3--------------------------')
