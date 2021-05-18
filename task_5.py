from random import randint

numbers = [str(randint(-10, 10)) for _ in range(10)]
numbers_str = ' '.join(numbers)
with open('task_5.txt', 'w+') as f:
    f.write(numbers_str)
