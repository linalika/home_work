seconds = input("Введите количество секунд: ")
seconds = int(seconds)

hours = seconds // 3600
minutes = seconds % 3600 // 60
seconds = seconds % 3600 % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')
