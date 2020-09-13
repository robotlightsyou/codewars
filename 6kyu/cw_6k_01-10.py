6 kyu
Replace With Alphabet Position
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
Python:


def alphabet_position(text):
    nums = []
    for i in range(1, 27):
        nums.append(i)
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    master = dict(zip(alpha.split(), nums))
    newText = []
    for letter in text:
        if letter.lower() in master.keys():
            newText.append(master[letter.lower()])
    newText = " ".join(map(str, newText))
    return newText


6 kyu
Multi-tap Keypad Text Entry on an Old Mobile Phone
Python:
import re
def presses(phrase):
    oneRegex = re.compile(r'[a|d|g|j|m|p|t|w|1|\*\#\s]')
    twoRegex = re.compile(r'[b|e|h|k|n|q|u|x|0]')
    threeRegex = re.compile(r'[c|f|i|l|o|r|v|y]')
    fourRegex = re.compile(r'[s|z|2-6|8]')
    fiveRegex = re.compile(r'[7|9]')
    
    total_presses = 0
    #If someone could point to a tidier way to write this block
    #it would be much appreciated
    for letter in phrase.lower():
        if oneRegex.match(letter):
            total_presses += 1 
        if twoRegex.match(letter):
            total_presses += 2 
        if threeRegex.match(letter):
            total_presses += 3
        if fourRegex.match(letter):
            total_presses += 4 
        if fiveRegex.match(letter):
            total_presses += 5
    return total_presses
1 week agoRefactorDiscuss

6 kyu
Count characters in your string
Python:
import collections
def count(string):
    answer = collections.Counter(string)
    return answer



6 kyu
Are they the "same"?
Python:
def comp(a, b):
    if (a == [] and b == []) or (a != [] and b != []):
        return sorted(a) == sorted([i**0.5 for i in b])
    else:
        return False
 

 6 kyu
Are they the "same"?
Python:
def comp(a, b):
    if (a == [] and b == []) or (a != [] and b != []):
        return sorted(a) == sorted([i**0.5 for i in b])
    else:
        return False
 
 6 kyu
Take a Ten Minute Walk
Python:
def isValidWalk(walk):
    if len(walk) == 10:
        return walk.count("e") == walk.count("w") and \
                walk.count("n") == walk.count("s")
    else:
        return False
     
3 days agoRefactorDiscuss
def isValidWalk(walk):
    if len(walk) == 10:
        return walk.count("e") == walk.count("w") and \
                walk.count("n") == walk.count("s")
    else:
        return False
3 days agoRefactor


6 kyu
Prize Draw
Python:
from string import ascii_lowercase
from operator import itemgetter

def move_up(names_list, place, a):    
    if names_list[place] != "":
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
        if (ranks[n-1][1] == ranks[n][1]):
            move_up(ranks, p, alpha)
        elif (n > 1) and (ranks[n-2][1] == ranks[n-1][1]):
            move_down(ranks, p, alpha)     
    else:
        if ranks[n-2][1] == ranks[n-1][1]:
            move_up(ranks, p, alpha)
    return st_orig[ranks[n-1][0]]
2 days agoRefactorDiscuss

6 kyu
Duplicate Encoder
Python:
import collections
def duplicate_encode(word):
    final = ''
    ans = collections.Counter(word.lower())
    for letter in word.lower():
        if ans[letter] > 1:
            final = final + ')'
        else:
            final = final + '('
    return final
2 days agoRefactorDiscuss


6 kyu
compute cube as sums
Python:
def find_summands(n):
    ans = []
    low = n ** 2 - (n - 1)
    high = (n ** 2 + (n - 1)) + 1
    return [i for i in range(low, high+1, 2)]
1 day agoRefactorDiscuss



6 kyu
Vasya - Clerk
Python:
def tickets(people):
    bills = [str(i) for i in people]
    change = {"25":0, "50":0, "100":0}
    for i in bills:
        if i == "25":
            change["25"] += 1
        if i == "50":
            if change["25"] >= 1:
                change["50"] += 1
                change["25"] -= 1
            else:
                return "NO"
        if i == "100":
            if change["50"] == 0 and change["25"] < 3:
                return "NO"
            elif change["50"] == 1 and change["25"] == 0:
                return "NO"
            elif change["50"] == 0 and change["25"] >= 3:
                change["25"] -= 3
            else:
                change["50"] -= 1
                change["25"] -= 1
        if change["25"] < 0 or change["50"] < 0:
            return "NO"
    return "YES"


