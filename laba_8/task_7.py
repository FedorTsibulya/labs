import itertools

def get_combinations_with_r(s, n):
    result = sorted(itertools.combinations_with_replacement(s,n))
    for i in range(len(result)):
        result[i] = ''.join(sorted(list(result[i])))
    return result

print(get_combinations_with_r("cat", 2))
