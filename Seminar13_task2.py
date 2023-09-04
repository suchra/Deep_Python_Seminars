# Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.

class InvalidDateFormatError(Exception):
    def __init__(self, date_str):
        self.date_str = date_str
        super().__init__(f"Некорректный формат даты: {date_str}")


class InvalidDateError(Exception):
    def __init__(self, date_str):
        self.date_str = date_str
        super().__init__(f"Некорректная дата: {date_str}")


class DateValidator:
    @staticmethod
    def is_leap_year(year):
        """
        Проверяет, является ли год високосным.
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def is_valid_date(date_str):
        """
        Проверяет, является ли дата корректной.
        """
        try:
            day, month, year = map(int, date_str.split('.'))

            if 1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999:
                days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                if DateValidator.is_leap_year(year):
                    days_in_month[2] = 29

                if day <= days_in_month[month]:
                    return True
                else:
                    raise InvalidDateError(date_str)
            else:
                raise InvalidDateError(date_str)
        except ValueError:
            raise InvalidDateFormatError(date_str)


# Пример использования
date_str = "29.02.2023"
try:
    if DateValidator.is_valid_date(date_str):
        print(f"{date_str} - корректная дата")
except InvalidDateFormatError as e:
    print(f"Ошибка: {e}")
except InvalidDateError as e:
    print(f"Ошибка: {e}")