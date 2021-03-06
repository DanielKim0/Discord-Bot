import os
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def add_quotes(string):
    if string[0] != "\"" and string[-1] != "\"":
        return "\"" + string + "\""
    else:
        return string

def transpose(data):
    return list(map(list, zip(*data)))

def convert_to_date(string):
    return dt.strptime(string, "%Y.%m.%d")

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def calculate_age(birth_date):
    return str(relativedelta(START_DATE, convert_to_date(birth_date)).years)

def add_plural(key, value, data):
    data[key] = value
    data[key + "s"] = value

START_DATE = convert_to_date("1444.11.11")