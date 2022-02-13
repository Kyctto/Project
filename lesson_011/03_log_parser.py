# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


class LogParser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.prev_line = None
        self.meter = 0
        self.line = None
        self.switch = 0

    def line_convert(self, line):
        line = line[0:17] +']'
        return line

    def metering(self, line):
        self.line = self.line_convert(line=line)
        if self.prev_line is None:
            self.prev_line = self.line
        elif self.line != self.prev_line:
            return True
        else:
            self.meter += 1

    def __iter__(self):
        self.file = open(self.file_name, 'r')
        return self

    def __next__(self):
        self.meter = 1
        self.prev_line = self.line
        for line in self.file:
            if line.endswith('NOK\n'):
                if self.metering(line=line):
                    return self.prev_line, self.meter
        if self.switch == 0:
            self.switch = 1
            return self.prev_line, self.meter
        self.file.close()
        raise StopIteration()


grouped_events = LogParser(file_name='events.txt')
for group_time, event_count in grouped_events:
    print(f'{group_time} {event_count}')
