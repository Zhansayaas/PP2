import re
pattern = r'([a-z])([A-Z])'

s1 = "ZhansayaKarboz"

s2 = re.sub(pattern, r'\1 \2', s1)

print(s2)