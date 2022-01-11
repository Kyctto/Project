# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class LogParser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.prev_line = None
        self.meter = 0
        with open(file='result.txt', mode='w', encoding='utf8') as file:
            pass

    def collect(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                if line.endswith('NOK\n'):
                    self.metering(line=line)
            self.write()

    def _line_convert(self, line):
        line = line[0:17]
        return line

    def metering(self, line):
        line = self._line_convert(line=line)
        if self.prev_line is None:
            self.meter += 1
            self.prev_line = line

        elif line != self.prev_line:
            self.write()
            self.meter = 1
            self.prev_line = line
        else:
            self.meter +=1

    def write(self):

        with open(file='result.txt', mode='a', encoding='utf8') as file:
            line_to_write = self.prev_line + '] ' + str(self.meter) + '\n'
            file.write(line_to_write)






class LogParserHour(LogParser):
    def _line_convert(self, line):
        line = line[0:14]
        return line

class LogParserMonth(LogParser):
    def _line_convert(self, line):
        line = line[0:8]
        return line

class LogParserYear(LogParser):
    def _line_convert(self, line):
        line = line[0:5]
        return line

pars = LogParserYear(file_name='events.txt')
pars.collect()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
