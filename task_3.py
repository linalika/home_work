def my_func(x, y, z):
    numbers = [x, y, z]
    max_of_numbers = max(numbers)
    min_of_numbers = min(numbers)
    total = [max_of_numbers, min_of_numbers]
    result = sum(total)
    return result


def main():
    num_1 = 3
    num_2 = 9
    num_3 = 0
    result = my_func(num_1, num_2, num_3)
    print(result)


main()
