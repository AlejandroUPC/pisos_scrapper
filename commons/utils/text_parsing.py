import re


def extract_numbers(str_data):
    numeric_data = __remove_special_chars(str_data)
    numeric_data = re.match(r'[0-9]*', numeric_data)
    if numeric_data:
        return numeric_data[0]
    else:
        return None


def __remove_special_chars(str_data):
    special_chars = [':']
    for item in special_chars:
        str_data = str_data.replace(item, '')
    return str_data.strip()
