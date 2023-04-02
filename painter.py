import matplotlib.pyplot as plt
import numpy as np
from math import *
from interpolation import lagrange_interpolation


def draw(func: list[str], interval: list[float]) -> None:
    '''Отрисовывает переданные функции'''
    # настройка поля для рисования
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)

    # разбивка интервала на более мелкие для построения фукнции
    x_copy = interval.copy()
    y_copy = []

    for f in func:
        tmp = []
        for x in x_copy:
            tmp.append(eval(f))
        y_copy.append(tmp)

    interval.sort()
    x_range = np.arange(interval[0], interval[-1], 0.001)

    # вычисление фукнций
    y_range = []
    for f in func:
        tmp = []
        for x in x_range:
            tmp.append(eval(f))
        y_range.append(tmp)

    for y in y_copy:
        lx = lagrange_interpolation(x_copy, y, interval)
        plt.plot(x_range, lx)

    # отрисовка графиков
    for y in y_range:
        plt.plot(x_range, y)

    # отрисовка точек
    for f in func:
        for x in interval:
            plt.scatter(x, eval(f), color='#c9007a')
    plt.show()

    


