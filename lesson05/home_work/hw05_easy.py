import os
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make():
    for i in range(1, 10):
        try:
            os.mkdir(os.path.join(os.getcwd(), 'dir_{}'.format(i)))
        except FileExistsError as e:
            print('{} - уже существует'.format(e.filename))


def remove():
    for i in range(1, 10):
        try:
            os.rmdir(os.path.join(os.getcwd(), 'dir_{}'.format(i)))
        except FileNotFoundError as e:
            print('{} - не существует'.format(e.filename))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_files():
    files = os.listdir(path=os.getcwd())
    if not files:
        print("Папка пуста\n")
    else:
        print('Файлы и папки:\n', *files, sep='\n')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file():
    cp = os.path.basename(__file__).split(".")
    shutil.copy(os.path.basename(__file__), "{}-copy.{}".format(cp[0], cp[1]))
