"""6 kyu Sort the Odd: sort odd numbers but leave evens in place"""

def sort_array(source_array):
    odds = sorted([i for i in source_array if i % 2 != 0], reverse = True)
    new_array = []
    for i in source_array:
        if i % 2:
            new_array.append(odds.pop())
        else:
            new_array.append(i)
    return new_array

"""6 kyu Who Likes It: duplicate FB likes statement"""

def likes(names):
    x = len(names)
    if x  == 0:
        return "no one likes this"
    elif x == 1:
        return f'{names[0]} likes this'
    elif 2 <= x <= 3:
        liked = ""
        for i in names[:-2]:
            liked += f'{i}, '
        liked += f'{names[-2]} and {names[-1]} like this'
        return liked
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'

"""6 kyu Array.diff: subtract all occurrances of list b items in list a"""

def array_diff(a, b):
    return [i for i in a if i not in b]

"""7kyu Sum nth term of Series"""

def series_sum(n):
    denom = 1
    series = [1]
    if n > 1:
        for i in range(1, n):
            denom += 3
            series.append(1/denom)
    return format(sum([i for i in series[:n]]), '.2f')

"""6kyu Mexican Wave"""

def wave(people):
    out = []
    spaces = 0
    for i,v in enumerate(people):
        offset = i - spaces
        if v != " ":
            out.append(list(people))
            if out[offset][i].isalpha():
                out[offset][i] = out[offset][i].upper()
            out[offset] = "".join(out[offset])
        else:
            spaces += 1
    return out

"""6 kyu two sum"""

from itertools  import combinations
def two_sum(numbers, target):
    answer = []
    out = []
    for t in combinations(numbers, 2):
        if sum(t) == target:
            out = [t[0],t[1]]
            break
    if out[0] == out[1]: 
        answer.append(numbers.index(out[0]))
        numbers.pop(numbers.index(out[0]))
        answer.append((numbers.index(out[1])) + 1)
    else:
        answer.append(numbers.index(out[0]))
        answer.append((numbers.index(out[1])))
    return answer


"""6kyu Bouncing Balls: How many times will a ball pass a window?"""

def bouncing_ball(h, bounce, window):
    count = 0
    if not 0 < bounce < 1:
        return -1
    while h > window:
        count += 1
        h *= bounce
    return 2 * count - 1
