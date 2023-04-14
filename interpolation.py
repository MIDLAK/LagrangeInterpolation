import numpy as np


def lagrange_interpolation(x_values: list[float], y_values: list[float],
                           interval: list[float], x=None) -> list[float]:
    print(f'x = {x_values}')
    print(f'y = {y_values}')
    interval.sort()
    
    if x != None:
        interval.append(x)

    x_range = np.arange(interval[0], interval[-1], 0.001)
    n = len(y_values)
    function_values_approx = []

    for x in x_range:
        s = 0.0
        for k in range(n):
            # числитель
            numerator = 1.0
            # знаменатель
            denominator = 1.0
            for j in range(n):
                if j != k:
                    numerator = numerator * (x - x_values[j])
                    denominator = denominator * (x_values[k] - x_values[j])
            s = s + (numerator / denominator) * y_values[k]
        function_values_approx.append(s)
    return function_values_approx






