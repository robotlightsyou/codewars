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
from cs50 import get_float


def main():
    owed = 0
    while owed < 1:
        owed = int(get_float("How much change is owed? ") * 100)
    coins = 0
    coins += owed // 25
    owed %= 25
    coins += owed // 10
    owed %= 10
    coins += owed // 5
    owed %= 5
    coins += owed
    print(coins)


if __name__ == '__main__':
    main()
