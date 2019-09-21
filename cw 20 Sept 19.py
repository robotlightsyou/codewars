# 6 kyu

# #Find the missing letter

# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# (Use the English alphabet with 26 letters!)

# Have fun coding it and please don't forget to vote and rank this kata! :-)

# I have also created other katas. Take a look if you enjoyed this kata!

import string


def find_missing_letter(chars):
    if chars[0].isupper():
        alpha = string.ascii_uppercase
    else:
        alpha = string.ascii_lowercase
    x = alpha.index(chars[0])
    for i in range(len(chars)):
        if alpha.index(chars[i]) != x + i:
            return alpha[(alpha.index(chars[i-1]))+1]
#             prev = alpha.index(chars[i-1])
#             return alpha[prev + 1]


# 7 kyu
# Sum of odd numbers
# Python:
def row_sum_odd_numbers(n):
    x = 1
    for i in range(1, n):
        x += 2 * i
    counter = 0
    result = 0
    for i in range(n):
        result += x + counter
        counter += 2
    return result
