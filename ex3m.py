# You have a list of ten random words which starts with letters A, C, or P.
# Write a function that takes a list of the word_list and prints new list 
# with all words that starts with letter P.

from typing import List

word_list = ["Adventure", "Cascade", "Paradox", "Astonish", "Crimson", "Pioneer", "Ambition", "Chandelier", "Prosper", "Courage"]

# def filter_words_by_p(word_list: List[str]) -> List[str]:
#     check = "P"
#     word_p_list = []
#     for word in word_list:
#         if word[0] == check: 
#             word_p_list.append(word)
#     print(word_p_list)
# filter_words_by_p(word_list)

def extract_specific_words(word_list: List[str]) -> List[str]:
    return [name for name in word_list if name.upper().startswith('P')]
result = extract_specific_words(word_list)
print(result)

# from typing import List
# word_list = ['Apple', 'Car', 'Proud', 'Apricot', 'Plank', 'Calk', 'Alphabet', 'Cork', 'August', 'Plain', 'peach']

# def starts_with_p(word_list: List[str]) -> List[str]:
#     p_words: List[str] = []
#     for word in word_list:
#         if word.upper().startswith('P'):
#             p_words.append(word)
#     return p_words
# print(starts_with_p(word_list))
