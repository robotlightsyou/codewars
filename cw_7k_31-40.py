7 kyu
Sum of Odd Cubed Numbers
Python:
def cube_odd(arr):
    try:
        return sum([i**3 for i in arr if i%2!=0])
    except:    
        return None



7 kyu
Convert the score
Python:
def scoreboard(string):
    nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'nil': 0}
    return [nums[i] for i in string.split() if i in nums]

# longform
#     score = []
#     for i in string.split():
#         if i in nums:
#             score.append(nums[i])
#     return score



7 kyu
Simple Fun #74: Growing Plant
Python:
def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    counter = 1
    while height < desiredHeight:
        height += upSpeed 
        if height < desiredHeight:
            counter +=1
            height -= downSpeed
    return counter
2 days agoRefactorDiscuss

7 kyu
Odder Than the Rest
Python:
def odd_one(arr):
    for i,j in enumerate(arr):
        if j % 2 != 0:
            return i
    return -1
2 days agoRefactorDiscuss


7 kyu
Sum of Array Averages
Python:
import math
def sum_average(arr):
    return math.floor(sum([sum(i)/len(i) for i in arr]))
    
# Longform
#     for i in arr:
#         ans.append(sum(i) / len(i))
#     return math.floor(sum(ans))
    
1 day agoRefactorDiscuss

7 kyu
Greatest common divisor
Python:
def mygcd(x,y):
    ans = [x,y]
    ans = list(map(abs, sorted(ans, reverse = True)))
    dividend = ans[0]
    divisor = ans[1]
    quo = dividend // divisor
    rem = dividend % divisor
    if rem == 0:
        return divisor
    else:
        return mygcd(divisor, rem)
1 day agoRefactorDiscuss


7 kyu
Two to One
Python:
def longest(s1, s2):
    return "".join(sorted(set(s1+s2)))
1 day agoRefactorDiscuss



7 kyu
Minimize Sum Of Array (Array Series #1)
Python:
def min_sum(arr):
    arr = sorted(arr)
    ans = (arr[0] * arr[-1])
    if len(arr) > 2:
        return ans + min_sum(arr[1:-1])
    else: 
        return ans

7 kyu
Form The Minimum
Python:
def min_value(digits):
    ans = []
    multi = 1
    for i in sorted(set(digits), reverse = True):
        ans.append(multi * i)
        multi *= 10
    return sum(ans)
8 hours agoRefactorDiscuss


7 kyu
Maximum Triplet Sum (Array Series #7)
Python:
def max_tri_sum(numbers):
    return sum([i for i in list(sorted(set(numbers)))[-3:]])
    
8 hours agoRefactorDiscuss
