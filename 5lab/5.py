import re
pattern = r'a.+b$' #. - any character
string = "Abba is ab"

match = re.search(pattern, string)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")