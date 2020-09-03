from collections import Counter
#import timeit


def best(arr):
    d = Counter(arr)
    result = {}
    for k, v in d.items():
        if d[k] == max(d.values()):
            result[k] = v
    return max(result.keys())


def better(arr):
    d = {}
    result = {}
    for i in set(arr):
        d[i] = arr.count(i)
    for k, v in d.items():
        if d[k] == max(d.values()):
            result[k] = v
    return max(result.keys())


test1 = best([12, 10, 8, 12, 7, 6, 4, 10, 12])
test2 = better([12, 10, 8, 12, 7, 6, 4, 10, 12])
test3 = best([12, 10, 8, 12, 7, 6, 4, 10, 10])
test4 = better([12, 10, 8, 12, 7, 6, 4, 10, 10])

if __name__ == "__main__":
    import timeit
    print('test1 = ' + str(timeit.timeit(
        stmt='best([12, 10, 8, 12, 7, 6, 4, 10, 12])', setup='from __main__ import best', number=10000)))
    print('test2 = ' + str(timeit.timeit(
        stmt='better([12, 10, 8, 12, 7, 6, 4, 10, 12])', setup='from __main__ import better', number=10000)))
    print('test3 = ' + str(timeit.timeit(
        stmt='best([12, 10, 8, 12, 7, 6, 4, 10, 10])', setup='from __main__ import best', number=10000)))
    print('test4 = ' + str(timeit.timeit(
        stmt='better([12, 10, 8, 12, 7, 6, 4, 10, 10])', setup='from __main__ import better', number=10000)))
