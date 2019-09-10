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
