import string
import re
import os
import random

print('---------------------задание 1-----------------------------------------\n')

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

mystr = ''
myline = []
for letter in line:
    if letter in string.ascii_lowercase:
        mystr = mystr + letter
    else:
        if mystr == '':
            continue
        else:
            myline.append(mystr)
            mystr = ''

print('вывод без re:\n', myline)

print('вывод с re: \n', re.findall(r'[a-z]+', line))

print('---------------------задание 2-----------------------------------------\n')

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

str2 = ''
myline2 = []
i = 2
low = string.ascii_lowercase
up = string.ascii_uppercase

while i < len(line2) - 2:
    if line2[i - 2] in low and line2[i - 1] in low and line2[i] in up\
            and line2[i + 1] in up and line2[i + 2] in up:
        str2 = str2 + line2[i]
        i += 1
        while True:
            if line2[i] in up and line2[i + 1] in up and line2[i + 2] in up:
                str2 = str2 + line2[i]
                i += 1
            else:
                myline2.append(str2)
                str2 = ''
                i += 1
                break
    else:
        str2 = ''
        i += 1

print('вывод без re: \n', myline2)

print('вывод с re:\n', re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line2))

print('---------------------задание 3-----------------------------------------\n')
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


# генерирую последовательность чисел
str1 = ''
while len(str1) < 2500:
    str1 = str1 + str(random.randint(0, 9))

# записываю её в файл, не стал писать UTF-8, так как здесь одни цифры
path = os.path.join('test.txt')
with open(path, 'w') as f:
    f.write(str1)

# открываю файл чтобы найти последовательность одинаковых цифр
with open(path, 'r') as f:
    file = f.read()
print('получилась число в файле test.txt:\n', file)

# далее идёт алгоритм по нахождению одинаковых последовательностей цифр

s = ''  # строка для единовременной записи одной последовательности одинаковых цифр
lstNumbers = []  # список в который добавляю все одинаковые последовательности цифр из строки s
n = 1
while n < len(file) - 1:
    if file[n - 1] == file[n]:
        s = s + file[n - 1]
        s = s + file[n]
        n += 1
        if n == len(file):
            lstNumbers.append(s)
            break
        while file[n - 1] == file[n]:
            s = s + file[n]
            n += 1
            if n == len(file):
                lstNumbers.append(s)
                break
        else:
            lstNumbers.append(s)
    else:
        s = ''
        n += 1

# смотрю какая самая длинная последовательность была, так как их может оказаться несколько.
maxSequence = max(lstNumbers, key=len)

# определяю все максимально длинные последовательности одинаковых чисел
sequences = list(filter(lambda x: len(x) == len(maxSequence), lstNumbers))
print('последователльности одинаковых чисел:\n', *sequences)
