# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

# всё что смог, первый вариант
matrix_rotate = [(print('matrix_rotate = '), [print('  ', line) for line in list(map(list, zip(*matrix)))])]

# второй вариант
matrix_rotate1 = [line for line in list(map(list, zip(*matrix)))]
print('\n{} {}'.format('matrix_rotate = ', matrix_rotate1))


