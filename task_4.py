number = input("Введите целое число: ")
number = int(number)
max = number % 10
number = number // 10
while number > 0:
    if number % 10 > max:
        max = number % 10
    number = number // 10

print(f'Самая большая цифра в числе: {max}')
