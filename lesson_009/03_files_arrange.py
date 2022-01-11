# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint

path = """E:\Torrent's KycTo\Python Обучение\[SkillBox] [Вадим Шандринов] Python-разработчик\9. Работа с файлами и форматированный вывод\lesson_009\icons"""
new_path = """E:\Torrent's KycTo\Python Обучение\[SkillBox] [Вадим Шандринов] Python-разработчик\9. Работа с файлами и форматированный вывод\lesson_009\icons_by_year"""

class Sort:

    def __init__(self,old_path, new_path):
        self.path = old_path
        self.new_path = new_path
        if not os.path.exists(new_path):
            os.makedirs(name=new_path)


    def create_dir(self, year_dir, month_dir):
        new_dir = os.path.join(self.new_path, year_dir, month_dir)
        if not os.path.exists(new_dir):
            os.makedirs(name=new_dir)
        return new_dir


    def file_sort(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                full_file_path = os.path.join(dirpath, filename)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                year_dir = str(file_time[0])
                month_dir = str(file_time[1])
                new_dir = self.create_dir(year_dir=year_dir, month_dir=month_dir)
                new_full_path = os.path.join(new_dir, filename)
                shutil.copy2(src=full_file_path, dst=new_full_path)


new_script = Sort(old_path=path, new_path=new_path)
new_script.file_sort()



# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
