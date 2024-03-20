import re
pattern = r'[a-z]+_[a-z]+'
string = 'hello_world'

match = re.findall(pattern, string)

print(match)