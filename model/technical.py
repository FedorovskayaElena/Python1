import re


# перед сравнением строк удаляем лишние пробелы в середине, в начале и в конце
def clear_extra_spaces(s):
    return re.sub(" +", " ", s.strip())