my_dict = {'Кирилл': 1996, 'Роза': 1998, 'Дмитрий': 2005, 'Андрей': 2004, 'Света': 2007}
print('Словарь:', my_dict)
print('Год рождения Роза:', my_dict['Роза'])
print('Год рождения Степа:', my_dict.get('Степа', 'нет такого ключа'))
my_dict.update({'Александр': 1997, 'Клеопатра': 2001})
removed_year = my_dict.pop('Клеопатра')
print('Значение удалённого элемента \'Клеопатра\':', removed_year)
print('Изменённый словарь:', my_dict)

print()

my_set = {2, 3, 3, 2, 5, True, True, False, True, 'list', 'set', 'list', 'list'}
print('Множество:', my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
print('Изменённое множество:', my_set)
