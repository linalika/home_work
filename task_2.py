class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Division:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def division(self):
        if self.num2 == 0:
            raise MyZeroDivisionError('Деление на ноль!')
        else:
            output = round(self.num1/self.num2, 2)
            print(output)


div = Division(1, 0)

try:
    div.division()
except MyZeroDivisionError:
    print('Деление на ноль!')

