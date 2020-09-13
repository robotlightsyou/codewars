import string
import random


def gen1():
    alpha = string.ascii_lowercase + string.ascii_uppercase
    name = "ABCDEF"
    while photoManager.nameExists(name) == True:
        name = "".join(random.choice(alpha) for i in range(6))
    return name


def gen2():
    alpha = string.ascii_lowercase + string.ascii_uppercase

    def new_name(letters):
        return "".join(random.choice(letters) for i in range(6))
    name = "ABCDEF"
    while photoManager.nameExists(name) == True:
        name = new_name(alpha)
    return name


if __name__ == "__main__":
    import timeit
    print('test1 = ' + str(timeit.timeit(
        stmt='gen1()', setup='from __main__ import gen1', number=10000)))
    print('test2 = ' + str(timeit.timeit(
        stmt='gen2()', setup='from __main__ import gen2', number=10000)))
    # print('test3 = ' + str(timeit.timeit(
    #     stmt='best([12, 10, 8, 12, 7, 6, 4, 10, 10])', setup='from __main__ import best', number=10000)))
    # print('test4 = ' + str(timeit.timeit(
    #     stmt='better([12, 10, 8, 12, 7, 6, 4, 10, 10])', setup='from __main__ import better', number=10000)))


##################
# broken heroes of magic: 1v1
##############
"""
def who_would_win(mon1, mon2):
    mon1_total = mon1["number"] * mon1["hitpoints"]
    mon2_total = mon2["number"] * mon2["hitpoints"]

    cur_mon1 = mon1["hitpoints"]
    cur_mon2 = mon2["hitpoints"]

    while mon1_total > 0:
        attack1 = mon1["number"] * mon1["damage"]
        mon2_total -= attack1
        if mon2_total <= 0:
            return "{number} {type}(s) won".format(**mon1)
        else:
            if attack1 > cur_mon2:
                mon2["number"] -= 1
                attack1 -= cur_mon2
                cur_mon2 = mon2["hitpoints"]
                cur_mon2 -= attack1
            else:
                cur_mon2 -= attack1

        ########

        attack2 = mon2["number"] * mon2["damage"]
        mon1_total -= attack2
        if mon1_total <= 0:
            return "{number} {type}(s) won".format(**mon2)
        else:
            if attack2 > cur_mon1:
                mon1["number"] -= 1
                attack2 -= cur_mon2
                cur_mon1 = mon1["hitpoints"]
                cur_mon1 -= attack2
            else:
                cur_mon1 -= attack2
"""
