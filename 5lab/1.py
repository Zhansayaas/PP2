import re
pattern = r'a{1}b*' 
string = ['ab', 'acb', 'abb', 'abbb', 'acbb', 'a', 'abc', 'aaab']
for s in string:
    if re.search(pattern, s):
        print(f"'{s}' matches the pattern")
    else:
        print(f"'{s}' does not match the pattern")