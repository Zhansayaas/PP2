import re

pattern = r'([a-z])([A-Z])'

s1 = "ThisIsCamelCaseString"

s2= re.sub(pattern, r'\1_\2', s1).lower()
print(s2)