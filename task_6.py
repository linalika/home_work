def get_title_words(user_string):
    return user_string.title()


def main():
    user_string = input('Введите слова: ')
    result = get_title_words(user_string)
    print(result)


main()
