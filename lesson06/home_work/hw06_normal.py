# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, person):
        person.health -= self._pure_damage(person)

    def _pure_damage(self, person):
        return self.damage / person.armor


class Player(Person):
    def __init__(self, health, damage, armor):
        Person.__init__(self, health, damage, armor)


class Enemy(Person):
    def __init__(self, health, damage, armor):
        Person.__init__(self, health, damage, armor)


class Start:
    player = Player(100, 25, 2)
    enemy = Enemy(100, 20, 2)

    while player.health >= 0 and enemy.health >= 0:
        player.attack(enemy)
        enemy.attack(player)

    if player.health > 0 >= enemy.health:
        print("Player победитель - осталось {} здоровья".format(round(player.health)))
    elif enemy.health > 0 >= player.health:
        print("Enemy победитель - осталось {} здоровья".format(round(enemy.health)))
