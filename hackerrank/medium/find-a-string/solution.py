import re

def count_substring(string, sub_string):
    matches = re.findall(f'(?={sub_string})', string)
    return len(matches)

