my_list = [45, 2, 11, 55, 67, 1, 8, 99, 30]

my_new_list = [el for num, el in enumerate(my_list) if num != 0 and my_list[num] > my_list[num - 1]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
