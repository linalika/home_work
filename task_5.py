my_rate = [7, 5, 3, 3, 2]
user_rate = input('Введите новый рейтинг: ')
i = 0
if user_rate.isdigit():
    user_rate = int(user_rate)
    for rate in my_rate:
        if user_rate <= rate:
            i += 1
    my_rate.insert(i, user_rate)
print(my_rate)


