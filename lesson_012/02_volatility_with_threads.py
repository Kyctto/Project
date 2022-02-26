# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# TODO тут ваш код в многопоточном стиле


import os
import threading
from  lesson_012.python_snippets.utils import time_track



class VolatilityAnalyzer(threading.Thread):

    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.result_dict = {}
        self.zero_vol_list = []
        self.volotility = 0
        self.secid = None
    def run(self):
        # self.result_dict = {}
        # self.zero_vol_list = []
        if os.path.isdir(self.path):
            for dirpath, dirnames, filenames in os.walk(self.path):
                for file in filenames:
                    full_path = os.path.join(dirpath, file)
                    analyzers = [VolatilityAnalyzer(path=full_path)]
                    for analyzer in analyzers:
                        analyzer.start()
                    for analyzer in analyzers:
                        analyzer.join()
                    for analyzer in analyzers:
                        if analyzer.volotility == 0.0:
                            self.zero_vol_list.append(analyzer.secid)
                        else:
                            self.result_dict[analyzer.secid] = analyzer.volotility
        else:
            self.secid, self.volotility = self._get_secid_volotility(path=self.path)


        #
        #
        #              Вывод данных
        #           надо перенести отдельно в мейн
        # sorted_dict = sorted(self.result_dict.items(), key=lambda item: item[1], reverse=True)
        # print (f' Максимальная волатильность:')
        # for item, value in sorted_dict[0:3]:
        #     print (f'       {item}  : {value}%')
        # print(f' Минимальная волатильность:  ')
        # for item, value in sorted_dict[:-4:-1]:
        #     print(f'       {item}  : {value}%')
        # print('Нулевые тикеты', self.zero_vol_list)
        #
        #

    def _get_secid_volotility(self, path):
        with open(file=path) as file:
            next(file)
            min_price = 0
            max_price = 0
            for line in file:
                secid, tradetime, price, quantity = line.split(sep=',')
                price = float(price)
                if price > max_price:
                    max_price = price
                if price < min_price:
                    min_price = price
                elif min_price == 0:
                    min_price = price
            average_price = (max_price + min_price) / 2
            volatility = ((max_price - min_price) / average_price) * 100
            volatility = round(volatility, 2)
            return secid, volatility

@time_track
def main():
    probe = VolatilityAnalyzer(path='trades')
    probe.run()
    sorted_dict = sorted(probe.result_dict.items(), key=lambda item: item[1], reverse=True)
    print(f' Максимальная волатильность:')
    for item, value in sorted_dict[0:3]:
        print(f'       {item}  : {value}%')
    print(f' Минимальная волатильность:  ')
    for item, value in sorted_dict[:-4:-1]:
        print(f'       {item}  : {value}%')
    print('Нулевые тикеты', probe.zero_vol_list)
if __name__ == '__main__':
    main()