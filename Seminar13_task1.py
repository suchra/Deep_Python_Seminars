# Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.

import re


class NameValidationException(Exception):
    def __init__(self, attribute_name, error_message):
        self.attribute_name = attribute_name
        self.error_message = error_message
        super().__init__(f"Ошибка валидации атрибута '{attribute_name}': {error_message}")


class NameValidator:
    def __init__(self, pattern, error_message):
        self.pattern = pattern
        self.error_message = error_message

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not re.match(self.pattern, value, re.UNICODE):
            raise NameValidationException(self.name, self.error_message)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Student:
    first_name = NameValidator(r'^[А-Я][а-я]*$',
                               "First name should start with a capital letter and contain only letters.")
    last_name = NameValidator(r'^[А-Я][а-я]*$',
                              "Last name should start with a capital letter and contain only letters.")
    middle_name = NameValidator(r'^[А-Я][а-я]*$',
                                "Middle name should start with a capital letter and contain only letters.")

    def __init__(self, first_name, last_name, middle_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name


try:
    student = Student("Иван", "Иванов", "Иванович")
    print("Student's full name:", student.first_name, student.middle_name, student.last_name)

    student.first_name = "иван"
    student.last_name = "Иванов1"
except NameValidationException as e:
    print("Error:", e)