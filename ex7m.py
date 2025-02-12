# from typing import List
# 1) Create a lambda function that takes a number and returns its square.

# def square(num_1):
#     return num_1 ** 2
# print(square(5))

square = lambda x: x ** 2
print(square (4))


# 2) Create a lambda function that takes two numbers and returns their squared sum.

two_int = lambda x, y: (x + y) ** 2
print(two_int(3, 4))


# 3) Use the lambda function to sort list of tuples based on the second element:
# tuples_list = [(1,3), (4,1), (5,2), (2,4)]

tuples_list = [(1,3), (4,1), (5,2), (2,4)]
tuples_list.sort(key=lambda x: x[1])
print(tuples_list)

# sort(key=lambda x: x[1]): Sorts the list of tuples (tuples_list)
# based on the second element of each tuple (i.e., the marks). 
# It uses a lambda function as the sorting key, 
# which extracts the second element (x[1]) for sorting purposes


# 4) Use lambda functions to sort list of strings by their length and then alphabetically.
# words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'acid']
words.sort(key=lambda x: (len(x), x))
print(words)


# 5) Create a function that filters a series of strings and 
# returns a new list containing only those that start with a vowel.
# Example call and result:
# start_with_vowel("apple", "banana", "orange") ➞ ["apple", "orange"]

start_with_vowel = ["apple", "banana", "orange"]
vowel = []
for vowels in start_with_vowel:
    if vowels [0] in "aeiou":
        vowel.append(vowels)
print(vowel)


start_with_vowel = ["apple", "banana", "orange"]
vowel = [vowels for vowels in start_with_vowel if vowels[0] in "aeiou"]
print(vowel)


def start_with_vowel(*vowel):
    return list(filter(lambda x: x[0].lower() in "aeiou", vowel))
result = start_with_vowel("apple", "banana", "orange")
print(result)

# Jeigu parašai be '*' 
# TypeError: start_with_vowel() takes 1 positional argument but 3 were given
