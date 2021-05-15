def my_func(x, y, z):
    numbers = [x, y, z]
    numbers.remove(min(numbers))
    result = sum(numbers)
    return result


def main():
    num_1 = 3
    num_2 = 9
    num_3 = 0
    result = my_func(num_1, num_2, num_3)
    print(f'Сумма максимальных чисел {result}')


main()
