my_rate = [7, 5, 3, 3, 2]
user_rate = input('Введите новый рейтинг: ')
if user_rate.isdigit():
    user_rate = int(user_rate)
    for i in range(len(my_rate)):
        if my_rate[i] == user_rate:
            my_rate.insert(i, user_rate)
            break
        else:
            my_rate.append(user_rate)
            break
print(my_rate)
