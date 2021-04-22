number = input("Введите число:")


def is_number(number):
    try:
        float(number)
        if float(number) == int(float(number)):
            print("Вы ввели целое число " + number)
        else:
            print("Вы ввели десятичное число " + number)
    except:
        print("Вы ввели не число")


is_number(number)
