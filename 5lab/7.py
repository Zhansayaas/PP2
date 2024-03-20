import re

pattern = r'_([a-z])'

s1 = "This_is_snake_case_string"

s2 = re.sub(pattern, r'\1'.upper(), s1.title().replace('_', ''))

print(s2)