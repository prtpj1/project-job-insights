from functools import lru_cache
import csv


@lru_cache
def read(path):
    employees_list = []
    with open(path, encoding="utf-8") as file:
        content = csv.DictReader(file)

        for row in content:
            employees_list.append(row)
    return employees_list
