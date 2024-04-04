#1
import math
list = [1,4,5,6,4,3]
print(math.prod(list))
#2
text = str(input())
low, up = 0, 0
for char in text:
    if(char.islower()):
        low += 1
    else:
        up +=1

print(low, up)
#3
text = str(input())
reversedText = ''.join(reversed(text))
if(reversedText == text):
    print("is palindrom")
else:
    print("not palindrom")
#4
import time
def my(num, miliseconds):
    time.sleep(miliseconds / 1000) # make a pause before running program
    # for a some amount of time
    result = math.sqrt(num)
    return result

num = int(input())
miliseconds = int(input())
output = my(num, miliseconds)
print(f"Square root of {num} after {miliseconds} miliseconds is", output)
#5
Tuple = (True, True, True)
if(all(Tuple)):
    print("Yes,", all(Tuple))
else:
    print("No")