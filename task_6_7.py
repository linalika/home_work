# Решение для 6 и 7 заданий

def int_func(user_string):
    return user_string.title()


def main():
    user_string = input('Введите слова: ')
    result = int_func(user_string)
    print(result)


main()
