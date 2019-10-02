print('---------------------задание 1-----------------------------------------\n')

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

y = float(equation[equation.index('=') + 2:equation.index('x')]) * x + float(equation[equation.index('+') + 2:])
print('координата y: ', y)

print('\n---------------------задание 2-----------------------------------------\n')

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.34.1985'


def check_format():
    if len(day) == 2 and len(month) == 2 and len(year) == 4:
        check_int_date()
        return True
    else:
        print('Вы не соблюдаете формат dd.mm.yyyy. Должно быть:')
        print('2 символа для дня, 2 - для месяца, 4 - для года')
        return False


def check_int_date():
    for number in date_lst:
        if number.isdigit():
            pass
        else:
            print('Нужно было ввести целые числа')


def check_date():
    if month in daysOfMonths:
        if 1 <= int(day) <= daysOfMonths[month]:
            if 1 <= int(year) <= 9999:
                print('Дата введена верно')
                return True
            else:
                print('год нужно вводить в диапазоне от 1 до 9999')
        else:
            print('день нужно вводить в диапазоне от 1 до 30 или 31, в зависимости от месяца')
    else:
        print('месяц нужно вводить в диапазоне от 1 до 12')


daysOfMonths = {
                '01': 31, '02': 30, '03': 31, '04': 30, '05': 31, '06': 30,
                '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31,
                }

while True:
    print('введите дату в формате dd.mm.yyyy')
    date = input('ОБЯЗАТЕЛЬНО ставить точки между dd mm yyyy: ')
    date_lst = date.split('.')
    day = date_lst[0]
    month = date_lst[1]
    year = date_lst[2]
    if check_format() and check_date():
        break

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

print('\n---------------------задание 3-----------------------------------------\n')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


def check_int_of_room():
    if roomNumber.isdigit():
        if 1 <= int(roomNumber) <= 2000000000:
            return True
        else:
            print('нужно было ввести число в диапазоне от 1 до 2000000000')
    else:
        print('нужно было ввести целое положительное число')


def floor_create():
    n = 1
    while n <= roomNumber:
        for i in range(n):
            floor.append(n)
        n += 1


def room_create_and_compare():
    rooms = []
    k = 1
    for i in range(len(floor)):
        for j in range(1, floor[i] + 1):
            rooms.append(k)
            k += 1

        if roomNumber in rooms:
            print('комната находится на:', i + 1, 'этаже', rooms.index(roomNumber) + 1, 'слева')
            break
        else:
            rooms = []


floor = []
print('программа определит на каком этаже находится ваша комната')
while True:
    roomNumber = input('Введите номер комнаты от 1 до 2000000000: ')
    if check_int_of_room():
        roomNumber = int(roomNumber)
        break

floor_create()
room_create_and_compare()

print('\n------------------------------------------------------------------------\n')
print('к сожалению задание 3 работает очень медленно, но ничего лучше сделать не получилось, ')
print('решение подсматривал, единственное, которое понял, было бы хорошо, ')
print('если бы вы объяснили математическое решение, я его приложил закоментированным ниже:')

# room = int(input('Введите номер комнаты: '))
# n = room
# roomsBefore = 0
# bloc = 0
# while n > 0:
#     bloc += 1
#     n = n - bloc**2
#     roomsBefore = roomsBefore + bloc**2
# roomsBefore = roomsBefore - bloc**2
#
# # определим номер этажа в блоке
# numberInBloc = room - roomsBefore
# floorInBloc = 1
# while numberInBloc > bloc:
#     floorInBloc += 1
#     numberInBloc = numberInBloc - bloc
#
# # определим номер этажа в башне
# floorInTower = 0
# while bloc > 0:
#     floorInTower = floorInTower + (bloc - 1)
#     bloc -= 1
# floor = floorInTower + floorInBloc
# print('Этаж: ', floor)
# print('Номер комнаты слева на право: ', numberInBloc)
