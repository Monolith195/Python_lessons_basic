# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

import os
import pickle

player_name = input("Введите имя игрока ")
enemy_name = input("Введите имя противника ")
player = {"health": 100, "damage": 5, "name": player_name, "armor": 1.2}
enemy = {"health": 100, "damage": 4, "name": enemy_name, "armor": 1.2}


def attack(person1, person2):
    person2["health"] = person2["health"] - final_damage(person1, person2)


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.


def final_damage(person1, person2):
    damage = person1["damage"] / person2["armor"]
    return damage


# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def save(person):
    with open(os.path.join('data', '{0}.txt'.format(person["name"])), 'wb') as handle:
        pickle.dump(person, handle)


def load(person):
    with open(os.path.join('data', '{0}.txt'.format(person["name"])), 'rb') as handle:
        pickle.load(handle)
    return person


def fight(person1, person2):
    while person1["health"] > 0 and person2["health"] > 0:
        attack(person1, person2)
        attack(person2, person1)
    print_result(person1, person2)


def print_result(person1, person2):
    if person1["health"] > 0 and person2["health"] <= 0:
        print('{0} - победитель, осталось {1} здоровья'.format(person1["name"], person1["health"]))
    elif person1["health"] < 0 and person2["health"] >= 0:
        print('{0} - победитель, осталось {1} здоровья'.format(person2["name"], person2["health"]))


save(player)
save(enemy)

fight(load(player), load(enemy))
