#################
# Find a series of odd integers that sum to cube of n


def find_summands(n):
    ans = []
    low = n ** 2 - (n - 1)
    high = (n ** 2 + (n - 1)) + 1
    return [i for i in range(low, high+1, 2)]


################
