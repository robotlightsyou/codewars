
7 kyu
Product Array(Array Series  # 5)
Python:
import copy
import functools
import operator

def product_array(numbers):
    ans=[]
    for i in range(len(numbers)):
        test=copy.deepcopy(numbers)
        test.pop(i)
        ans.append(functools.reduce(operator.mul, test, 1))
    return ans
9 hours agoRefactorDiscuss

7 kyu
Array Leaders(Array Series  # 3)
Python:
def array_leaders(numbers):
    return [numbers[i] for i in range(len(numbers)) if numbers[i] > sum(numbers[i+1:])]
19 hours agoRefactorDiscuss

7 kyu
Product Of Maximums Of Array(Array Series  # 2)
Python:
def max_product(lst, n):
    ans=1
    lst=sorted(lst)[-n:]
    for i in lst:
        ans *= i
    return ans

7 kyu
Maximum Product
Python:
def adjacent_element_product(array):
    max_prod=array[0] * array[1]
    for i, j in enumerate(array[1:-1]):
        if j * array[i+2] > max_prod:
            max_prod=j * array[i+2]
    return max_prod
29 minutes agoRefactorDiscuss

7 kyu
Minimum Steps(Array Series  # 6)
Python:
def minimum_steps(numbers, value):
    numbers=(sorted(numbers))
    if value <= numbers[0]:
        return 0
    sum=numbers[0] + numbers[1]
    if sum >= value:
        return 1
    else:
        return 1 + minimum_steps(numbers[1:], value - numbers[0])

52 minutes agoRefactorDiscuss
def minimum_steps(numbers, value):
    x=min(numbers)
    counter=0
    for i in sorted(numbers)[1:]:
        if x < value:
            x += i
            counter += 1
    return counter


7 kyu
Disemvowel Trolls - remove vowels from string, y not a vowel


def disemvowel(string):
    return "".join([i for i in string if i not in "aeiouAEIOU"])

7 kyu
Credit Card Mask

# return masked string
def maskify(cc):
    for i in range(len(cc[:-4])):
        cc=cc[:i] + "#" + cc[i+1:]
    return cc

# 7 kyu - Numericals of a string - return a string replacing each character with its appearance count

def numericals(s):
    r=""
    myDict={}
    for char in s:
        if char in myDict:
            myDict[char] += 1
            r += str(myDict[char])
        else:
            myDict[char]=1
            r += str(myDict[char])
    return r
