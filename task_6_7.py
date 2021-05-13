# Решение для 6 и 7 заданий

def int_func(*args):
    user_string = list(args)
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(len(user_string)):
        if not set(user_string[i]).difference(latin_char):
            user_string[i] = user_string[i].title()
        else:
            user_string.remove(user_string[i])
    return user_string


def main():
    user_string = input('Введите слова: ').split()
    result = int_func(*user_string)
    print(result)


main()
