import re


def extract_numbers(str_data):
    """
        Given a string, extracts only the numbers.
    """
    numeric_data = __remove_special_chars(str_data, [':'])
    numeric_data = re.match(r'[0-9]*', numeric_data)
    if numeric_data:
        return numeric_data[0]
    else:
        return None


def extract_text(str_data):
    """
        Prepares a list with characters to be removed from a string.
    """
    str_data = __remove_special_chars(str_data, [':', '`'])
    return str_data.strip()


def __remove_special_chars(str_data, special_chars):
    """
         Removes spaces and special characters given a list.
    """
    for item in special_chars:
        str_data = str_data.replace(item, '')
    return str_data.strip()
