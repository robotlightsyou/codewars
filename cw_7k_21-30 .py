
7 kyu
Eliminate the intruders! Bit manipulation
Python:
def eliminate_set_bits(number):  
    if number.count('1') == 0: 
        return 0
    else:    
        return int("1" * number.count('1'), 2)
    
1 week agoRefactorDiscuss

7 kyu
Negation of a Value
Python:
def negation_value(s, val): return bool(val if len(s) % 2 == 0 else not val)
    
1 week agoRefactorDiscuss

7 kyu
Sum of Cubes
Python:
def sum_cubes(n): return sum([i**3 for i in range(1, n+1)])

# Long form I wrote first, still new to lambdas/one liners
# def sum_cubes(n):
#     cube_list = []
#     for i in range(1,n+1):
#         cube_list.append(i**3)
#     return sum(cube_list)
    
1 week agoRefactorDiscuss

7 kyu
Row Weights
Python:
def row_weights(array):
    team1 = []
    team2 = []
    for i in range(len(array)):
        if i%2==0:
            team1.append(array[i])
        else:
            team2.append(array[i])
    return (sum(team1), sum(team2))
1 week agoRefactorDiscuss

7 kyu
Going to the cinema
Python:
import math
def movie(card, ticket, perc):
    print(card,ticket,perc)
    cTotal = float(card)
    tTotal = 0
    cTicket = ticket
    counter = 0
    while math.ceil(cTotal) >= tTotal:
        counter += 1
        cTicket *= float(perc)
        cTotal += (cTicket)
        tTotal += ticket
    return counter
        
6 days agoRefactorDiscuss

7 kyu
Sum of Odd Cubed Numbers
Python:
def cube_odd(arr):
    try:
        return sum([i**3 for i in arr if i%2!=0])
    except:    
        return None
6 days agoRefactorDiscuss

goRefactorDiscuss


7 kyu
Tidy Number (Special Numbers Series #9)
Python:
def tidyNumber(n):
    test = str(n)
    for i in range(len(test[:-1])):
        if int(test[i]) > int(test[i+1]):
            return False
    return True
1 week agoRefactorDiscuss

7 kyu
Maximum Gap (Array Series #4)
Python:
def max_gap(numbers):
    largest_gap = 0
    t = sorted(numbers)
    for i in range(len(t)-1):
        test = abs(t[i+1] - t[i])
        if test > largest_gap:
            largest_gap = test
    return largest_gap
    
1 week agoRefactorDiscuss

7 kyu
Aerial Firefighting
Python:
# return the minimum required waterbombs to extinguish the fires in the array
def waterbombs(fire, w):
    test_string = ''
    total_bombs = 0
    for i in fire:
        if i == 'x':
            if len(test_string) < w:
                test_string += i
            else:
                total_bombs += 1
                test_string = i
        else:
            if test_string != '':
                total_bombs += 1
                test_string = ''
    if test_string != '':
        total_bombs += 1
    return total_bombs


    7 kyu
Going to the cinema
Python:
import math
def movie(card, ticket, perc):
    print(card,ticket,perc)
    cTotal = float(card)
    tTotal = 0
    cTicket = ticket
    counter = 0
    while math.ceil(cTotal) >= tTotal:
        counter += 1
        cTicket *= float(perc)
        cTotal += (cTicket)
        tTotal += ticket
    return counter
        
6 days agoRefactorDiscuss

