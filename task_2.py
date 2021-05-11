def input_data(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


def main():
    user_name = input('Введите имя: ')
    user_surname = input('Введите фамилию: ')
    user_year = input('Введите год рождения: ')
    user_city = input('Введите город проживаня: ')
    user_email = input('Введите email: ')
    user_phone = input('Введите телефон: ')
    result = input_data(user_name, user_surname, user_year, user_city, user_email, user_phone)
    print(f'{result}')


main()
