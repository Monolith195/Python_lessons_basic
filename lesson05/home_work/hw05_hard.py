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

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создание копии файла в текущей директории")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - изменение текущей директории на указанную")
    print("ls - отображение полного пути текущей директории")


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


def copy():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        shutil.copy(file_path, "copy_{}".format(file_name))
        print("Файл {} успешно скопирован".format(file_name))
    except FileNotFoundError:
        print("Файл {} не найден".format(file_name))


def remove():
    if not remove_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), remove_name)
    answer = input("Вы уверены что хотите удалить {}? [y/n]: ".format(remove_name))
    if answer.lower() == "y":
        try:
            os.remove(file_path)
            print("Файл {} успешно удален".format(remove_name))
        except FileNotFoundError:
            print("Файл {} не найден".format(remove_name))
    else:
        print("Файл {} не удален".format(remove_name))


def change_directory():
    if not cd_path:
        print("Необходимо указать путь вторым параметром")
        return
    try:
        os.chdir(cd_path)
        print("Текущая директория: {}".format(os.getcwd()))
    except FileNotFoundError:
        print("Указанная директория {} не найдена".format(cd_path))


def show_full_path():
    print("Путь до текущей директории: {}".format(os.getcwd()))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy,
    "rm": remove,
    "cd": change_directory,
    "ls": show_full_path
}

try:
    dir_name = sys.argv[2]
    file_name = sys.argv[2]
    remove_name = sys.argv[2]
    cd_path = sys.argv[2]
except IndexError:
    dir_name = None
    file_name = None
    remove_name = None
    cd_path = None

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
