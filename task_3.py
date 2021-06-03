class NotNumberError(Exception):
    pass


my_list = []

while True:
    val = input('Введите значения и нажимайте Enter - ')


    if val.isdigit():
        my_list.append(val)
    else:
        raise NotNumberError('Вы ввели не число')

    if input('Для выхода из приложения введите stop, для продолжения Enter: ') == 'stop':
        print(f'вы ввели числа {my_list}')
        break
