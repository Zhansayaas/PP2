#1
def square_gen(N):
    for i in range(1, N+1): 
        yield i**2
for x in square_gen(5):
    print(x)
#2
def even_num_gen(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a value for n: "))
even_numbers = even_num_gen(n)
print(','.join(map(str, even_numbers))) 
#3
def div_by_3_and_4_gen(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a value for n: "))
div_numbers = div_by_3_and_4_gen(n)
print(','.join(map(str, div_numbers)))
#4
def squares_gen(a, b):
    for i in range(a, b+1):
        yield i**2
for square in squares_gen(1, 5):
    print(square)
#5
def countdown(n):
    while n >= 0:
        yield n
        n = n - 1
for i in countdown(5):
    print(i)   