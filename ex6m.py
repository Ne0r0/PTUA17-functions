# Parašykite programą, kuri pagal gautą tekstinę įvestį suskaičiuotų, kiek žodžių turi „e“ raidę.

# Pavyzdys:

# Įveskite tekstą: Šioje paskaitoje aptarsime papildomas Python integruotų duomenų struktūrų funkcijas.
# Žodžių su 'e' skaičius: 5

from typing import List, Union

def word_with_e(text: List[str | int]) -> List[str | int]:
    return len([word for word in user_input.split() if 'e' in word])

user_input = input("Įveskite tekstą: ")
words_count = word_with_e(user_input)
print(f"Žodžių su 'e' skaičius: {words_count}")


# user_input = input("Įveskite tekstą: ")
# words_with_e = [word for word in user_input.split() if 'e' in word]
# print(f"Žodžių su 'e' skaičius: {len(words_with_e)}")


# user_input = input("Įveskite tekstą: ")

# words = user_input.split()

# count = sum(1 for word in words if 'e' in word)

# print(f"Žodžių su 'e' skaičius: {count}")
