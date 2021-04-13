
8 kyu
Palindrome Strings
Palindrome strings
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This includes capital letters, punctuation, and word dividers.

Implement a function that checks if something is a palindrome.

Examples
isPalindrome("anna") == > true
isPalindrome("walter") == > false
isPalindrome(12321) == > true
isPalindrome(123456) == > false
Python:


def is_palindrome(string):
    return str(string) == str(string)[::-1]


1 week agoRefactorDiscuss


8 kyu
Multiply
The code does not execute properly. Try to figure out why.


def multiply(a, b):
    a * b


Python:


def multiply(a, b):
    result = a * b
    return result


8 kyu
You only need one - Beginner
Python:


def check(seq, elem):
    return elem in seq


1 week agoRefactorDiscuss

8 kyu
String repeat
Python:


def repeat_str(repeat, string):
    string *= repeat
    return string


1 week agoRefactorDiscuss

8 kyu
Is the string uppercase?
Is the string uppercase?
Task
Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

is_uppercase("c") == False
is_uppercase("C") == True
Python:


def is_uppercase(inp):
    for letter in inp:
        if not letter.isupper() and letter.isalpha():
            return False
    return True


8 kyu
Beginner - Lost Without a Map
Python:


def maps(a):
    newList = []
    for item in a:
        newList.append(item*2)
    return newList


1 week agoRefactorDiscuss

8 kyu
Is this my tail?
Python:


def correct_tail(body, tail):
    #     sub = body.substr(len(body)-len(tail.length))
    #     if sub == tail:
    if body.endswith(tail):
        return True
    else:
        return False


8 kyu
Sum Arrays
Python:


def sum_array(a):
    total = 0
    for item in a:
        total += item
    return total


8 kyu
Get Nth Even Number
Python:


def nth_even(n):
    return 2*(n-1)


8 kyu
Get the mean of an array
Python:


def get_average(marks):
    counter = 0
    total = 0
    for i in marks:
        total += i
        counter += 1
    return total // counter


1 week agoRefactorDiscuss

########################
########################
########################
8 kyu
Regex count lowercase letters
Python:


def lowercase_count(strng):
    #lowerRegex = re.compile(r'\w[a-z]+')
    lowerRegex = re.findall('[a-z]+', strng)
    lowerRegex = ''.join(lowerRegex)
    return len(lowerRegex)


1 week agoRefactorDiscuss


8 kyu
Count Odd Numbers below n
Python:


def odd_count(n):
    if (n-1) % 2 == 0:
        return (n-1)//2
    else:
        return (n)//2


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

8 kyu
DNA to RNA Conversion
Python:


def DNAtoRNA(dna): return ''.join(
    [letter if letter != "T" else "U" for letter in dna])

# longform
#     rna = []
#     for letter in dna:
#         if letter != 'T':
#             rna.append(letter)
#         else:
#             rna.append('U')
#     return ''.join(rna)


8 kyu

A Needle in the Haystack
Python:


def find_needle(haystack):
    return 'found the needle at position ' + str(haystack.index("needle"))


8 kyu
Grasshopper - Summation
Python:


def summation(num):
    return sum(i for i in range(num+1))


2 days agoRefactorDiscuss

8 kyu
Find the Integral
Python:


def integrate(coefficient, exponent):
    exponent += 1
    coefficient //= exponent
    ans = "{}x^{}".format(coefficient, exponent)
    return ans


3 days agoRefactorDiscuss

8 kyu
Sum of positive
Python:


def positive_sum(arr):
    return sum([i for i in arr if i > 0])


#     ans = []
#     for i in arr:
#         if i > 0:
#             ans.append(i)
#     return sum(ans)
3 days agoRefactorDiscuss

8 kyu
Well of Ideas - Easy Version
Python:


def well(x):
    isgood = 0
    for i in x:
        if i.lower() == "good":
            isgood += 1
    if isgood >= 3:
        return "I smell a series!"
    elif isgood > 0:
        return "Publish!"
    else:
        return "Fail!"


3 days agoRefactorDiscuss

########################
########################
########################
8 kyu
Convert a string to an array
Python:


def string_to_array(s):
    if s == "":
        return [""]
    else:
        return s.split()


1 week agoRefactorDiscuss

8 kyu
Is it a palindrome?
Python:


def is_palindrome(s):
    return s.lower() == s.lower()[::-1]


1 week agoRefactorDiscuss

8 kyu
Count by X
Python:


def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    answer = []
    for i in range(1, n+1):
        answer.append(i*x)
    return answer


1 week agoRefactorDiscuss

8 kyu
Counting sheep...
Python:


def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)


1 week agoRefactorDiscuss

8 kyu
Difference of Volumes of Cuboids
Python:


def find_difference(a, b):
    volA = 1
    for i in range(len(a)):
        volA *= a[i]
    volB = 1
    for i in range(len(a)):
        volB *= b[i]
    myL = [volA, volB]
    myL.sort()
    return myL[1]-myL[0]


1 week agoRefactorDiscuss

8 kyu
Stringy Strings
Python:


def stringy(size):
    answer = ""
    number = '1'
    for i in range(size):
        answer += number
        if number == '1':
            number = '0'
        else:
            number = '1'
    return answer

    # Good Luck!
1 week agoRefactorDiscuss

8 kyu
If you can't sleep, just count sheep!!
Python:


def count_sheep(n):
    sheeps = ""
    for i in range(n):
        sheeps = sheeps + str(i+1) + ' sheep...'
    return sheeps


1 week agoRefactorDiscuss

8 kyu
Basic variable assignment
Python:
a = "code"
b = "wa.rs"
name = a + b
1 week agoRefactorDiscuss


8 kyu
L1: Set Alarm
Python:


def set_alarm(employed, vacation):
    return employed and not vacation


1 week agoRefactorDiscuss

8 kyu
Convert a Number to a String!
Python:


def number_to_string(num):
    return str(num)


1 week agoRefactorDiscuss

########################
########################
########################
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
