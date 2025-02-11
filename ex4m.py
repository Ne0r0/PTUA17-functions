# Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.

# Pavyzdys:

# Skaičiai nuo 1 iki 1000, kurie dalijasi iš 6: [6, 12, 18, ..., 996]

from typing import List

def new_list(int_list: List[int]) -> List[int]:
    return [number for number in range(1, 1001) if number % 6 == 0]
result = new_list([])
print(f"Skaičiai nuo 1 iki 1000, kurie dalijasi iš 6: {result}")


# int_list = [number for number in range(1, 1001) if number % 6 == 0]
# print(f"Skaičiai nuo 1 iki 1000, kurie dalijasi iš 6: {int_list}")

# int_list = []
# for number in range(1, 1001):
#     if number % 6 == 0: # Tikrinu, ar skaičius dalijasi iš 6 be liekanos
#         int_list.append(number)

# print(int_list)
