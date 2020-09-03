while True:

    print("Height: ", end="")

    n = int(input("please enter an int"))

    if n <= 23 and n > 0:

        break

    for i in range(n):

        print(' ' * (n-1-i), end="")

        print('#' * (i+2))
