# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел

class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.prime_numbers = []

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        self.i += 1
        for number in range(self.i, self.n + 1):
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.i = number
                self.prime_numbers.append(number)
                return number
        raise StopIteration()


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# print(get_prime_numbers(n=100))


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик

#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    i = 2
    prime_numbers = []
    for number in range(i, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


# for number in prime_numbers_generator(n=100000):
#     print(number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def check_happy_number(number):
    str_number = str(number)
    if len(str_number) <= 2:
        return False
    if len(str_number) % 2 == 0:
        middle_index = int(len(str_number) / 2)
        first_half = sum([int(x) for x in str_number[:middle_index]])
        second_half = sum([int(x) for x in str_number[middle_index:]])
    else:
        middle_index = int((len(str_number) - 1) / 2)
        first_half = sum([int(x) for x in str_number[:middle_index]])
        second_half = sum([int(x) for x in str_number[middle_index + 1:]])
    if first_half == second_half:
        return True


def check_polindrome(number):
    str_number = str(number)
    if len(str_number) <= 2:
        return False
    if len(str_number) % 2 == 0:
        middle_index = int(len(str_number) / 2)
        first_half = [x for x in str_number[:middle_index]]
        second_half = [x for x in str_number[-1:middle_index - 1:-1]]
    else:
        middle_index = int((len(str_number) - 1) / 2)
        first_half = [x for x in str_number[:middle_index]]
        second_half = [x for x in str_number[-1:middle_index:-1]]
    if first_half == second_half:
        return True


# for number in prime_numbers_generator(n=100000):
#     if check_polindrome(number):
#         print(number)


def check_mersenn_number(number):
    for n in range(500):
        if number == 2 ** n - 1:
            return True


for number in prime_numbers_generator(n=1000000):
    if check_mersenn_number(number):
        print(number)
