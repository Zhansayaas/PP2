# #1
class toUppercase():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter a string: ") #Get a string from console input.

    def printString(self):
        print(self.str.upper()) #Print the string in upper case.

test = toUppercase()
test.getString()
test.printString()
#2
class Shape():
    def __init__(self, length):
        self.length = length
    def area(self):
        print(0)
class Square(Shape):
    def area (self):
        print(self.length*self.length)
newShape=Shape(9)
b = Shape(newShape)
b.area()
b = Square(newShape)
b.area()
#3
class Shape():
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Shape):
    def area(self):
        print(self.length * self.width)

x = int(input())
y = int(input())
s = Rectangle(x, y)
s.area()
#4
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, end = " ")
        print(self.y)
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        print(self.x, end = " ")
        print(self.y)
    
    def dist(self, Point):
        print(abs(Point.x - self.x), end = " ")
        print(abs(Point.y - self.y))

p1 = Point(6, 8)
p2 = Point(5, 5)
p1.show()
p1.move(1, 1)
p1.dist(p2)
#5
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money
        if(self.balance < 0):
            print("You have not enough money")
        else:
            print(self.balance)

wallet = Account("Zhansaya", 50000)
wallet.deposit(5000)
wallet.withdraw(10000)
#6
def isPrime(num):
    if(num == 1):
        return False
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True

class List():
    def __init__(self, a):
        self.a = a
    def filtering(self):
        return list(filter(lambda num : isPrime(num), self.a))

myList = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(myList.filtering())
