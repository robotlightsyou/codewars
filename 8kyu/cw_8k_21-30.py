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
