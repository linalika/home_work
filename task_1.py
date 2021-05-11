def div(dividend, divider):
    if dividend.isdigit() and divider.isdigit():
        dividend = float(dividend)
        divider = float(divider)
        try:
            result = round(dividend / divider, 2)
        except ArithmeticError:
            result = 'Ошибка, деление на ноль!'
    else:
        result = 'Вы ввели не число'
    return result


def main():
    number_1 = input('Введите делимое: ')
    number_2 = input('Введите делитель: ')
    print(div(number_1, number_2))


main()
