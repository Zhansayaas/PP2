import re

s1 = "Hello,it is replacing all occurrences of space, comma, or dot with a colon"

s2 = re.sub(r'[ ,.]+', ':', s1)

print(s2)