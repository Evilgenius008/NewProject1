# Задача "Распаковка"
# 1. Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()                               # Вызов функции без аргументов
print_params(5, 'pyramid', False)   # Вызов функции с тремя аргументами
print_params(466, 'водопад')           # Вызов функции с двумя аргументами + 1 по умолчанию
print_params(b = 'экзамен')                  # Вызов функции с одним аргументом + 2 по умолчанию
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2. Распаковка параметров:
values_list = [458, 'вода', False]
values_dict = {'a': 500, 'b': 'стол', 'c': True}
print_params(*values_list)
print_params(**values_dict)
# Одновременно передать values_list и values_dict в функцию print_params невозможно,
# не изменив количество элементов.

# 3. Распаковка + отдельные параметры:
values_list_2 = [3.14, 'ноутбук']
print_params(*values_list_2, 42)

