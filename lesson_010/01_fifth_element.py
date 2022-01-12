# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError as exp:
    print(f'Невозможно преобразовать "{input_data[4]}" к числу ')
except IndexError as exp:
    print(f'Неверное количество введенных символов {len(input_data)} < 5')
except Exception:
    print(f'Ты вообще в своём уме? {Exception}')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
