import math

print('---------------------задание 1-------------------------------------------------------\n')

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        point1, point2, point3 = (x1, y1), (x2, y2), (x3, y3)
        lst = sorted([point1, point2, point3])  # отсортируем чтобы точки встали по порядку
        self.a = lst[0]  # распределяем отсортированные координаты по точкам a b c
        self.b = lst[1]
        self.c = lst[2]

    def area(self):
        return math.fabs(((self.b[0] - self.a[0]) * (self.c[1] - self.a[1]) -     # [0] это x, [1] это y
                       (self.c[0] - self.a[0]) * (self.b[1] - self.a[1]))) / 2

    def __ab(self):
        return math.sqrt(((self.b[0] - self.a[0]) ** 2) + ((self.b[1] - self.a[1]) ** 2))  # [0] это x, [1] это y

    def __bc(self):
        return math.sqrt(((self.c[0] - self.b[0]) ** 2) + ((self.c[1] - self.b[1]) ** 2))

    def __ac(self):
        return math.sqrt(((self.c[0] - self.a[0]) ** 2) + ((self.c[1] - self.a[1]) ** 2))

    def perimetr(self):
        return round(self.__ab() + self.__bc() + self.__ac(), 2)

    def heigth(self):
        return round(2 * self.area() / self.__check_heigth(), 2)

    def __check_heigth(self):
        answer = input(' какую сторону (ab, bc или ac) нужно считать основанием,\n для определения высоты: ')
        if answer == 'ab':
            return self.__ab()
        elif answer == 'bc':
            return self.__bc()
        elif answer == 'ac':
            return self.__ac()


triangle = Triangle(0, 0, 1, 1, 2, 1)
print('периметр треугольника: ', triangle.perimetr())
print('площадь треугольника: ', triangle.area())
print('высота треугольника: ', triangle.heigth())

print('---------------------задание 2---------------------------------------------------\n')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        lst = sorted([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
        self.a, self.b, self.c, self.d = lst[0], lst[1], lst[2], lst[3]

    def side(self, point1, point2):
        return math.sqrt(math.fabs((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2))

    def ab(self):
        return self.side(self.a, self.b)

    def bc(self):
        return self.side(self.b, self.c)

    def cd(self):
        return self.side(self.c, self.d)

    def da(self):
        return self.side(self.d, self.a)

    def __diagonal_ac(self, a, b, c, d):
        return math.sqrt(math.fabs((d ** 2 + a * b) - ((a * (d ** 2 - c ** 2)) / (a - b))))

    def __diagonal_bd(self, a, b, c, d):
        return math.sqrt(math.fabs((c ** 2 + a * b) - ((a * (c ** 2 - d ** 2)) / (a - b))))

    def check_trapezoid(self):
        if self.__diagonal_ac(self.da(), self.bc(), self.ab(), self.cd())\
                == self.__diagonal_bd(self.da(), self.bc(), self.ab(), self.cd()):
            return 'это равнобедренная трапеция'
        else:
            return 'это не равнобедренная трапеция'

    def perimetr(self):
        return self.ab() + self.bc() + self.cd() + self.da()

    def area(self):
        a, b, c, d = self.da(), self.bc(), self.ab(), self.cd()
        return ((a + b) / 2) * math.sqrt(math.fabs(c ** 2 - ((((a - b) ** 2 + c ** 2 - d ** 2) / (2 * (a - b))) ** 2)))


trapez = Trapezoid(-6, 0, 6, 0, 2, 2, -2, 2)
print(trapez.check_trapezoid())
print('длины сторон трапеции: {}, {}, {}, {}'.format(round(trapez.ab(), 2), round(trapez.bc(), 2),
                                                     round(trapez.cd(), 2), round(trapez.da(), 2)))
print('периметр трапеции равен: ', round(trapez.perimetr(), 2))
print('площадь трапеции: ', round(trapez.area(), 2))
