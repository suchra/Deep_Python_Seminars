import logging
import argparse

# Инициализация системы логирования
logging.basicConfig(level=logging.INFO, filename='date_validator.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DateValidator:
    @staticmethod
    def is_leap_year(year):
        """
        Проверяет, является ли год високосным.
        """
        try:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        except Exception as e:
            logging.error(f"An error occurred in is_leap_year: {str(e)}")
            return False

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

                return day <= days_in_month[month]
            return False
        except ValueError:
            return False
        except Exception as e:
            logging.error(f"An error occurred in is_valid_date: {str(e)}")
            return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate a date string.')
    parser.add_argument('date_str', type=str, help='Date string to validate (e.g., "29.02.2028")')
    args = parser.parse_args()

    if DateValidator.is_valid_date(args.date_str):
        print(f"{args.date_str} - корректная дата")
    else:
        print(f"{args.date_str} - некорректная дата")