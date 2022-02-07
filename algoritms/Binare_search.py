import time
from pprint import pprint
from random import randint
def time_track(func):
    def surogate(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        run_time = round(end_time - start_time, 5)
        print(f'Программа {func.__name__} была выполнена за {run_time} секунд(ы)')
        return result
    return surogate

@time_track
def sorted_list(n):
    list = []
    i = 0
    for _ in range (n):
        list.append(i)
        i += 1
    return list

@time_track
def lin_search(list, find_value):
    for i in list:
        if find_value == i:
            return print(f'Найдено значение {find_value}, количество итераций {i}')

@time_track
def binary_search(list, find_value):
    low = 0
    high = list[-1]
    iter_value = 1
    if low == find_value:
        return print(f'Найдено значение {find_value}, количество итераций {iter_value}')
    elif high == find_value:
        return print(f'Найдено значение {find_value}, количество итераций {iter_value}')
    while low <= high:
        mid = int((low + high)/2)
        mid_value = list[mid]
        if mid_value == find_value:
            return print(f'Найдено значение {find_value}, количество итераций {iter_value}')
        elif mid_value > find_value:
            high = mid - 1
            iter_value += 1
        else:
            low = mid + 1
            iter_value += 1
    return None

#
# n = 2**25
# print (n)
# list = sorted_list(n)
# find_value = randint(0, n)
# lin_search(list=list, find_value=find_value)
# binary_search(list=list, find_value=find_value)






