import itertools

def get_permutations(s, n):
    result = sorted(itertools.permutations(s,n))
    for i in range(len(result)):
        result[i] = ''.join(list(result[i]))
    return result

print(get_permutations("cat", 2))