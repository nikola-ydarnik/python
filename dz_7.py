import random

# """
# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
# """


class Card:
    def __init__(self, name):
        self.card = self.get_card()
        self.name = name

    def get_card(self):
        lst = [x for x in range(1, 91)]
        card = [[], [], []]
        for n in range(3):
            for i in range(5):
                card[n].append(random.choice(lst))

                for z in lst:
                    if z in card[n]:
                        lst.remove(z)

            for i in range(4):
                card[n].append('  ')
            random.shuffle(card[n])
        return card

    def show_card(self, card):
        print('{}'.format(self.name))
        [print(*x) for x in card]
        print('--------------------------')


class Game:
    def __init__(self, player_card, computer_card):
        self.lst_keg = [x for x in range(1, 91)]
        self.player = player_card
        self.computer = computer_card
        self.user_choice()

    def get_keg(self):
        rand_keg = random.choice(self.lst_keg)
        number = rand_keg
        self.lst_keg.remove(rand_keg)
        return number

    def show_both_cards(self):
        player.show_card(self.player)
        computer.show_card(self.computer)

    def user_choice(self):
        while len(self.lst_keg) > 0:
            keg = self.get_keg()
            if self.winner():
                break
            else:
                print('Новый бочонок: {} (осталось {})'.format(keg, len(self.lst_keg)))
                self.show_both_cards()
                answer = input('Зачеркнуть цифру? (y/n): ')
                if answer == 'y':
                    self.check_cross(keg, self.computer)
                    if self.check_cross(keg, self.player):
                        continue
                    else:
                        print('вы проиграли')
                        break
                elif answer == 'n':
                    self.check_cross(keg, self.computer)
                    if self.check_not_cross(keg, self.player):
                        print('вы проиграли')
                        break
                else:
                    print('\nвы ввели что то не то, попробуйте сначала\n')
                    break

    def check_cross(self, keg, card):
        for line in card:
            if keg in line:
                i = line.index(keg)
                line.insert(i, ' -')
                line.remove(keg)
                return True

    def check_not_cross(self, keg, card):
        for line in card:
            if keg in line:
                return True
            else:
                continue

    def check_card(self, card):
        lst1 = []
        for line in card.copy():
            for elem in line:
                if type(elem) == int:
                    lst1.append(elem)
                else:
                    continue
        if len(lst1) > 0:
            return False
        else:
            return True

    def winner(self):
        players = [self.player, self.computer]
        for user in players:
            if self.check_card(user):
                if user == self.player:
                    print('вы выиграли!!')
                    return True
                else:
                    print('выиграл компьютер!!')
                    return True
            else:
                continue


player = Card('------ Ваша карточка -----')
computer = Card('-- Карточка компьютера ---')
Game(player.card, computer.card)
