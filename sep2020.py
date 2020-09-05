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

"""6kyu Heroes of Might and Magic II: 1v1 combat"""

class Monster:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)
        self.current_hp = self.hitpoints
            
    def no_lives(self):
        return self.number <= 0
        
    def attack(self, defend):
        round_damage = self.number * self.damage
        while round_damage > 0:
            if round_damage >= defend.current_hp:
                defend.number -= 1
                round_damage -= defend.current_hp
                defend.current_hp = defend.hitpoints
            else:
                defend.current_hp -= round_damage
                round_damage = 0
            if defend.no_lives():
                return True
            
def who_would_win(mon1, mon2):
    m1 = Monster(mon1)
    m2 = Monster(mon2)
    
    while True:
        if m1.attack(m2):
            return f"{m1.number} {m1.type}(s) won"
        if m2.attack(m1):
            return f"{m2.number} {m2.type}(s) won"

"""6kyu Counting Duplicates"""

def duplicate_count(text):
    ans = {}
    for i in text.lower():
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
    dups = len([k for k in ans if ans[k] > 1])
    return dups

"""6 kyu Another one down, survival of the fittest"""

def remove_smallest(n, arr):
    result = arr[:]
    if arr == [] or n <= 0: return arr
    if n > len(arr): return []
    while n > 0:
        result.remove(min(result))
        n -= 1
    return result

