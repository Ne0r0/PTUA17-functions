# Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 1000, kuriuose yra skaitmuo 9.

# Pavyzdys:

# Skaičiai nuo 1 iki 1000, kuriuose yra 9: [9, 19, 29, ..., 999]

from typing import List

def num_nine_list(int_list: List[int]) -> List[int]:
    return [num for num in range(1, 1001) if "9" in str(num)]
result = num_nine_list([])
print(f"Skaičiai nuo 1 iki 1000, kuriuose yra 9: {result}")


# Neteisingas
# for num in range(1, 1001):
#     the_list.append(num)
#     if 9 in the_list:
#         int_list = [num for num in the_list if num <=9]
# print(int_list)
