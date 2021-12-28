# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile
from pprint import pprint


class CharStats:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.summa = 0


    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] +=1
                else:
                    self.stat[char] = 1
                self.summa +=1

    def sorted(self):

        print ('+----------+----------+')
        for i , k in sorted(self.stat.items(), key=lambda item: item[1], reverse=True):
            print (f'|{i:^10}|{k:^10}|')
        print('+----------+----------+')
        print(f'|{"Всего":^10}|{self.summa:^10}|')

    def revers_sorted(self):

        print('+----------+----------+')
        for i, k in sorted(self.stat.items(), key=lambda item: item[1], reverse=False):
            print(f'|{i:^10}|{k:^10}|')
        print('+----------+----------+')
        print(f'|{"Всего":^10}|{self.summa:^10}|')


    def key_sort(self):

        print('+----------+----------+')
        for i, k in sorted(self.stat.items()):
            print(f'|{i:^10}|{k:^10}|')
        print('+----------+----------+')
        print(f'|{"Всего":^10}|{self.summa:^10}|')


    def key_sort_revers(self):

        print('+----------+----------+')
        for i, k in sorted(self.stat.items(),reverse=True):
            print(f'|{i:^10}|{k:^10}|')
        print('+----------+----------+')
        print(f'|{"Всего":^10}|{self.summa:^10}|')




    def print (self):
        # to_print = sorted(self.stat.items())
        # pprint(to_print)
        pprint(self.stat)
        print(self.summa)

new = CharStats(file_name='voyna-i-mir.txt')
new.collect()
new.key_sort_revers()
# new.print()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
