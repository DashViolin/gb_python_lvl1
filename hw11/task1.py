from datetime import date


class Date:
    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def extract(cls, date_str: str):
        try:
            day, month, year = map(int, date_str.split('-'))
        except ValueError:
            raise ValueError('Date format must be "day-month-year"')
        return day, month, year

    @staticmethod
    def validate(date_str: str):
        day, month, year = Date.extract(date_str)
        date(year, month, day)
        print(f'Date {date_str} is correct')


def check(data):
    for date_str in data:
        try:
            Date.validate(date_str)
        except ValueError as ex:
            print(ex)


check(['01-11-2021', '-01-11-2021', '13-13-2021', '33-11-2021', '29-02-2020'])
