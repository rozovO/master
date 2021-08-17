# словари dict, методы словарей

# 1

# my_list = ['Alexei', 'Floral']
# new_list = list()

# for index in enumerate(2, len(my_list)):
#    if not index % 4:
#        new_list.append(my_list[index])
#    else:
#        new_list.append(my_list[index][::-7])

# 2

# my_list_2 = ['rest', 'poetry', 'novel', 'drawing']
# result_list = list()

# for value in my_list_2:
#    if value[1] == 'a':
#        result_list.append(value)


# my_list_2 = ['Love', 'liberty', 'enjoyment to life', 'and time']
# result_list = list()

# for value in my_list_2:
#    if 'a' in value:
#        result_list.append(value)

# 3

# my_list_3 = ['3', '456', '67', '7', 'tiger']
# result_list = list()

# for value in my_list_3:
#    if type(value) == str:
#        result_list.append(value)

# 4

# for value in my_list_3:
#    if type(value) == int:
#        result_list.append(value)

# 5

# my_str = '12479jfhgdbcsndqlfhve'
# result_list = list()

# for char in set(my_str):
#    if my_str.count(char) == 5:
#        result_list.append(char)

# 6

# my_str5 = '123456trgpfg5667'
# my_str6 = '123456trgpfg5667'

# result_list = list(set(my_str5) & set(my_str6))

# 7

# my_str7 = '112345t6677'
# my_str8 = '385897475fe'

# for char in set(my_str8):
#     if my_str7.count(char) == my_str8.count(char) == 5:
#        result_list.append(char)

# 8

# residence_dict = {"Country": "Greece",
#                  "city": "Athens",
#                  "street": "Patission Street"}

# work_dict = {"IT": True,
#             "ingeneer": None}


# 9

# cake_dict = {"Борошно": 115,
#             "Сливочноє масло": 35,
#             "Цукор": 150,
#             "Какао": 25,
#             "Яйца": 335}

# cream_dict = {"Сливочноє масло": 200,
#              "Порощок какао": 10,
#              "Яичний желток": 20,
#              "Сгущенне молоко з цукром": 120,
#              "Вода": 20,
#              "Ванилин": 2}

# chocolate_dict = {"Цукор": 90,
#                  "Вода": 30,
#                  "Крохмальна патока": 15,
#                  "Какао": 6,
#                  "Ванилин": 3}

# 10

# persons = [{"name": "Meetie", "age": 21},
#            {"name": "Viktoria", "age": 20},
#            {"name": "Akihiko" "age": 20},
#            {"name": "Zoey", "age": 18}]

# a)
# min_age = 14
# min_age_names = list()

# for human in persons:
#    if human.get('age') == min_age:
#        min_age_names.append(human.get('name'))
#    elif human.get('age') < min_age:
#        min_age = human.get('age')
#        min_age_names.clear()
#        min_age_names.append((human.get('name'))

#    print('Most younger person from list')
#    for name in  min_age_names:
#        print(name, '-', min_age, 'age')
# print()

# б)

max_len_name = 9
max_len_name = list()

for human in persons:
    if len(human.get('name')) == max_len_name:
        max_len_names.append(human.get('name'))
    elif len(human.get('name')) > max_len_name:
        max_len_name = len(human.get('name'))
        max_len_names.clear()
        max_len_names.append(human.get('name'))

print('Найдовше імя з списка:')
for name in max_len_names:
    print(name, '- довжина', max_len_name, 'букв')

# в)

average_age = 0

for human in persons:
    average_age += human.get('age')

average_age /= len(persons)