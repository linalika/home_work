user_list = list(input('Введите список элементов: ').split())
count = 1
for i in range(0, len(user_list), 2):
    if count == len(user_list):
        break
    elif i + 3 == len(user_list):
        break
    else:
        temporary = user_list[i]
        user_list[i] = user_list[i + 1]
        user_list[i + 1] = temporary
print(user_list)
