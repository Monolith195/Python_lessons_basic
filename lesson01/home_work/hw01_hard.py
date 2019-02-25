__author__ = 'Зайцев Андрей'


# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!


class Profile:
    def __init__(self, name, family_name, age, weight):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.weight = weight

    @staticmethod
    def enter_data():
        name = input("Введите имя - ")
        family_name = input("Введите фамилию - ")
        age = int(input("Введите возраст - "))
        weight = int(input("Введите вес - "))
        return Profile(name, family_name, age, weight)

    @staticmethod
    def print_result():
        profile = Profile.enter_data()
        result = "{0} {1}, {2} год, вес {3} - ".format(profile.name, profile.family_name, profile.age, profile.weight)
        if profile.age < 30 and 50 < profile.weight < 120:
            print(result + "хорошее состояние")
        elif profile.age > 30 and (profile.weight < 50 or profile.weight > 120):
            print(result + "следует заняться собой")
        elif profile.age > 40 and (profile.weight < 50 or profile.weight > 120):
            print(result + "следует обратится к врачу!")


Profile.print_result()
