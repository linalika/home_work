class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def transform(cls, date):
        day, month, year = map(int, date.split('-'))
        print(day, month, year)

    @staticmethod
    def validate(*date):
        # метод статический, может быть вызван на любом наборе данных
        if not all(map(lambda x: isinstance(x, int), date)):
            return print("Неверные данные")

        day, month, year = date
        return all([1 <= day <= 31, 1 <= month <= 12, year >= 1970])


date = Date('2020-06-02')
date.transform('2020-06-02')
date.validate('2020-16-02')