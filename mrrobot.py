import os
import sys
import psutil  #Сторонний установлен через CMD: pip install psutil
import shutil
import random

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print('файл', newfile, 'успешно создана')
            return True
        else:
            print("Возникли проблемы копирования")
            return False

def sys_info():
    print("Вот что я знаю о системе:")
    print("Имя рабочей директории:", os.getcwd())
    print("Платформа (ОС):", sys.platform)
    print("Кодировка системы:", sys.getfilesystemencoding())
    print("Логин пользователя:", os.getlogin())
    print("Количество CPU:", psutil.cpu_count())

def random_delete(dirname):
    file_list = os.listdir(dirname)
    if file_list:
        i = random.randrange(0, len(file_list))
        fullname = os.path.join(dirname, file_list[i])
        if os.path.isfile(fullname):
            os.remove(fullname)
            print('Файл', fullname, 'был случайно удален')

def del_duplicats(dirname):
    file_list = os.listdir(dirname)
    double_count = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                double_count += 1
                print("Файл", fullname, "был успешно удален")
    return double_count

def duble_files(dirname):
    file_list = os.listdir()
    i = 0
    while i < len(file_list):
        duplicate_file(file_list[i])
        i += 1

def main():
    print("Привет, программист!")
    name = input("Ваше имя: ")
    print(name, ", добро пожаловать в мир Python !")

    answer = ''

    while answer != 'q':
        answer = input("Давайте поработаем ? (Y/N/q) ")
        if answer == 'Y':
            print("Отлично, хозяин !")
            print("Я могу:")
            print(" [1] вывести список файлов текущей директории")
            print(" [2] вывести информацию о системе")
            print(" [3] вывести список процессов")
            print(" [4] продублировать файлы в текущей дериктории")
            print(" [5] дублировать указанный Вами файл")
            print(" [6] удалить все файлы с окончанием '.dupl' в указанной Вами директории")
            print(" [7] удалить случайный файл")
            do = int(input("Укажите номер действия: "))
            if do == 1:
                print(os.listdir())
            elif do == 2:
                sys_info()

            elif do == 3:
                print("PIDы процессов:", psutil.pids())
            elif do == 4:
                print("=Дублирование файлов в текущей дериктории=")
                duble_files('.')

            elif do == 5:
                file_list = os.listdir()
                print(file_list)
                print('Какой файл вы хотите продублировать?')
                filename = input("введите имя файла:")
                duplicate_file(filename)
            elif do == 6:
                print("Введите дерикторию в которой будем удалять: (например, D:\\1 Work\Python): ")
                dirname = input()
                count = del_duplicats(dirname)
                print("Удаленно файлов: ", count)
            elif do == 7:
                print("Удаление случайного файла ")
                dirname = input("Укажите имя дериктории:")
                random_delete(dirname)
            else:
                pass
        elif answer == 'N':
            print("Ты хочешь отказаться? -Ха, но я не сдамся!")
        else:
            print("неизвестный выбор")
    print("Вы нажали q для выхода из программы. До свидания.")

if __name__ == "__main__":
    main()