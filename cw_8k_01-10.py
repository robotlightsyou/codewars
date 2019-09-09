
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
