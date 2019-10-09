import os
import sys
import shutil

print('---------------------задание 1-------------------------------------------------------\n')

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


if __name__ == '__main__':

    for i in range(1, 10):
        name_dir = "dir_" + str(i)
        new_dir = os.path.join(os.getcwd(), name_dir)
        try:
            os.mkdir(new_dir)
            print('создана директория: ', name_dir)
        except FileExistsError:
            print('директория ', name_dir, ' уже существует')

    for i in range(1, 10):
        name_dir = "dir_" + str(i)
        remove_dir = os.path.join(os.getcwd(), name_dir)
        try:
            os.rmdir(remove_dir)
            print('удалена директория: ', name_dir)
        except FileNotFoundError:
            print('директория ', name_dir, ' не существует')

    print('---------------------задание 2---------------------------------------------------\n')

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

    folders = []
    files_in_cwd = os.listdir(os.getcwd())
    for i, file in enumerate(files_in_cwd):
        if os.path.isdir(file):
            folders.append(file)

    print('вот все папки в текущей директории: ', *folders, sep='\n')

    print('---------------------задание 3----------------------------------------------------\n')

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    file_name = sys.argv[0]
    file_name_new = file_name[:file_name.rfind('.')] + '(copy)' + file_name[file_name.rfind('.'):]
    if not os.path.isfile(file_name_new):
        shutil.copy(file_name, file_name_new)
        print('файл скопирован')
    else:
        print('этот файл уже скопирован')

# ----------------------------------------------------------------------------------------------------------------------
# --------------------дальше написал функции для импортирования в задание Normal----------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
else:

    def show_folders():  # покажет какие папки есть в директории
        folders = []
        files_in_cwd = os.listdir(os.getcwd())
        for i, file in enumerate(files_in_cwd):
            if os.path.isdir(file):
                folders.append(file)
        print('вот все папки в текущей директории: ', *folders, sep='\n')


    def change_dir():
        show_folders()  # покажу папки, чтобы пользователю было удобнее выбрать какую нибудь из них
        print('\nмы находимся здесь:\n', os.getcwd())
        user_dir = input('Введите название папки, в которую хотите перейти: \n')
        try:
            os.chdir(user_dir)
            print("теперь находимся здесь:", os.getcwd())
            return True
        except FileNotFoundError:
            return False


    def cwd_content():
        files = os.listdir(os.getcwd())
        print('\nвот содержимое папки: ', *files, sep='\n ')


    def remove_folder():
        show_folders()  # покажу папки, чтобы пользователю было удобнее выбрать какую нибудь из них
        folder_remove = input('\nКакую папку вы хотите удалить: ')
        new_path = os.path.join(os.getcwd(), folder_remove)
        try:
            os.rmdir(new_path)
            return True
        except FileNotFoundError:
            return False


    def create_folder():
        folder_new = input('\nпапку с каким названием вы хотите создать: ')
        new_path = os.path.join(os.getcwd(), folder_new)
        try:
            os.mkdir(new_path)
            return True
        except FileExistsError:
            return False
