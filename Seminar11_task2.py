# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнени

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __add__(self, other):
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_length = max(self.length - other.length, 0)
        new_width = max(self.width - other.width, 0)
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __str__(self):
        return f"Rectangle({self.length}, {self.width})"

rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 6)
rectangle3 = Rectangle(4, 4)

print("Rectangle 1:", rectangle1)
print("Rectangle 2:", rectangle2)
print("Rectangle 3:", rectangle3)

print("Rectangle 1 == Rectangle 2:", rectangle1 == rectangle2)
print("Rectangle 1 < Rectangle 2:", rectangle1 < rectangle2)
print("Rectangle 1 <= Rectangle 2:", rectangle1 <= rectangle2)
print("Rectangle 1 > Rectangle 2:", rectangle1 > rectangle2)
print("Rectangle 1 >= Rectangle 2:", rectangle1 >= rectangle2)
print("Rectangle 1 != Rectangle 2:", rectangle1 != rectangle2)

print("Rectangle 1 == Rectangle 3:", rectangle1 == rectangle3)