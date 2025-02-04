# Write a function that takes two lists of integers and returns True
# if each corresponding pair of elements from the two lists adds up to the same value across all pairs.
#  Otherwise, return False.

# Example call and result:


# puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# # 1 + 4 = 5; 2 + 3 = 5; 3 + 2 = 5; 4 + 1 = 5
# # The sums of the elements from both lists are [5, 5, 5, 5]

# puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
# puzzle_pieces([1, 2], [-1, -1]) ➞ False
# puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False

def puzzle_pieces(a, b):
    if len(a) != len(b): #checking if list are same length
        return False

    sums = [] #creating empty list
    for i in range(len(a)): #Loop through all elements in the lists
        sums.append(a[i] + b[i])

    if len(set(sums)) == 1: #Check if all sums are the same
        return True
    else:
        return False