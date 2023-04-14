from file_read import read_table, read_x_values 
import printer
from interpolation import lagrange_interpolation
from painter import draw

def main():
    # выбор режима работы
    printer.print_working_mode_message() 
    working_mode = str(input('>'))
    filename = str(input('Имя файла>'))

    match working_mode:
        case '1':
            function_values = read_table(filename)
            x_values = function_values[0]
            y_values = function_values[1]
            x = float(input('x>'))
            fv = lagrange_interpolation(x_values, y_values, x_values, x)
            fv = fv[-1]
            print(f'L({x}) = {fv}')
        case '2':
            x_mas = read_x_values(filename)
            functions = str(input('Функции>')).replace(',', '').split()
            print(f'Введённые функции: {functions}')
            draw(functions, x_mas)


if __name__ == '__main__':
    main()
