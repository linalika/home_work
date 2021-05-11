def my_fanc(x, y):
    result = 1 / x ** abs(y)
    return result

def main():
    x = 5
    y = -2
    result = my_fanc(x, y)
    print(result)


main()
