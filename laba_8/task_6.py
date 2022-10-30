import itertools

def get_combinations(s, n):
    result = []
    for i in range(n):
        elements = []
        A = itertools.combinations(s, i+1)
        for j in A:
            elements.append(''.join(sorted(j)))
        elements.sort()
        result.extend(elements)
    return result

print((get_combinations('cat', 2)))