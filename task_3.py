user_month = input("Введите месяц: ")
season_list = ['winter', 'spring', 'spring', 'autumn']
season_dict = {1: 'winter', 2: 'spring', 3: 'spring', 4: 'autumn'}
if user_month.isdigit() and 0 < int(user_month) <= 12:
    if 12 == int(user_month) or 1 <= int(user_month) <= 2:
        print(f'list: {season_list[0]}')
        print(f'dict: {season_dict.get(1)}')
    elif 3 <= int(user_month) <= 5:
        print(f'list: {season_list[1]}')
        print(f'dict: {season_dict.get(2)}')
    elif 6 <= int(user_month) <= 8:
        print(f'list: {season_list[2]}')
        print(f'dict: {season_dict.get(3)}')
    else:
        print(f'list: {season_list[3]}')
        print(f'dict: {season_dict.get(4)}')
else:
    print("Вы ввели неверный месяц")
