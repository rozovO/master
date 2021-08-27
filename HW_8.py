# 1

# def get_domain(filename):
#    """
#    Функція повертає назви інтернет доменов
#    :param filename: строка с именем файла
#    :return: список
#    """
#    try:
#        with open(filename, "r") as file:
#            return [line.strip()[1:] for line in file.readlines()]
#    except FileNotFoundError as error:
#        return f"this is (error)"


# print(get_domain("next/domain.txt"))

# 2


# def get_names(filename):
#    result = []
#    with open(filename, "r") as file:
#        for line in file.readlines():
#            result.append(line.split('\t')[1])
#    return result
#    with oprn(filename, "r") as file:
#        return [line.split("\t")[1] for line in file.readlines()]


#    print(get_names('names.txt'))


# 3


from datetime import datetime

my_month = datetime.strptime("February", "%B").month

date = "26th Feb 1802"
day, month, year = date.split()
res_date = f"{day[:-2]} {month} {year}"
my_date = datetime.strptime(res_date, "%d %b %Y")
my_date = datetime.strftime(my_date, "%d/%m/%Y")


def get_only_dates(filename):
    """
    :param filename:
    :return:
    """
    result = []
    with open(filename, "r") as file:
        for line in file.readlines():
            my_line = line.split(" - ")
            if len(my_line) > 1:
                date = my_line[0]
                day, month, year = date.split()
                my_date = datetime.strptime(f"{day[:-2]} {month} {year}", "%d %B %Y")
                result.append(
                    {
                        "date_original": date,
                        "date_modified": datetime.strftime(my_date, "%d/%m/%Y"),
                    }
                )
    return result


print(get_only_dates("authors.txt"))