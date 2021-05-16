my_list = [99, 45, 2, 2, 11, 55, 11, 67, 1, 8, 1, 2, 99, 30]

my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Исходный список {my_list}')
print(f'Новый список, не имеющий повторений {my_new_list}')
