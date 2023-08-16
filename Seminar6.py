# 1. Создайте модуль и напишите в нём функцию,
# которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# 2. В модуль с проверкой даты добавьте возможность запуска в терминале
# с передачей даты на проверку.

def is_leap_year(year):
    """Function checks if the year is a leap year."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    return True


def is_valid_date(date):
    """Function checks the date for correctness."""
    try:
        day, month, year = map(int, date.split('.'))
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap_year(year):
            days_in_month[2] = 29
        if day < 1 or day > days_in_month[month]:
            return False
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    input_date = input("Введите дату в формате DD.MM.YYYY: ")
    if is_valid_date(input_date):
        print("Дата существует.")
    else:
        print("Дата не существует.")