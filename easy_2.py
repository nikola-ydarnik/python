print('---------------------задание 1-----------------------------------------\n')

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

listProducts = ['яблоко', 'груша', 'молоко', 'макароны', 'конфеты']

count = 0
for product in listProducts:
    count += 1
    print('{}. {:>10}'.format(count, product))

print('\n---------------------задание 2-----------------------------------------\n')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = [1, 2, 3, 'яблоко', 'груша', 'молоко', 'макароны', 'конфеты']
list2 = [1, 3, 'яблоко', 'банан', 'киви', 'молоко', 'арбуз']

print('список 1 был: ', list1)
print('список 2: ', list2)

for i in list2:
    while list1.count(i) != 0:
        list1.remove(i)

print('список 1 стал: ', list1)

print('\n//также написал ЕЩЁ ОДНО решение, оно закоментировано.')
print(' не понимаю почему n1 перескакивает элементы списка? ')

# for n1 in list1:
#     for n2 in list2:
#         if n1 == n2:
#             list1.remove(n1)
#             break

print('\n---------------------задание 3-----------------------------------------\n')

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

listNumbers = [1, 2, 3, 4, 5, 6, 7, 8]
listNumbersNew = []

print('был дан список: ', listNumbers)

for i in listNumbers:
    if (i % 2) == 0:
        i /= 4
        listNumbersNew.append(i)
    else:
        i *= 2
        listNumbersNew.append(i)

print('получился список: ', listNumbersNew)
