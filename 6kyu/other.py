# hello.py
# name = input("What is your name?\n")
# print(f"hello, {name}")

# mario less
# from cs50 import get_int

# while True:
#     height = get_int("Height: ")
#     if 0 < height <= 8:
#         print("\n".join([((" " * (height - i)) + ('#' * i))
#                          for i in range(1, height + 1)]))
#         break

# # mario more
# from cs50 import get_int

# while True:
#     height = get_int("Height: ")
#     if 0 < height <= 8:
#         for i in range(1, height + 1):
#             hsh = "#" * i
#             space = " " * (height - i)
#             print(space + hsh + "  " + hsh)
#         break

# Cash
# from cs50 import get_float


# def main():
#     owed = 0
#     while owed < 1:
#         owed = int(get_float("How much change is owed? ") * 100)
#     coins = 0
#     coins += owed // 25
#     owed %= 25
#     coins += owed // 10
#     owed %= 10
#     coins += owed // 5
#     owed %= 5
#     coins += owed
#     print(coins)


# if __name__ == '__main__':
#     main()


# credit.py

# from cs50 import get_int


# def main():

#     # ask user for input
#     credit = get_int("What is your credit card number? ")
#     if not is_length(cc=credit):
#         print("INVALID")
#         return 0

#     # luhn the digits
#     if not is_luhn(lcc=credit):
#         print("INVALID")
#         return 0

#     # if luhn check company
#     else:
#         print_name(ncc=credit)
#     # print company name


# def is_length(cc=0):
#     return len(str(cc)) in [13, 15, 16]


# def is_luhn(lcc=0):
#     odds = 0
#     evens = lcc % 10
#     lcc //= 10
#     while lcc > 0:

#         odds += get_odds(lcc)

#         # remove a digit
#         lcc //= 10

#         # evens digit
#         if lcc > 0:
#             evens += lcc % 10
#             lcc //= 10

#     total = odds + evens
#     return total % 10 == 0


# def print_name(ncc=0):
#     length = len(str(ncc))
#     two = str(ncc)[0:2]
#     one = str(ncc)[0]
#     if (length == 16 or length == 13) and one == '4':
#         print("VISA")
#     elif length == 15 and two in ["37", "34"]:
#         print("AMEX")
#     elif length == 16 and two in ["51", "52", "53", "54", "55"]:
#         print("MASTERCARD")


# def get_odds(cc=0):
#     # odds digit place
#     n = (cc % 10) * 2
#     n = n if n < 10 else ((n//10) + (n % 10))
#     return n


# read.py
from cs50 import get_string
# from string import punctuation as punc

def main():
    pass
    # get string from user
    text = get_string("Text: ")

    # get total letters, words, and sentences.
    letter, word, sentence = counts(string = text)

    # calculate avg wors per 100 words
    L = get_avg(letter, word)

    # calculate avg sentence per 100 words
    S = get_avg(sentence, word)

    # find grade using:
    # grade = 0.0588 * L - 0.296 * s - 15.8
    grade = round((0.0588 * L) - (0.296 * S) -15.8)

    # print grade
    # print(f"L {L}")
    # print(f"S {S}")
    # print(f"grade {grade}")
    print(print__grade(grade))

def counts(string = ''):
    letters = 0
    words = 1
    sentences = 0
    for i in string:
        if i.isalpha():
            letters += 1
        elif i.isspace():
            words += 1
        elif i in ["!", ".", "?"]:
            sentences += 1
    return letters, words, sentences

def get_avg(item = 0, outof = 0):
    if outof < 100:
        mult = 100 / outof
        return item * mult
    else:
        divisor = outof / 100
        return item // divisor

def print__grade(score = 0):
    if score <= 0:
        return "Before Grade 1"
    elif score >= 16:
        return "Grade 16+"
    else:
        return f"Grade {score}"

# def avg_sentences(words = 0, sentences = 0):
#     if words < 100:
#         mult = 100 / words
#         return sentences * mult

if __name__ == '__main__':
    main()


