# 1

# my_list = ["Це", "просто", "кількість", "книг", "6", "11"]

# result = []
# name = 'number of books'
# for index in range(len(my_list)):
#   if index % 4:
#       result.append(my_list[index][::-1])
#    else:
#        result.append(my_list[index])
#        return result, name

# print(reserve_second_value(["Це", "просто", "кількість", "книг", "6", "11"]))



# my_list_2 = ["Це", "просто", "кількість", "книг", "6", "11"]
# example = [2, 3, 4, 5, 7]
# first, second, *other = example
# first, second, other = example
# print(first, second, other, sep=' !!!! ')

# result_2 = [my_list_2[index][::-1] if index % 2 else my_list_2_[index] for index in range(len(my_list_2))]

# test = [1, 3, 5, 4, 4, 4, 4, 7, 6, 5, 4, 2, 2, 2,]
# print(set(test))
# print(max(set(test), key=test.count))

# 2

# list_of_names = ["Artemis", "Agnesa", "Agata", "Adam"]
# name = []

# for name in my_list:
#    if name.lower().starswith("a"):
#        names.append(name)
# print(*name)

# my_names = [name for name in list_of_names if name.lower().starswith("a")]
# print(*my_names)

# my_list = ["anatomy", "data", "car", "rat", "nature"]
# name = []
# for name in my_list:
#    if 'A' in name.upper():
#        names.append(name)

# print(*names)


# 3

# my_list = [2, 2, 2, 2, 3, 4, 4, 4, 5, 5, "55", "32"]

# print(set(my_list))
# my_list.insert(0, "OBJECT")
# print(my_list[::])
# result = []
# for element in my_list:
#    if type(element) == str:
#        result.append(element)
# print(result)

# 4

# def creating_list_only_str_values(some_list: list) -> list:
#    result_list = [value for value in some_list if(type) is str]
#    return result_list

# my_list = ['puma', 39, 54, 'rebort', '-43', '111']
# new_list = creating_list_only_str_values(my_list)

# 5

# def create_unique_symbols_from_str(some_str: str) -> str:
#    result_list = [char for char in set (some_str) if some_str.count(char) == 1]
#    return result_list

# my_str = [ 'seen' 1, 'names', 2, 'fake']
# new_str = create_unique_symbols_from_str(my_str)

# 6

# def create_list_with_common_two_str(some_str_1: str, some_str_2: str) -> list:
#    result_list = list(set(some_str_1) & set(some_str_2))

#    return result_list

# my_str_1 = '2255reduce"
# my_str_2 = '2255reduce"

# new_list = create_list_with_common_two_str(my_str_1, my_str_2)

# 7

# def create_list_with_same_symbol_2_str(some_str_1: str, some_str_2: str) -> list:
#    result_list = [char for char in set (str_2) if str_1.count(char) == str_2.count(char) == 1]

#    return result_list

# my_str_1 = '2255reduce34443432"
# my_str_2 = '5432232kttreewwewe"

# new_list = create_list_with_same_symbol_2_str(my_str_1, my_str_2)

# 8

from random import randint
from random import choice
from string import ascii_lowercase

def create_email(names_list: domains_list: list) -> str:
    name = choice(names_list)
    domain = choice(domains_list)
    name_after_cat = ''

for _ in range(randint(6, 9)):
    name_after_cat += choice(ascii_lowercase)

res = es = name + '.' + str(randint(100, 999)) + '@' + name_after_dog + '.' + domain

    return res


names = ['nata', 'maya', 'lara', 'artem', 'adraey']
domains = ['net', 'com', 'ua', 'us', 'jpg']
e_mail = create_email(names, domains)