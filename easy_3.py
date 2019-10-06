print('---------------------задание 1-----------------------------------------\n')
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    a = int(number * (10 ** ndigits))
    int(number * 10 ** (ndigits + 1) / 10)
    return (a + 1) / (10 ** ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

print('\n---------------------задание 2-----------------------------------------\n')

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(x):
    x = str(x)
    first_number, second_number = int(x[0]), int(x[1])
    last_number, penult_number = int(x[-1]), int(x[-2])
    if (first_number + second_number) == (last_number + penult_number):
        return 'вам попался счастливый билет'
    else:
        return 'вам не повезло'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
