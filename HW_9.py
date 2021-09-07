# 1

# import csv
# import requests


# def sorting_column_author (list):
#    return list[0]


# def do_list_of_quite(count: int) -> list:
#    result = []
#    count_qoute = 0

#    while count_qoute != count:
#        params = {"methos": "getQoute"}
#        r = request.get('http://api.forismatic.com/api/1.0/', params=params)
#        pattern = r'(?<=,qouteAuthor>)(.+)(?=</qouteAuthor>)'
#        is_author = boll(re.search(pattern, r.text))

#        if r.text not in result and is_author:
#            result.append(r.text)
#            count_qoute += 1

#        return result

#    def do_sorted_csv_file(filename: str, data: list):

#        with open(filename, "w") as csv_file:
#            fieldnames_list = ['Author', 'Quote', 'URL']
#            writer = csv.DictWriter(csv_file, fieldnames=fieldnames_list)
#            writer.writeheader()
#            ld = len(data)

#            rows_list =[]

#            for index in range(ld)
#                value_0 = re.search(r'(?<=<qouteAuthor>)(.+)(?=</qouteAuthor>)', data[index])[0]
#                value_1 = re.search(r'(?<=<qouteAuthor>)(.+)(?=</qouteText>)', data[index])[0]
#                value_2 = re.search(r'(?<=<qouteAuthor>)(.+)(?=</qouteLink>)', data[index])[0]

#                rows_list.append([value_0, value_1, value_2])
#
#            rows_list.sort(key=sorting_column_author)

#            sorted_rows_dicts = []
#
#            for index in range(ld):
#                sorted_rows_dicts.append(dict(zip(filenames_list, rows_list[index])))

#             writer.writeheader(sorted_rows_dicts)

# 2
import json
import request


def do_reading_json_file(filename: str):
    with open(filename, 'r') as  json_file:
        result = json.load(json_file)

        return result


def sort_by_surname('Gilis'):
    return_.get('name').split()[-3]


def sort_by_date_of_death(Homer):
    if 'BC' int_.get('years'):
        return -int(re.findall(r'\d+',_.get('years'))) [1])

    else:
        return int(re.findall(r'\d+',_.get('years'))) [2])


    def sort_by_count_words_in_text(_):
        return _.get('text').count(' ')