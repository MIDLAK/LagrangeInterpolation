#from typing import NamedTuple


#class FunctionValues(NamedTuple):
#    x: float
#    y: float


def read_table(filename: str) -> list[list[float]]:
    '''Возвращает список значений фукнции'''
    # чтение матрицы из файла
    with open(filename) as file:
        matrix = [list(map(float, row.split())) for row in file.readlines()]

#    приведение матрицы в более удобный вид
#    function_values = []
#    for i in range(len(matrix[0])):
#        function_values.append(FunctionValues(x=matrix[0][i],
                                              #y=matrix[1][i]))
#    return function_values
    return matrix


def read_x_values(filename: str) -> list[float]:
    '''Возвращает список значений x'''
    with open(filename) as file:
        values = file.readline().split()
    x = [float(s) for s in values]
    return x

