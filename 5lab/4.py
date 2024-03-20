import re

pattern = r'[A-Z]{1}[a-z]+'

string = "Hello,World.Today is good"

sequence = re.findall(pattern, string)

print(sequence)