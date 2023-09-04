# класс прямоугольник.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __add__(self, other):
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_length = max(self.length - other.length, 0)
        new_width = max(self.width - other.width, 0)
        return Rectangle(new_length, new_width)

    def __str__(self):
        return f"Rectangle({self.length}, {self.width})"

# Пример использования
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 6)

print("Rectangle 1:", rectangle1)
print("Rectangle 2:", rectangle2)

sum_rectangle = rectangle1 + rectangle2
print("Sum of rectangles:", sum_rectangle)

diff_rectangle = rectangle1 - rectangle2
print("Difference of rectangles:", diff_rectangle)