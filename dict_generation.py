# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt

# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

def way_func(way):
# print(way)
    *a, b = way
    d, c = b.split('.')
    print(('/'.join(a), d, '.' + c))

way = ('c:/Users/Vladislav/Desktop/deep_to_python/test.txt'.split('/'))
way_func(way)