7 kyu
Sum of two lowest positive integers
Python:


def sum_two_smallest_numbers(numbers):
    lowest = min(numbers)
    numbers.remove(lowest)
    second = min(numbers)
    return lowest + second


7 kyu(8????)
Make a function that does arithmetic!
Python:
def arithmetic(a, b, operator):
    if operator == 'add':
        return a+b
    if operator == 'subtract':
        return a-b
    if operator == 'multiply':
        return a*b
    if operator == 'divide':
        return a/b



7 kyu
Sort Out The Men From Boys
Python:
def men_from_boys(arr):
    odds = []
    evens = []
    for i in arr:
        if i % 2 == 0:
            if i not in evens:
                evens.append(i)
        if i % 2 != 0:
            if i not in odds:
                odds.append(i)
    evens.sort()
    odds.sort(reverse=True)
    for number in odds:
        evens.append(number)
    
    return evens





7 kyu
Get the Middle Character
Python:
def get_middle(s):
    sample = list(s)
    if len(s) % 2 == 0:
        while len(''.join(sample)) > 2:
            sample.pop(0)
            sample.pop(-1)
    else:
        t = len(s)//2
        sample = s[t]
    return ''.join(sample)

         
        
1 week agoRefactorDiscuss

7 kyu
Printer Errors
Python:
import re
def printer_error(s):
    myAlpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    colErr = 0
    printerRegex = re.compile(r'^\w[a-mA-M]+$')
    if not printerRegex.match(s):
        printList = list(s)
        for i in printList:
            if i not in myAlpha:
                colErr +=1
        return str(colErr) + '/' + str(len(s))
                
   
1 week agoRefactorDiscuss

7 kyu
Number of People in the Bus
Python:
def number(bus_stops):
    total_pass = []
    for k,v in bus_stops:
        total_pass.append(k-v)
    return sum(total_pass)
1 week agoRefactorDiscuss
7 kyu
Powers of 3
Python:
def largestPower(N):
    if N <2:
        return -1
    ex = 1
    answer = [0]
    while 3**ex < N:
        answer.append(ex)
        ex += 1
    return answer[-1]
    
1 week agoRefactorDiscuss

7 kyu
Alphabetical Addition
Python:
def add_letters(*letters):
    if not letters:
        return 'z'
    else:
      nums = []
      for i in range(1, 27):
          nums.append(i)
      alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
      master = dict(zip(alpha.split(), nums))
      toAdd = []
      for i in letters:
          toAdd.append(master[i])
      toAdd = sum(toAdd)
      while toAdd >26:
          toAdd -= 26
      masterBackward = dict(zip(nums, alpha.split()))
      return masterBackward[toAdd]    
1 week agoRefactorDiscuss

7 kyu
Remove the minimum
Python:
def remove_smallest(numbers):
    answer = []
    counter = 0
    # check for empty set
    if numbers == []:
        return answer
    else:
        lowest = min(numbers)
        for i in numbers:
            # check if first iteration of lowest number
            if i != lowest or counter != 0:
                answer.append(i)
            # skip first lowest number
            elif i == lowest: 
                counter +=1
                continue
        return answer
    
1 week agoRefactorDiscuss

7 kyu
Regex validate PIN code
Python:
import re
def validate_pin(pin):
    if pin.isdecimal():
      shortRegex = re.compile(r'^\d{4}$')
      longRegex = re.compile(r'^\d{6}$')
      if shortRegex.search(pin) or longRegex.search(pin):
          return True
      else:
          return False
    else:
        return False
      # return true or false
1 week agoRefactorDiscuss

7 kyu
Beginner Series #3 Sum of Numbers
Python:
def get_sum(a,b):
    gapSum = []
    entry = [a,b]
    entry.sort()
    first = entry[0]
    last = entry[1]
    if a==b:
        return a
    else:
        for i in range(first,last+1):
            gapSum.append(i)
        return sum(gapSum)
        
1 week agoRefactorDiscuss

