# Создайте класс Матрица. Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition.")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix.")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                result.data[i][j] = dot_product
        return result

# Пример использования
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

print("Matrix 3:")
print(matrix3)

print("Matrix 1 == Matrix 2:", matrix1 == matrix2)
print("Matrix 1 + Matrix 2:")
print(matrix1 + matrix2)

print("Matrix 1 * Matrix 3:")
print(matrix1 * matrix3)