# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
# Чтобы записать байты можно использовать список с числами и функцию bytes

import os
import random
import string


def generate_name(min_length=6, max_length=30):
    """The function generates a random name for the file."""
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def create_files(extension,
                 min_name_len=6,
                 max_name_len=30,
                 min_bytes=256,
                 max_bytes=4096,
                 num_files=42):
    """The function creates the specified number of files with the specified
    extension, random names, sizes, and content."""
    if not extension.startswith('.'):
        extension = '.' + extension

    for _ in range(num_files):
        filename = generate_name(min_name_len, max_name_len) + extension
        file_size = random.randint(min_bytes, max_bytes)

        with open(filename, 'wb') as file:
            file.write(os.urandom(file_size))

        print(f"Created file: {filename} ({file_size} bytes)")


create_files('.txt', 8, 15, 300, 5000, 2)