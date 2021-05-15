def div(dividend, divider):
    try:
        result = round(float(dividend) / float(divider), 2)
    except ValueError:
        result = 'Введены неверные данные'
    except ArithmeticError:
        result = 'Ошибка, деление на ноль!'
    return result


def main():
    number_1 = input('Введите делимое: ')
    number_2 = input('Введите делитель: ')
    print(div(number_1, number_2))


main()
