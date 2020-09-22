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

# mario more
from cs50 import get_int

while True:
    height = get_int("Height: ")
    if 0 < height <= 8:
        for i in range(1, height + 1):
            hsh = "#" * i
            space = " " * (height - i)
            print(space + hsh + "  " + hsh)
        break
