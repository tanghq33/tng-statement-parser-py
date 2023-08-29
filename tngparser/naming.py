import re

def snake_case(value: str) -> str:
    value = value.lower()
    value = re.sub(r'[^\w]', ' ', value)
    value_split = re.split('[-_., ()/*&%$#^@!\\\\"]+', value.strip('-_. ()/*&%$#^@!'))
    return '_'.join(value_split)

def fix_spaces(value: str) -> str:
    values = value.split(' ')
    values = list(filter(None, values))
    return ' '.join(values)