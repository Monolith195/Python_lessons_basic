#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random


class Card:
    def __init__(self, name):
        self._name = name
        self._card = self._make_card()
        self._count_barrel = 15

    def _make_card(self):
        numbers = random.sample(range(1, 91), 15)
        self._card = [sorted(numbers[i:i + 5]) for i in range(0, 15, 5)]
        for line in self._card:
            for spaces in "    ":
                line.insert(random.randint(0, len(line) - 1), spaces)
        return self._card

    def print_card(self):
        for row in self._card:
            print(' '.join(map(str, row)))

    def find_number(self, number):
        for i in range(len(self._card)):
            for j in range(len(self._card[i])):
                if self._card[i][j] == number:
                    self._card[i][j] = "-"
                    self._count_barrel -= 1
        return self._card

    def get_card(self):
        return self._card

    def get_card_barrel_count(self):
        return self._count_barrel

    def get_name(self):
        return self._name


class Bag:
    def __init__(self):
        self._bag = [i for i in range(1, 91)]

    def pick_barrel(self):
        barrel = random.choice(self._bag)
        self._bag.remove(barrel)
        print("Новый бочонок: {} (осталось {})".format(barrel, len(self._bag)))
        return barrel


class Game:
    def __init__(self, player, comp):
        self.player = player
        self.comp = comp
        self.bag = Bag()
        self._start()

    def _get_current_stats(self):
        print("\n------ Ваша карточка -----")
        self.player.print_card()
        print("--------------------------")
        print("-- Карточка компьютера ---")
        self.comp.print_card()
        print("--------------------------\n")

    def _check_winner(self):
        if self.player.get_card_barrel_count() == 0 and self.comp.get_card_barrel_count() != 0:
            print("Победил {}".format(self.player.get_name()))
        elif self.comp.get_card_barrel_count() == 0 and self.player.get_card_barrel_count() != 0:
            print("Победил {}".format(self.comp.get_name()))
        elif self.player.get_card_barrel_count() == 0 and self.comp.get_card_barrel_count() == 0:
            print("Ничья")

    def _start(self):
        while self.player.get_card_barrel_count() != 0 and self.comp.get_card_barrel_count() != 0:
            current_barrel = self.bag.pick_barrel()
            self._get_current_stats()
            answer = input("Зачеркнуть цифру? (y/n) ")
            while answer not in "yn":
                print("Неизвестная команда")
                answer = input("Зачеркнуть цифру? (y/n) ")
            if answer == "y":
                if any(current_barrel in x for x in self.player.get_card()):
                    self.player.find_number(current_barrel)
                else:
                    print("Вы проиграли. Цифра {} была у вас в карточке".format(current_barrel))
                    break
            elif answer == "n":
                if any(current_barrel in x for x in self.player.get_card()):
                    print("Вы проиграли. Цифра {} была у вас в карточке".format(current_barrel))
                    break
            if any(current_barrel in x for x in self.player.get_card()):
                self.player.find_number(current_barrel)
            if any(current_barrel in x for x in self.comp.get_card()):
                self.comp.find_number(current_barrel)

        self._check_winner()


game = Game(Card("Игрок"), Card("Компьютер"))
