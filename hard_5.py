import os
import sys
import shutil

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

print('sys.argv = ', sys.argv)


def print_help():
    print('\n')
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print('cp <file_name> - создает копию указанного файла')
    print("rm <file_name> - удаляет указанный файл")
    print('\n')


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def change_dir():
    try:
        os.chdir(dir_name)
        print('теперь вы находитесь здесь\n', os.getcwd())
    except FileNotFoundError:
        print('Вы ввели что то не так')


def show_cwd():
    print('\nтекущая директория: ', os.getcwd(), '\n')


def copy_file():
    try:
        os.path.isfile(dir_name)
        file_name_new = dir_name[:dir_name.rfind('.')] + '(copy)' + dir_name[dir_name.rfind('.'):]
        shutil.copy(dir_name, file_name_new)
        print('файл скопирован\n')
    except FileNotFoundError:
        print('нет такого файла, копирует только файлы, не папки\n')


def remove_file():
    try:
        os.path.isfile(dir_name)
        os.remove(dir_name)
        print('файл удалён')
    except FileNotFoundError:
        print('нет такого файла, удаляет только файлы, а не папки')


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cd": change_dir,
    "ls": show_cwd,
    "cp": copy_file,
    "rm": remove_file,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
