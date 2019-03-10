# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
from lesson05.home_work.hw05_easy import show_files


def remove():
    rm = input("Введите название папки: ")
    try:
        os.rmdir(os.path.join(os.getcwd(), rm))
        print('Папка {} успешно удалена'.format(rm))
    except FileNotFoundError as e:
        print('{} - невозможно удалить. Папки не существует'.format(e.filename))
    except OSError as o:
        print('{} - невозможно удалить. Папка не пустая'.format(o.filename))


def make():
    mk = input("Введите название папки: ")
    try:
        os.mkdir(os.path.join(os.getcwd(), mk))
        print('Папка {} успешно создана'.format(mk))
    except FileExistsError as e:
        print('Папка {} - уже существует'.format(e.filename))


def change_dir():
    cd = input("Введите название папки: ")
    try:
        os.chdir(cd)
        print("Перешел в папку: {}".format(cd))
    except OSError as e:
        print("Папка {} не найдена".format(e.filename))


def start():
    while True:
        try:
            user_input = int(input("\nВыбор действия:\n"
                                   "1. Перейти в папку\n"
                                   "2. Просмотреть содержимое текущей папки\n"
                                   "3. Удалить папку\n"
                                   "4. Создать папку\n"
                                   "0. Выход\n"
                                   "==============================\n"))
            if user_input == 1:
                change_dir()

            if user_input == 2:
                show_files()

            if user_input == 3:
                remove()

            if user_input == 4:
                make()

            if user_input == 0:
                break

        except ValueError:
            print("Такого действия не существует")


start()
