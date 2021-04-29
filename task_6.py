day_result = float(input("Введите количество начальное количество километров: "))
goal_result = float(input("Введите желаемое количество километров: "))
days = 1
while goal_result > day_result:
    day_result += day_result / 10
    days += 1

print(f"Вы достигните результата на {days} день")
