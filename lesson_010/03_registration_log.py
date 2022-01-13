# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import os


def check(line):
    line = line[:-1]
    line = line.split(' ')
    if len(line) < 3:
        raise ValueError()
    elif not line[0].isalpha():
        raise NotNameError()
    elif not line[1].count('@') or not line[1].count('.'):
        raise NotEmailError()
    elif not 10 < int(line[2]) < 99:
        raise ValueError()
    return True

class NotNameError(Exception):

    def __str__(self):
        return 'NotNameError'

class NotEmailError(Exception):
    def __str__(self):
        return f'{self.__class__}'

def write_log(filename, line, ext=None):
    if ext:
        with open(file=filename, mode='a', encoding='utf8') as log:
            log.write(line)
    with open(file=filename, mode='a', encoding='utf8') as log:
        log.write(line)


good_log_path = """F:/Users/Кусто/Desktop/Project/lesson_010/registrations_good.log"""
bad_log_path = """F:/Users/Кусто/Desktop/Project/lesson_010/registrations_bad.log"""
if os.path.isfile(good_log_path):
    os.remove(good_log_path)
if os.path.isfile(bad_log_path):
    os.remove(bad_log_path)




with open(file='registrations.txt', mode='r', encoding='utf8') as file:
    for line in file:
        try:
            if check(line=line):
                write_log(filename=good_log_path, line=line)

        except ValueError as exc:
            report = (f'{line[:-1]}  {type(exc)}\n')
            write_log(filename=bad_log_path,line=report)

        except NotNameError as exc:
            report = (f'{line[:-1]}  {exc}\n')
            write_log(filename=bad_log_path, line=report)

        except NotEmailError as exc:
            report = (f'{line[:-1]}  {exc}\n')
            write_log(filename=bad_log_path, line=report)




