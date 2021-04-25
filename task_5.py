proceed = int(input("Введите сумму выручки: "))
cost = int(input("Введите сумму издержек: "))
profit = round((proceed - cost), 2)
if profit < 0:
    print("Фирма работает в убыток")
elif profit > 0:
    print(f'Фирма работает в прибыль, прибыль составляет {profit}')
    staff = int(input("Введите количество сотрудников: "))
    profitability = round((profit / proceed * 100), 2)
    profit_by_staff = round(profit / staff, 2)
    print(f'Рентабельность выручки сотавила {profitability}')
    print(f'Прибыль в расчете на одного сторудника сотавила {profit_by_staff}')
else:
    print("Фирма работает в ноль")
