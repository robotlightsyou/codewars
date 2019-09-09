from string import ascii_lowercase
from operator import itemgetter

# get length of name
# add letters together
# multiply by weight

# find which name is rank n in names_num
from string import ascii_lowercase


def move_up(names_list, place, a):
    test1 = []
    for letter in names_list[place-1][0]:
        test1.append(a[letter])
    test2 = []
    for letter in names_list[place][0]:
        test2.append(a[letter])
    for i in range(len(test1)):
        if test1[i] < test2[i]:
            break
        elif test1[i] == test2[i]:
            continue
        else:
            holder = names_list[i]
            names_list[place-1] = names_list[place]
            names_list[place] = holder


def move_down(names_list, place, a):
    test1 = []
    for letter in names_list[place - 1][0]:
        test1.append(a[letter])
    test2 = []
    for letter in names_list[place - 2][0]:
        test2.append(a[letter])
    for i in range(len(test1)):
        if test1[i] > test2[i]:
            break
        elif test1[i] == test2[i]:
            continue
        else:
            holder = names_list[i]
            names_list[place - 1] = names_list[place - 2]
            names_list[place] = holder


def rank(st, we, n):
    print(st, we, n)
    p = n
    if len(st) == 0:
        return "No participants"
    elif len(st.split(',')) < n:
        return "Not enough participants"
    alpha = dict(zip(ascii_lowercase, range(1, 28)))
    testList = st.lower().split(',')
    names_num = [0 for name in testList]
    st_orig = dict(zip(testList, st.split(',')))
    for name in testList:
        names_num[testList.index(name)] += len(name)
        for letter in name.lower():
            names_num[testList.index(name)] += alpha[letter]
    for i in range(len(names_num)):
        names_num[i] *= we[i]
    ranks = []
    for i in testList:
        ranks.append([i, names_num[testList.index(i)]])
    ranks = sorted(ranks, key=itemgetter(1), reverse=True)
    if n != len(testList):

        # split test, add move_up/move_down

        if (ranks[n-1][1] == ranks[n][1]):
            move_up(ranks, p, alpha)
        elif (n > 1) and (ranks[n-2][1] == ranks[n-1][1]):
            move_down(ranks, p, alpha)
    else:
        if ranks[n-2][1] == ranks[n-1][1]:
            move_up(ranks, p, alpha)

    return st_orig[ranks[n-1][0]]


rank("Benjamin,James,Madison,David,Natalie,Sophia,Emily,Grace,Addison,Olivia,Ethan,Emma,Samantha,Andrew,Aubrey,Michael,Aiden,Daniel,Avery,Mia,Alexander,Chloe,Noah", [
     3, 5, 3, 2, 2, 1, 2, 2, 3, 2, 4, 2, 3, 4, 2, 3, 5, 5, 1, 3, 3, 1, 4], 5)
