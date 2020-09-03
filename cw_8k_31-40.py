8 kyu
Grasshopper - Grade book
Python:


def get_grade(s1, s2, s3):
    grades = (sum([s1, s2, s3])) / 3
    if grades >= 90:
        return "A"
    elif grades >= 80:
        return "B"
    elif grades >= 70:
        return "C"
    elif grades >= 60:
        return "D"
    else:
        return "F"


1 day agoRefactorDiscuss

8 kyu
Remove String Spaces
Python:


def no_space(x): return x.replace(" ", '')


1 day agoRefactor

8 kyu
Opposite number
Python:


def opposite(number):
    return number * - 1


1 day agoRefactorDiscuss


8 kyu
Century From Year
Python:


def century(year):

    # Finish this :)
    if len(str(year)) <= 2:
        return 1
    answer = str(year)[:-2]
    if str(year).endswith('00'):
        return int(answer)
    else:
        return int(answer)+1


1 week agoRefactorDiscuss

8 kyu
Logical calculator
Python:


def logical_calc(array, op):
    # and
    if op.upper() == "AND":
        for item in array:
            if item == True:
                continue
            else:
                return False
        return True
    # or
    if op.upper() == "OR":
        counter = 0
        for item in array:
            if item == True:
                counter += 1
                continue
            else:
                continue
        if counter >= 1:
            return True
        else:
            return False
    # xor
    tcount = 0
    for i in array:
        if i == True:
            tcount += 1
    if tcount % 2 != 0:
        return True
    else:
        return False


8 kyu
Simple Fun  # 1: Seats in Theater
Python:


def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - (col-1)) * (tot_rows - row)

    8 kyu


How good are you really?
Python:


def better_than_average(class_points, your_points):
    return your_points > sum(class_points)/len(class_points)


1 week agoRefactorDiscuss

8 kyu
Reversed Words
Python:


def reverseWords(str):
    str = str.split()
    str = str[::-1]
    str = ' '.join(str)
    return str


1 week agoRefactorDiscuss

8 kyu
How many stairs will Suzuki climb in 20 years?
Python:


def stairs_in_20(stairs): return sum([sum(i) for i in stairs]) * 20


# longform
#     total_stairs = []
#     for i in stairs:
#         total_stairs.append(sum(i))
#     return sum(total_stairs)*20
1 week agoRefactorDiscuss

8 kyu
Bin to Decimal
Python:


def bin_to_decimal(inp): return int(inp, 2)


1 week agoRefactorDiscuss

########################
########################
########################
