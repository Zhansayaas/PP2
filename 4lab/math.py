#1
import math
x = int(input())
print((x * math.pi) / 180)
#2
def trap(a, b, h):
    A = ((a + b) * h) / 2
    return A
x = int(input("Input 1st base: "))
y = int(input("Input 2nd base: "))
z = int(input("Input height: "))
print(trap(x, y, z))
#3
import math
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
a = (n * l**2) / (4 * math.tan(math.pi / n))
print(a)
#4
a = int(input("Input the length: "))
b = int(input("Input the height: "))
print(a * b)