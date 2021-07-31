# Булевий тип данних
my_bool_1 = True
print('my_bool_1: ', my_bool_1)
print('type(my_bool_1): ', type(my_bool_1))

my_bool_2 = 2 == 3
print('my_bool_2: ', my_bool_2)
print('type(my_bool_2): ', type(my_bool_2))

my_bool_3 = 10 >= 14
print('my value: ', my_bool_3)
print('type(my_bool_3): ', type(my_bool_3))

my_bool_4 = 10 == 10
print('my_bool_4: ', my_bool_4)
print('type(my_bool_4): ', type(my_bool_4))

my_bool_5 = 19.9 != 19
print('my_bool_5: ', my_bool_5)
print('type(my_bool_5): ', type(my_bool_5))

my_bool = 15 == 22
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))

my_bool = 155 != 155
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))

my_bool = 16 > 16
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))

my_bool = 5 >= 7
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))

my_bool = 90 >= 90
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))

my_bool = 46 >= 67
print('my_bool: ', my_bool)
new_bool = not my_bool
print('new_bool: ', new_bool)
print('type(new_bool): ', type(new_bool))

my_bool = 21 >= 22
print('my_bool: ', my_bool)
new_bool = not my_bool
print('new_bool: ', new_bool)
print('type(new_bool): ', type(new_bool))

my_int = 5
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))
print('type(bool(my_int)): ', type(bool(my_int)))

my_int = -23
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))

my_int = 0
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))

list_ = [2, 8, 0, 8]
print('len(list_): ', len(list_))
if len(list_):
     print('список має значення')
else:
     print('список не має значення')

list_ = []
print('len(list_): ', len(list_))
if list_:
     print('список має значення')
else:
     print('список не має значення')


my_int = -6.9
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))

my_int = 0.
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))

# Зміна точності
my_int = 0.00000000000000000000000000
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))
print(len('00000000000000000000000000'))

val_1 = 24.578
val_2 = 24.578
print(val_1==val_2)
print(abs(val_1 - val_2) < 0.00001)

my_str = 'my string'
print('bool(my_str): ', bool(my_str))

my_str = ''
print('len(my_str): ', len(my_str))
print('bool(my_str): ', bool(my_str))

my_str = ' '
print('len(my_str): ', len(my_str))
print('bool(my_str): ', bool(my_str))

my_none = None
print('bool(my_none): ', bool(my_none))

my_str = 'True'
print('my_str: ', my_str)
print('type(my_str): ', type(my_str))
print('bool(my_str): ', bool(my_str))

my_bool = True
print('my_bool: ', my_bool)

my_int = int(my_bool)
print('my_int: ', my_int)
print('type(my_int): ', type(my_int))

my_str = str(my_bool)
print('my_str: ', my_str)
print('type(my_str): ', type(my_str))

my_str = 'False'
print('bool(my_str): ', bool(my_str))

my_bool = False
print('my_bool: ', my_bool)

my_int = int(my_bool)
print('my_int: ', my_int)
print('type(my_int): ', type(my_int))

my_str = str(my_bool)
print('my_str: ', my_str)
print('type(my_str): ', type(my_str))
print('bool(my_str): ', bool(my_str))
print('type(my_str): ', type(my_str))

my_val = None
print('bool(my_val): ', bool(my_val))

my_val = 'NotImplemented'
print('bool(my_val): ', bool(my_val))

my_val = Ellipsis
print('bool(my_val): ', bool(my_val))
