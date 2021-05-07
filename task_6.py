products = []
product_description = {}
analytics = {}
name = []
price = []
count = []
unit = []
while input("Если вы хотите ввести номер товара, введите yes ") == 'yes':
    number = int(input("Введите номер товара: "))
    product_name = input("Введите название: ")
    product_price = input("Введите цену: ")
    product_count = input('Введите количество: ')
    product_unit = input("Введите единицу измерения: ")
    product_description = dict({'название': product_name, 'цена': product_price,
                                'количество': product_count, 'eд': product_unit})
    products.append(tuple([number, product_description]))
    name.append(product_name)
    price.append(product_price)
    count.append(product_count)
    unit.append(product_unit)
analytics['название'] = name
analytics['цена'] = price
analytics['количество'] = count
analytics['eд'] = unit

for i in range(len(products)):
    print(products[i])

for item in analytics.items():
    print(item)
