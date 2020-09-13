# 8 kyu Opposite Number
# Very simple, given a number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34


def opposite(number):
    return number * -1

###########
# 8 kyu Remove string spaces

# Simple, remove the spaces from the string, then return the resultant string.


def no_space(x): return x.replace(" ", "")


######################

# 8 kyu Grasshopper Grade Book

# Complete the function so that it finds the mean of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
# #

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


####################
# 7 kyu Largest Common Divisor
# Find the greatest common divisor of two positive integers. The integers can be large, so
# you need to find a clever solution.

# The inputs x and y are always greater or equal to 1, so the the greatest common divisor
# will always be an integer that is also greater or equal to 1.
# Try to make your own gcd method without importing stuff


def mygcd(x, y):
    ans = [x, y]
    ans = list(map(abs, sorted(ans, reverse=True)))
    # dividend = divisor quotient remainder
    dividend = ans[0]
    divisor = ans[1]
    quo = dividend // divisor
    rem = dividend % divisor
    if rem == 0:
        return divisor
    else:
        return mygcd(divisor, rem)

    print(ans)


mygcd(30, -12)  # ,6)

##########
