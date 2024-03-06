# #1
# gram= int(input("Gram: "))
# def convertToGrams(grams):
#   ounces = 28.3495231 * grams
#   print(ounces)
# convertToGrams(5)
# #2
# F = int(input("Fahrenheit temperature : "))
# def convertTemperature(F):
#   C = (F-32)*(5/9)
#   print(C)
# convertTemperature(200)
# convertTemperature(F)
# #3
# def solve(numheads, numlegs):
#   chicken=(-numlegs+4*numheads)/2
#   rabbit=numheads-chicken
#   print(chicken,rabbit)
# solve(35,94)
# #4
# def filterPrime(num):
#     if(num == 1):
#         return False
#     for i in range(2, num):
#         if(num % i == 0):
#             return False
#     return True
# list = [12,3,4,90,10]

# print([x for x in list if filterPrime(x)])
#5
# from itertools import permutations
# def print_permutations():
#       s = input("String : ")
#       perm = permutations(s)
#       for i in list(perm):
#                   print(''.join(i))
# print_permutations()
# #6
# def reverseTxt(s):
#     reversed_s = " ".join(reversed(s.split()))
#     print(reversed_s)
# s = str(input())
# reverseTxt(s)

# #7
# def has_33(nums):
#     for i in range(0,len(nums)-1):
#         if(nums[i] == nums[i+1] == 3):
#             print("True")
#             return True
#     print("False")
#     return False

# has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# has_33([3,  1, 3])

# #8
# def spy_game(nums):
#     for i in range(0, len(nums)):
#         if(nums[i] == 0):
#             for j in range(i, len(nums)):
#                 if(nums[j] == 0):
#                     for k in range(j, len(nums)):
#                         if(nums[k] == 7):
#                             print("True")
#                             return True
#     print("False")
#     return False

# spy_game([1,2,4,0,0,7,5])
# spy_game([1,0,2,4,0,5,7])
# spy_game([1,7,2,0,4,5,0])

#9
def volumeSphere():
     r=int(input())
     volume=3/4*3.14*pow(r,3)
     print(volume)
volumeSphere()
#10
def unique(input_list):
    unique_list = []
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

list1 = input().split()
print(unique(list1))
#11
def isPalindrom(word):
    reversed_word = word[::-1]
    if(reversed_word == word):
        print("Palindrom")
    else:
        print("Not palindrom")
s = input()
isPalindrom(s)
#12
def histogram(seq):
    for i in seq:
        print("*" * i)

s = [1,2,3,4,5]
histogram(s)
#13
import random

def guessTheNumber():
    random_number = random.randint(1, 20)
    print("Hello! What is your name?")
    name = str(input())
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    attempts = 0
    while True:
        num = int(input())
        attempts += 1
        if(num < random_number):
            print("Your guess is too low. \nTake a guess.")
        elif(num > random_number):
            print("Your guess is too high. \nTake a guess.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

guessTheNumber()
