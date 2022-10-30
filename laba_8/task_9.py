import itertools

def maximize(lists, m):
    summ = 0
    for i in itertools.starmap(max,lists):
        summ += i**2
    return summ % m

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, m=1000))
