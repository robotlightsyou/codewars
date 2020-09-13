"""
Some new cashiers started to work at your restaurant.

They are good at taking orders, but they don't know how to capitalize words, or use a space bar!

All the orders they create look something like this:

"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

The kitchen staff are threatening to quit, because of how difficult it is to read the orders.

Their preference is to get the orders as a nice clean string with spaces and capitals like so:

"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

The kitchen staff expect the items to be in the same order as they appear in the menu.

The menu items are fairly simple, there is no overlap in the names of the items:

1. Burger
2. Fries
3. Chicken
4. Pizza
5. Sandwich
6. Onionrings
7. Milkshake
8. Coke
"""

# Python


def get_order(order):
    ansList = []
    menu = {"Burger": 0, "Fries": 0, "Chicken": 0, "Pizza": 0, "Sandwich": 0, "Onionrings": 0,
            "Milkshake": 0, "Coke": 0}
    for k, v in menu.items():
        v += order.count(k.lower())
        for i in range(v):
            ansList.append(k)
    return " ".join(ansList)


"""
5 kyu - Land Perimeter  **Curently not working**
Task:
Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1piece of land. Some examples for better visualization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']
"""


def land_perimeter(arr):
    #     for i,j in enumerate(arr):
    #         print(j + f" {i}")
    fences = 0
    # top row
    for i in range(len(arr[0])):
        if arr[0][i] == "X":
            fences += 4
            try:
                if len(arr[0]) > i + 1 and arr[0][i + 1] == 'X':
                    fences -= 1
                if arr[0][i-1] == "X":
                    fences -= 1
                if arr[1][i] == "X":
                    fences -= 1
            except IndexError:
                pass
    # middle rows
    for lst in range(1, len(arr[1:])):
        for i in range(len(arr[lst])):
            if arr[lst][i] == "X":
                fences += 4
                try:
                    # right
                    if len(arr[lst]) > i + 1 and arr[lst][i + 1] == 'X':
                        fences -= 1
                    # left
                    if arr[lst][i-1] == "X":
                        fences -= 1
                    # below
                    if arr[lst+1][i] == "X":
                        fences -= 1
                    # above
                    if arr[lst-1][i] == "X":
                        fences -= 1
                except IndexError:
                    pass
    # bottom row
    for i in range(len(arr[-1])):
        if arr[-1][i] == "X":
            fences += 4
            try:
                if len(arr[-1]) > i + 1 and arr[-1][i + 1] == 'X':
                    fences -= 1
                if arr[-1][i-1] == "X":
                    fences -= 1
                if arr[-2][i] == "X":
                    fences -= 1
            except IndexError:
                pass
    # return totals
    return ("Total land perimeter: %d" % (fences))
