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

    # вычисление интерполяций для каждой из функций
    lx_range = []
    k = 0
    for y in y_copy:
        lx = lagrange_interpolation(x_copy, y, interval)
        f_name = func[k]
        plt.plot(x_range, lx, label=f'L(x) for {f_name}')
        lx_range.append(lx)
        k = k + 1


    # определение максимальных отклонений между графиками
    # func и их интерполяциями lx_range
    max_deviation = []
    max_current = 0.0
    f_counter = 0
    for f in func:
        for i in range(len(x_range)):
            deviation = abs(y_range[f_counter][i] - lx_range[f_counter][i])
            if max_current < deviation:
                max_current = deviation
        max_deviation.append(max_current)
        print(f"Для {f} максимальное отклонение от интерполяции составляет {max_current}")
        max_current = 0.0
        f_counter = f_counter + 1

    # отрисовка графиков
    i = 0
    for y in y_range:
        plt.plot(x_range, y, label=func[i])
        i = i + 1

    # отрисовка точек
    for f in func:
        for x in interval:
            plt.scatter(x, eval(f), color='#c9007a')

    plt.legend()
    plt.show()

    


